import cv2
import shutil
import numpy as np
import matplotlib.pyplot as plt
import kagglehub
from pathlib import Path

# The images are downloaded, so they live in the cache folder, not in the repo.
CACHE_DIR = Path.home() / ".cache" / "ml-notebooks" / "computer-vision" / "06-image-matching"
DATA_PATH = CACHE_DIR / "data"

# Pokemon Images Dataset (Kaggle: kvpratama/pokemon-images-dataset). Files are
# named by Pokedex number. These 8 are the candidate images.
CANDIDATE_IDS = [4, 7, 25, 92, 252, 258, 393, 495]

# Target objects: a candidate rotated and enlarged, so it is not an identical
# copy. File name -> (Pokedex number, rotation in degrees, scale).
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

object = cv2.imread(str(CACHE_DIR / "Object.png"))
# object = cv2.imread(str(CACHE_DIR / "Object2.png"))

# Preprocessing
## Color to RGB
object = cv2.cvtColor(object, cv2.COLOR_BGR2RGB)

# Akses dataset
data = []
for image_path in sorted(DATA_PATH.iterdir()):
    image_data = cv2.imread(str(image_path))
    data.append(image_data)

# Preprocessing

## RGB to Grayscale
grayscale_object = cv2.cvtColor(object, cv2.COLOR_RGB2GRAY)

## Median Blur
# grayscale_object = cv2.medianBlur(grayscale_object, ksize=5)

## Gausian Blur
grayscale_object = cv2.GaussianBlur(grayscale_object, ksize=(3, 3), sigmaX=1)

## Equ Histogram
grayscale_object = cv2.equalizeHist(grayscale_object)


# Feature Descriptor

## AKAZE -> Accelerated KAZE
akaze = cv2.AKAZE_create()

## ORB -> Oriented FAST and Rotated Brief
# orb = cv2.ORB_create()

## SHIFT -> Scale Invariant Feature Transform
# shift = cv2.SHIFT_create()

target_keypoint, target_descriptor = akaze.detectAndCompute(grayscale_object, None)
target_descriptor = np.float32(target_descriptor)

# Best Matches
best_match = 0

for index, img in enumerate(data):
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    grayscale_data = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    # grayscale_data = cv2.medianBlur(grayscale_data, 5)
    grayscale_data = cv2.GaussianBlur(grayscale_data, (3, 3), 1)
    grayscale_data = cv2.equalizeHist(grayscale_data)

    data_keypoint, data_descriptor = akaze.detectAndCompute(grayscale_data, None)
    data_descriptor = np.float32(data_descriptor)

    # Match using FLANN
    flann = cv2.FlannBasedMatcher(dict(algorithm=1), dict(checks=50))
    matcher = flann.knnMatch(target_descriptor, data_descriptor, 2)

    matchmask = [[0, 0] for _ in range(0, len(matcher))]

    current_matches = 0
    for i, (fm, sm) in enumerate(matcher):
        if fm.distance < 0.7 * sm.distance:
            matchmask[i] = [1, 0]  # mark as valid match
            current_matches += 1

    # Update best match
    if best_match < current_matches:
        best_match = current_matches
        best_match_data = {
            "image_data": img,
            "keypoint": data_keypoint,
            "descriptor": data_descriptor,
            "match": matcher,
            "matchmask": matchmask,
        }

# Plotting
result = cv2.drawMatchesKnn(
    object,
    target_keypoint,
    best_match_data["image_data"],
    best_match_data["keypoint"],
    best_match_data["match"],
    None,
    matchesMask=best_match_data["matchmask"],
    matchColor=[255, 0, 0],
    singlePointColor=[0, 0, 255],
)

plt.figure()
plt.imshow(result)
plt.title("Matching image")
plt.show()
