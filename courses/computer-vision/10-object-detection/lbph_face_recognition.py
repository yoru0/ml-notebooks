import cv2
import os
import shutil
import numpy as np
import kagglehub
from pathlib import Path

# The dataset is downloaded, so it lives in the cache folder, not in the repo.
CACHE_DIR = Path.home() / ".cache" / "ml-notebooks" / "computer-vision" / "10-object-detection"

# Labeled Faces in the Wild (Kaggle: jessicali9530/lfw-dataset). Three people
# with many photos each: the first 12 images are used for training (one folder
# per person) and the next 2 for testing (all in one flat folder).
PEOPLE = ["Colin_Powell", "Tony_Blair", "Donald_Rumsfeld"]
N_TRAIN = 12
N_TEST = 2


def prepare_dataset():
    train_dir = CACHE_DIR / "dataset" / "train"
    test_dir = CACHE_DIR / "dataset" / "test"
    if train_dir.exists() and test_dir.exists():
        return train_dir, test_dir

    lfw_path = Path(kagglehub.dataset_download("jessicali9530/lfw-dataset"))
    lfw_path = lfw_path / "lfw-deepfunneled" / "lfw-deepfunneled"

    test_dir.mkdir(parents=True, exist_ok=True)
    for person in PEOPLE:
        images = sorted((lfw_path / person).glob("*.jpg"))
        (train_dir / person).mkdir(parents=True, exist_ok=True)
        for image in images[:N_TRAIN]:
            shutil.copy(image, train_dir / person / image.name)
        for image in images[N_TRAIN : N_TRAIN + N_TEST]:
            shutil.copy(image, test_dir / image.name)

    return train_dir, test_dir


face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

train_path, test_path = prepare_dataset()

# Face Recognition (+ Training)
face_list = []
label_list = []

person_names = os.listdir(train_path)

for idx, name in enumerate(person_names):
    dir_name = f"{train_path}/{name}"
    for file_name in os.listdir(dir_name):
        file_path = f"{dir_name}/{file_name}"
        img = cv2.imread(file_path, cv2.IMREAD_GRAYSCALE)

        detected_faces = face_cascade.detectMultiScale(
            img, scaleFactor=1.2, minNeighbors=5
        )
        if len(detected_faces) < 1:
            continue

        for face in detected_faces:
            x, y, h, w = face
            face_img = img[y : y + h, x : x + w]

            face_list.append(face_img)
            label_list.append(idx)


# Face Detection (Testing)
recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.train(face_list, np.array(label_list))

for img_name in os.listdir(test_path):
    img_path = f"{test_path}/{img_name}"
    img = cv2.imread(img_path)
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    detected_faces = face_cascade.detectMultiScale(img_gray)

    if len(detected_faces) < 1:
        continue

    for face in detected_faces:
        x, y, h, w = face
        face_img = img_gray[y : y + h, x : x + w]

        label, confidence = recognizer.predict(face_img)

        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
        text = f"{person_names[label]}: {confidence:.2f}"
        cv2.putText(
            img, text, (x, y - 8), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2
        )
        cv2.imshow("Result", img)

    cv2.waitKey(0)
cv2.destroyAllWindows()
