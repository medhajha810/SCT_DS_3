from flask import Flask, request, render_template, jsonify
import numpy as np
import joblib
import cv2
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)

# Load model
model = joblib.load("svm_dogs_vs_cats.pkl")

IMG_SIZE = 64

@app.route("/", methods=["GET", "POST"])
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    if 'image' not in request.files:
        return jsonify({"error": "No image uploaded"}), 400

    file = request.files['image']
    filename = secure_filename(file.filename)
    filepath = os.path.join("static", filename)
    file.save(filepath)

    # Preprocess the image
    img = cv2.imread(filepath, cv2.IMREAD_GRAYSCALE)
    img = cv2.resize(img, (IMG_SIZE, IMG_SIZE))
    img_flat = img.flatten().reshape(1, -1) / 255.0

    pred = model.predict(img_flat)[0]
    label = "Dog 🐶" if pred == 0 else "Cat 🐱"

    return render_template("index.html", prediction=label, image_path=filepath)

if __name__ == "__main__":
    app.run(debug=True)
