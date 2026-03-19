# 🌿 Leaf Identification & Medicinal Recommendation System

A full-stack **Machine Learning + Web Application** that identifies plant leaves from images and provides **medicinal uses, symptoms, and remedies** based on the detected plant.

---

## 🚀 Features

* 🔍 **Leaf Identification using MobileNetV2**
* 🌱 Detects **plant + disease (if any)**
* 💊 Displays **medicinal uses, symptoms, and remedies**
* 🔐 User **Authentication (Login & Signup)**
* 📊 Stores **prediction history**
* ⚡ Fast API using **Flask**
* 🎨 Clean UI using **React (Vite)**

---

## 🧠 Tech Stack

### 🔹 Frontend

* React (Vite)
* CSS

### 🔹 Backend

* Flask
* TensorFlow / Keras
* SQLite
* Flask-CORS
* Flask-Bcrypt

### 🔹 ML Model

* MobileNetV2 (Transfer Learning)
* Trained on custom dataset:

  * Camphor
  * Neem
  * HariTaki
  * Sojina

---

## 📂 Project Structure

```
leaf-project/
│
├── backend/
│   ├── app.py
│   ├── database.db
│   ├── uploads/
│   ├── model/
│   │   ├── mobilenetv2_leaf.h5
│   │   └── labels.txt
│   └── utils/
│       └── predict.py
│
├── frontend/
│   ├── src/
│   │   ├── App.jsx
│   │   ├── index.css
│   │   ├── components/
│   │   │   ├── UploadBox.jsx
│   │   │   └── ResultCard.jsx
│   │   └── pages/
│   │       ├── Login.jsx
│   │       └── Signup.jsx
│
└── README.md
```

---

## ⚙️ Installation & Setup

### 🔹 1. Clone the Repository

```bash
git clone <your-repo-link>
cd leaf-project
```

---

### 🔹 2. Backend Setup

```bash
cd backend
pip install flask flask-cors flask-bcrypt tensorflow pillow numpy
```

Run backend:

```bash
python app.py
```

Backend runs on:

```
http://127.0.0.1:5000
```

---

### 🔹 3. Frontend Setup

```bash
cd frontend
npm install
npm run dev
```

Frontend runs on:

```
http://localhost:5173
```

---

## 📸 How It Works

1. User logs in / signs up
2. Uploads a leaf image
3. Image is sent to Flask backend
4. Model predicts:

   * Plant name
   * Disease (if any)
5. Backend fetches:

   * Symptoms
   * Remedies
     from SQLite database
6. Results displayed on UI

---

## 📊 Example Output

```
Plant: Neem
Detected Issue: Healthy Leaf
Confidence: 98%

Medicinal Uses:
- Disease: Skin Infection
  Symptoms: Itching, redness
  Remedies: Neem paste, neem oil
```

---

## ⚠️ Important Notes

* Model accuracy depends on dataset quality
* Only supports trained leaf categories
* Remedies are informational (not medical advice)

---

## 🔮 Future Improvements

* 🌍 Deploy using Render + Netlify
* 📱 Mobile responsive UI
* 📈 Show Top-3 predictions
* 🧾 Export results as PDF
* 🧠 Improve model accuracy with more data

---

## 👨‍💻 Author

**Fruity Sharma D**
Information Technology 
Chennai, India


---

## ⭐ If you like this project

Give it a ⭐ on GitHub and share it!

---
