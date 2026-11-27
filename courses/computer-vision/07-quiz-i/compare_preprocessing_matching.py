import os
import shutil
import cv2
import numpy as np
import kagglehub
from pathlib import Path
from matplotlib import pyplot as plt

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

target_path = str(CACHE_DIR / "Object.png")
data_folder = str(DATA_PATH)


# Median Blur
def preprocess_v1(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    eq = cv2.equalizeHist(gray)
    blur = cv2.medianBlur(eq, 5)
    return blur


# Gaussian Blur
def preprocess_v2(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    eq = cv2.equalizeHist(gray)
    blur = cv2.GaussianBlur(eq, (3, 3), 0)
    return blur


def find_best_match(preprocess_func, title):
    target = cv2.imread(target_path)
    target = cv2.cvtColor(target, cv2.COLOR_BGR2RGB)
    target_gray = preprocess_func(target)

    akaze = cv2.AKAZE_create()
    kp_target, desc_target = akaze.detectAndCompute(target_gray, None)
    desc_target = np.float32(desc_target)

    flann = cv2.FlannBasedMatcher(dict(algorithm=1), dict(checks=50))

    best_match_count = 0
    best_match_img = None
    best_match_title = ""

    for filename in os.listdir(data_folder):
        img_path = os.path.join(data_folder, filename)
        scene = cv2.imread(img_path)
        scene = cv2.cvtColor(scene, cv2.COLOR_BGR2RGB)
        scene_gray = preprocess_func(scene)

        kp_scene, desc_scene = akaze.detectAndCompute(scene_gray, None)
        desc_scene = np.float32(desc_scene)
        matches = flann.knnMatch(desc_target, desc_scene, k=2)

        good = []
        for m, n in matches:
            if m.distance < 0.7 * n.distance:
                good.append([m])

        if len(good) > best_match_count:
            best_match_count = len(good)
            best_match_img = cv2.drawMatchesKnn(
                target,
                kp_target,
                scene,
                kp_scene,
                good,
                None,
                matchColor=[0, 255, 0],
                singlePointColor=[255, 0, 0],
            )
            best_match_title = filename

    plt.figure(figsize=(8, 6))
    plt.imshow(best_match_img)
    plt.title(f"{title} - Best Match: {best_match_title}")
    plt.axis(False)
    plt.show()


find_best_match(preprocess_v1, "Version 1 (Median Blur)")
target_path = str(CACHE_DIR / "Object2.png")
find_best_match(preprocess_v2, "Version 2 (Gaussian Blur)")

target_path = str(CACHE_DIR / "Object3.png")
find_best_match(preprocess_v2, "Version 2 (Gaussian Blur)")