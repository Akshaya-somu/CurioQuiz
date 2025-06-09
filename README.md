🎓 CurioQuiz

CurioQuiz is an intelligent web application designed to generate and administer multiple-choice questions (MCQs) from input text using advanced Natural Language Processing (NLP) techniques. It enables users to create quizzes dynamically, attempt them, and track their performance over time.

📑 Table of Contents

* 📘 Project Overview
* ✨ Features
* 🛠️ Technologies Used
* ⚙️ Installation
* 🚀 Usage
* 🗂️ Project Structure
* 🤝 Contributing
* 📄 License
* 📬 Contact

📘 Project Overview
CurioQuiz aims to automate the generation of multiple-choice questions based on user-provided text inputs. This is particularly useful for educators and students to create quizzes for study or evaluation purposes quickly. The system supports user registration and login to personalize quiz data and tracks quiz history, allowing users to review past attempts.

The backend leverages Flask, a lightweight Python web framework, combined with NLP libraries like spaCy to parse and extract meaningful information from the text. The frontend uses Bootstrap and JavaScript to create a responsive and user-friendly interface.

✨ Features

* Automated MCQ Generation: Converts raw text input into meaningful multiple-choice questions
* User Authentication: Secure registration, login, and logout functionalities
* Quiz History Tracking: View past quizzes, filter by date or difficulty
* Responsive UI: Clean and intuitive interface powered by Bootstrap
* Difficulty Levels: Customize quizzes with easy, medium, and hard levels

🛠️ Technologies Used

* Backend: Python, Flask, spaCy
* Frontend: HTML5, CSS3, JavaScript, Bootstrap
* Database: SQLite (can be upgraded to PostgreSQL or MySQL)
* Version Control: Git, GitHub

⚙️ Installation

1. Clone the repository:
   git clone [https://github.com/Akshaya-somu/CurioQuiz.git](https://github.com/Akshaya-somu/CurioQuiz.git)
   cd CurioQuiz

2. Set up a virtual environment:
   python -m venv venv

3. Activate the environment

   * On Windows: venv\Scripts\activate
   * On macOS/Linux: source venv/bin/activate

4. Install dependencies:
   pip install -r requirements.txt

5. Run the application:
   flask run

6. Open in browser:
   [http://127.0.0.1:5000](http://127.0.0.1:5000)

🚀 Usage

* Register or login
* Paste input text to generate MCQs
* Attempt quizzes and submit answers
* View quiz history with filters

🗂️ Project Structure
CurioQuiz/
├── app.py – Main Flask app
├── requirements.txt – Python dependencies
├── templates/ – HTML pages
├── static/ – CSS, JS, image files
├── models.py – Database models
├── README.md – Project documentation
└── venv/ – Virtual environment (usually excluded from GitHub)

🤝 Contributing

1. Fork the repository
2. Create a new branch: git checkout -b feature-name
3. Commit your changes: git commit -m "Add feature"
4. Push your branch: git push origin feature-name
5. Open a pull request

📄 License
This project is licensed under the MIT License. You are free to use, modify, and distribute it.

📬 Contact
Akshaya Somu
Department of Computer Science and Engineering
Shri Vishnu Engineering College for Women, Bhimavaram
Email: [akshayasomu2005@gmail.com](mailto:akshayasomu2005@gmail.com)


