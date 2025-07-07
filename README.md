---

# 🎓 CurioQuiz

Live Deployment:
🌐 [https://curioquiz.onrender.com](https://curioquiz.onrender.com)

CurioQuiz is an intelligent web application that automatically generates multiple-choice questions (MCQs) from input text using advanced Natural Language Processing (NLP). It enables users to dynamically create, attempt, and track quizzes—making it ideal for both students and educators.

---

## 📑 Table of Contents

* [📘 Project Overview](#-project-overview)
* [✨ Features](#-features)
* [🛠️ Technologies Used](#-technologies-used)
* [⚙️ Installation](#-installation)
* [🚀 Usage](#-usage)
* [🗂️ Project Structure](#-project-structure)
* [🤝 Contributing](#-contributing)
* [📄 License](#-license)
* [📬 Contact](#-contact)

---

## 📘 Project Overview

CurioQuiz aims to automate the creation of MCQs from raw input text using NLP techniques. It provides user authentication, tracks quiz history, and offers a smooth and responsive experience for quiz generation, attempting, and review.

* Designed for educators, students, and self-learners
* Backend powered by **Flask** and **spaCy**
* Frontend built with **Bootstrap** and **JavaScript**
* Persistent data tracking through user authentication and history logs

---

## ✨ Features

✅ Automated MCQ Generation
→ Paste text and instantly receive intelligent multiple-choice questions.

✅ User Authentication
→ Secure registration, login, and logout functionalities.

✅ Quiz History Tracking
→ Review previous attempts and filter by date or difficulty level.

✅ Responsive UI
→ Built using Bootstrap for seamless experience across devices.

✅ Difficulty Levels
→ Option to generate quizzes with easy, medium, or hard-level questions.

---

## 🛠️ Technologies Used

Backend:

* Python
* Flask
* spaCy (NLP)

**Frontend:**

* HTML5
* CSS3
* JavaScript
* Bootstrap

**Database:**

* SQLite (Upgradeable to PostgreSQL/MySQL)

**Version Control:**

* Git
* GitHub

---

## ⚙️ Installation

1. **Clone the repository**

   ```bash
   git clone https://github.com/Akshaya-somu/CurioQuiz.git
   cd CurioQuiz
   ```

2. **Set up a virtual environment**

   ```bash
   python -m venv venv
   ```

3. **Activate the environment**

   * Windows:
     `venv\Scripts\activate`
   * macOS/Linux:
     `source venv/bin/activate`

4. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

5. **Run the application**

   ```bash
   flask run
   ```

6. **Visit the app**
   Open your browser and go to:
   [http://127.0.0.1:5000](http://127.0.0.1:5000)

---

## 🚀 Usage

1. Register or log in
2. Paste your text to generate MCQs
3. Attempt the quiz and submit your answers
4. View and filter your quiz history

---

🗂️ Project Structure
CurioQuiz/
├── app.py – Main Flask app
├── requirements.txt – Python dependencies
├── templates/ – HTML pages
├── static/ – CSS, JS, image files
├── models.py – Database models
├── README.md – Project documentation
└── venv/ – Virtual environment (usually excluded from GitHub)

---

## 🤝 Contributing

We welcome contributions! 🚀

1. Fork the repository
2. Create a new branch

   ```bash
   git checkout -b feature-name
   ```
3. Make your changes
4. Commit changes

   ```bash
   git commit -m "Add feature"
   ```
5. Push to your fork

   ```bash
   git push origin feature-name
   ```
6. Open a Pull Request

---

## 📄 License

This project is licensed under the **MIT License**.
Feel free to use, modify, and distribute it.

---

## 📬 Contact

**Akshaya Somu**
Department of Computer Science and Engineering
Shri Vishnu Engineering College for Women, Bhimavaram
📧 Email: [akshayasomu2005@gmail.com](mailto:akshayasomu2005@gmail.com)

---





