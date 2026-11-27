import shutil
import cv2
import numpy as np
import kagglehub
import matplotlib.pyplot as plt
from pathlib import Path

# The images are downloaded, so they live in the cache folder, not in the repo.
CACHE_DIR = Path.home() / ".cache" / "ml-notebooks" / "computer-vision" / "07-quiz-i"
DATA_PATH = CACHE_DIR / "data"

# Pokemon Images Dataset (Kaggle: kvpratama/pokemon-images-dataset). Same
# images and targets as 06-image-matching.
CANDIDATE_IDS = [4, 7, 25, 92, 252, 258, 393, 495]
TARGETS = {
    "Object.png": (252, 20, 1.8),
    "Object2.png": (7, -15, 1.5),
    "Object3.png": (92, 35, 2.0),
}


def make_target(image, angle, scale):
    h, w = image.shape[:2]
    rotation = cv2.getRotationMatrix2D((w / 2, h / 2), angle, 1.0)
    rotated = cv2.warpAffine(image, rotation, (w, h), borderValue=(255, 255, 255))
    return cv2.resize(rotated, None, fx=scale, fy=scale, interpolation=cv2.INTER_CUBIC)


def prepare_dataset():
    if DATA_PATH.exists():
        return

    source = Path(kagglehub.dataset_download("kvpratama/pokemon-images-dataset"))
    source = source / "pokemon_jpg" / "pokemon_jpg"

    DATA_PATH.mkdir(parents=True, exist_ok=True)
    for pokemon_id in CANDIDATE_IDS:
        shutil.copy(source / f"{pokemon_id}.jpg", DATA_PATH / f"{pokemon_id}.jpg")

    for name, (pokemon_id, angle, scale) in TARGETS.items():
        image = cv2.imread(str(source / f"{pokemon_id}.jpg"))
        cv2.imwrite(str(CACHE_DIR / name), make_target(image, angle, scale))


prepare_dataset()

data = [cv2.imread(str(path)) for path in sorted(DATA_PATH.iterdir())]

images = [str(CACHE_DIR / name) for name in TARGETS]

akaze = cv2.AKAZE_create()
flann = cv2.FlannBasedMatcher(dict(algorithm=1), dict(checks=50))

for obj_path in images:
    obj = cv2.imread(obj_path)
    obj_gray = cv2.cvtColor(obj, cv2.COLOR_BGR2GRAY)
    obj_gray = cv2.medianBlur(obj_gray, ksize=5)
    obj_gray = cv2.equalizeHist(obj_gray)
    obj_kp, obj_desc = akaze.detectAndCompute(obj_gray, None)

    best_match = 0
    for img in data:
        img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        img_gray = cv2.medianBlur(img_gray, ksize=5)
        img_gray = cv2.equalizeHist(img_gray)
        img_kp, img_desc = akaze.detectAndCompute(img_gray, None)

        matches = flann.knnMatch(np.float32(obj_desc), np.float32(img_desc), 2)
        good = [[m] for m, n in matches if m.distance < 0.7 * n.distance]

        if best_match < len(good):
            best_match = len(good)
            best_match_data = {"img":img, "kp":img_kp, "good": good}

    result = cv2.drawMatchesKnn(
        obj,
        obj_kp,
        best_match_data["img"],
        best_match_data["kp"],
        best_match_data["good"],
        None,
        matchColor=[255, 0, 0],
        singlePointColor=[0, 0, 255],
    )

    plt.figure(figsize=(8, 6))
    plt.imshow(cv2.cvtColor(result, cv2.COLOR_BGR2RGB))
    plt.title(f"Best match for {obj_path}")
    plt.show()
