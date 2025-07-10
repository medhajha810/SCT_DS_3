# 🐾 Dogs vs Cats Classifier - SkillCraft ML Internship (Task 3)

This is Task 3 of my Machine Learning Internship at **SkillCraft Technology**. The goal was to implement a Support Vector Machine (SVM) model to classify images of **dogs and cats**, and deploy it using a responsive **Flask web app** with a beautiful frontend.

---

## 🎯 Objective

- ✅ Build a machine learning model (SVM) to classify images as either **Dog 🐶** or **Cat 🐱**
- ✅ Use [Kaggle's Dogs vs Cats dataset](https://www.kaggle.com/c/dogs-vs-cats/data)
- ✅ Create an interactive **frontend using HTML/CSS**
- ✅ Connect everything using a **Flask API backend**
- ✅ Add styling, animations, and responsiveness

---

## 🧠 ML Workflow

- 📦 **Dataset**: 5000 grayscale images (`64x64`) from Kaggle
- ⚙️ **Preprocessing**: Grayscale → Resize → Flatten → Normalize
- 🧪 **Model**: `SVC(kernel='linear')` using Scikit-learn
- 📊 **Accuracy**: ~53% on test data
- 💾 **Saved model**: `svm_dogs_vs_cats.pkl` using `joblib`

---

## 🌐 Web App Features

- 📤 Upload an image of a cat or dog
- 🧠 Model predicts and returns: **Dog 🐶** or **Cat 🐱**
- 🖼 Uploaded image is previewed below the prediction
- 🎨 Clean UI with glowing text, animated background, and responsive layout

---

## 📁 Project Structure

dogs-vs-cats-app/
├── app.py # Flask backend
├── svm_dogs_vs_cats.pkl # Trained SVM model
├── static/
│ └── style.css # CSS with animations and layout
├── templates/
│ └── index.html # Web frontend (upload form + prediction UI)
├── README.md



---

## 🚀 How to Run Locally

### Step 1: Clone the Repository
git clone https://github.com/medhajha810/SCT_DS_3.git
cd SCT_DS_3

### Step 2: Install Dependencies
pip install flask joblib numpy opencv-python

### Step 3: Run the App
python app.py

### Step 4: Open in Browser
http://127.0.0.1:5000/


📦 Files to Include
     File	                      Description
svm_dogs_vs_cats.pkl	      Trained SVM model
X_test.npy & y_test.npy	    for testing or future evaluation


👩‍💻 Developed by
Medha Jha
🚀 Machine Learning Intern @ SkillCraft Technology
🔗 [LinkedIn](https://www.linkedin.com/in/medha-jha810/)
🌐 [GitHub](https://github.com/medhajha810/)

🙏 Acknowledgements
Kaggle: Dogs vs Cats Dataset

Scikit-learn

Flask Web Framework

Internship guided by SkillCraft Technology
