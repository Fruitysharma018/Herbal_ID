import tensorflow as tf
import numpy as np
from tensorflow.keras.preprocessing import image
import json

model = tf.keras.models.load_model("model/mobilenet_leaf.h5")

with open("metadata/class_names.json") as f:
    class_names = json.load(f)

def predict_leaf(img_path):
    img = image.load_img(img_path, target_size=(224,224))
    img = image.img_to_array(img) / 255.0
    img = np.expand_dims(img, axis=0)

    preds = model.predict(img)[0]
    idx = int(np.argmax(preds))

    return class_names[str(idx)], float(preds[idx]) * 100

if __name__ == "__main__":
    label, conf = predict_leaf("test.jpg")
    print(label, conf)