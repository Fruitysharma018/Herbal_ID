import tensorflow as tf
import numpy as np
from PIL import Image

MODEL_PATH = "model/mobilenetv2_leaf.h5"
LABELS_PATH = "model/labels.txt"

model = tf.keras.models.load_model(MODEL_PATH)

with open(LABELS_PATH) as f:
    class_names = [line.strip() for line in f.readlines()]

def preprocess_image(image_path):
    img = Image.open(image_path).convert("RGB")
    img = img.resize((224, 224))
    img = np.array(img) / 255.0
    img = np.expand_dims(img, axis=0)
    return img

def predict_leaf(image_path):
    print("Received image path:", image_path)

    img = preprocess_image(image_path)
    preds = model.predict(img)[0]

    idx = np.argmax(preds)
    confidence = round(float(preds[idx]) * 100, 2)
    label = class_names[idx]

    description = f"{label} leaf disease detected."

    return label, confidence, description