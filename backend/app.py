from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_bcrypt import Bcrypt
from utils.predict import predict_leaf
import sqlite3
import os

# ------------------ APP SETUP ------------------
app = Flask(__name__)
CORS(app)
bcrypt = Bcrypt(app)

UPLOAD_FOLDER = "uploads"
DB_NAME = "database.db"

os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# ------------------ DATABASE UTILS ------------------
def get_db():
    return sqlite3.connect(DB_NAME)


def init_leaf_info():
    conn = get_db()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS leaf_medicinal_info (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            leaf_name TEXT,
            disease_name TEXT,
            symptoms TEXT,
            remedies TEXT
        )
    """)

    # Insert ONLY if table is empty
    cursor.execute("SELECT COUNT(*) FROM leaf_medicinal_info")
    count = cursor.fetchone()[0]

    if count == 0:
        data = [
            ("Neem", "Skin Infection",
             "Itching, redness, rashes",
             "Apply neem paste, neem oil, consult dermatologist"),

            ("Neem", "Diabetes Support",
             "High blood sugar, fatigue",
             "Neem leaf juice in morning under medical supervision"),

            ("HariTaki", "Digestive Disorder",
             "Constipation, bloating",
             "Haritaki powder with warm water"),

            ("Camphor", "Respiratory Issues",
             "Cough, congestion",
             "Steam inhalation, external application only"),

            ("Sojina", "Joint Pain",
             "Inflammation, stiffness",
             "Sojina leaf curry, warm compress")
        ]

        cursor.executemany("""
            INSERT INTO leaf_medicinal_info
            (leaf_name, disease_name, symptoms, remedies)
            VALUES (?, ?, ?, ?)
        """, data)

    conn.commit()
    conn.close()


def init_db():
    conn = get_db()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            email TEXT UNIQUE,
            password TEXT
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS predictions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            prediction TEXT,
            confidence REAL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)

    conn.commit()
    conn.close()
    init_leaf_info()


init_db()

# ------------------ AUTH ROUTES ------------------
@app.route("/auth/signup", methods=["POST"])
def signup():
    data = request.json
    email = data.get("email")
    password = data.get("password")

    if not email or not password:
        return jsonify({"error": "Missing fields"}), 400

    hashed_pw = bcrypt.generate_password_hash(password).decode("utf-8")

    conn = get_db()
    cursor = conn.cursor()

    try:
        cursor.execute(
            "INSERT INTO users (email, password) VALUES (?, ?)",
            (email, hashed_pw)
        )
        conn.commit()
    except sqlite3.IntegrityError:
        return jsonify({"error": "User already exists"}), 409
    finally:
        conn.close()

    return jsonify({"message": "Signup successful"}), 201


@app.route("/auth/login", methods=["POST"])
def login():
    data = request.json
    email = data.get("email")
    password = data.get("password")

    conn = get_db()
    cursor = conn.cursor()

    cursor.execute("SELECT id, password FROM users WHERE email=?", (email,))
    user = cursor.fetchone()
    conn.close()

    if user and bcrypt.check_password_hash(user[1], password):
        return jsonify({
            "message": "Login successful",
            "user_id": user[0]
        })

    return jsonify({"error": "Invalid credentials"}), 401

# ------------------ LEAF IDENTIFICATION ------------------
@app.route("/identify", methods=["POST"])
def identify():
    if "image" not in request.files:
        return jsonify({"error": "No image uploaded"}), 400

    file = request.files["image"]
    user_id = request.form.get("user_id")

    filepath = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(filepath)

    prediction, confidence, description = predict_leaf(filepath)

    # Example prediction: "Camphor__Shot_Hole"
    parts = prediction.split("__")

    leaf_name = parts[0]          # Camphor
    leaf_disease = parts[1] if len(parts) > 1 else "Healthy Leaf"

    # Extract leaf name
    leaf_name = prediction.split("/")[0]

    # Fetch medical info
    conn = get_db()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT disease_name, symptoms, remedies
        FROM leaf_medicinal_info
        WHERE leaf_name = ?
    """, (leaf_name,))

    medical_info = cursor.fetchall()

    # Save history
    if user_id:
        cursor.execute("""
            INSERT INTO predictions (user_id, prediction, confidence)
            VALUES (?, ?, ?)
        """, (user_id, prediction, confidence))
        conn.commit()

    conn.close()

    return jsonify({
        "prediction": prediction,
        "confidence": confidence,
        "leaf_name": leaf_name,
        "medical_uses": [
            {
                "disease": row[0],
                "symptoms": row[1],
                "remedies": row[2]
            }
            for row in medical_info
        ]
    })

# ------------------ HISTORY ------------------
@app.route("/history/<int:user_id>")
def history(user_id):
    conn = get_db()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT prediction, confidence, created_at
        FROM predictions
        WHERE user_id=?
        ORDER BY created_at DESC
    """, (user_id,))

    rows = cursor.fetchall()
    conn.close()

    return jsonify({
    "prediction": prediction,
    "confidence": confidence,
    "leaf_name": leaf_name,
    "leaf_disease": leaf_disease.replace("_", " "),
    "medical_uses": [
        {
            "disease": row[0],
            "symptoms": row[1],
            "remedies": row[2]
        }
        for row in medical_info
    ]
})

# ------------------ ROOT ------------------
@app.route("/")
def home():
    return "Leaf Identification Backend Running ✅"

# ------------------ RUN ------------------
if __name__ == "__main__":
    app.run(debug=True)