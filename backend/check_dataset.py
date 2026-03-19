import os

DATASET_PATH = r"C:\Users\Fruity D\leaf-project\backend\dataset\Resized Image"

for plant in os.listdir(DATASET_PATH):
    plant_path = os.path.join(DATASET_PATH, plant)
    if os.path.isdir(plant_path):
        for disease in os.listdir(plant_path):
            disease_path = os.path.join(plant_path, disease)
            count = len(os.listdir(disease_path))
            print(f"{plant}/{disease}: {count}")