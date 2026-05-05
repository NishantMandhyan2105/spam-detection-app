# spam-detection-app
Spam Detection Web App using Machine Learning (KNN + TF-IDF) with FastAPI backend and simple UI
# 🚀 Spam Detection App

A machine learning web application that classifies messages as **Spam** or **Not Spam** using KNN and TF-IDF.

---

## 🧠 Features

* Detect spam messages instantly
* Machine Learning model (KNN)
* Text preprocessing (TF-IDF)
* FastAPI backend
* Simple and clean UI

---

## 🛠️ Tech Stack

* Python
* FastAPI
* Scikit-learn
* Pandas
* Jinja2 (HTML templates)

---

## 📂 Project Structure

```
spammessage/
│── src/
│   └── app.py
│── templates/
│   └── index.html
│── model/
│── .gitignore
│── README.md
```

---

## ⚙️ How to Run Locally

1. Clone the repository

```
git clone https://github.com/YOUR_USERNAME/spam-detection-app.git
cd spam-detection-app
```

2. Create virtual environment

```
python -m venv venv
venv\Scripts\activate
```

3. Install dependencies

```
pip install -r requirements.txt
```

4. Run the app

```
python -m uvicorn src.app:app --reload
```

5. Open in browser

```
http://127.0.0.1:8000/
```

---

## 📸 Demo

Enter a message → Get prediction → Spam / Not Spam

---

## 📌 Future Improvements

* Better UI (CSS / React)
* Deploy on cloud
* Use advanced models (Logistic Regression / Deep Learning)

---

## 👨‍💻 Author

Nishant Mandhyan
