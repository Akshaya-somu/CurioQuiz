CurioQuiz

**CurioQuiz** is an intelligent web application designed to generate and administer multiple-choice questions (MCQs) from input text using advanced Natural Language Processing (NLP) techniques. It enables users to create quizzes dynamically, attempt them, and track their performance over time.


 Table of Contents

* [Project Overview](#project-overview)
* [Features](#features)
* [Technologies Used](#technologies-used)
* [Installation](#installation)
* [Usage](#usage)
* [Project Structure](#project-structure)
* [Contributing](#contributing)
* [License](#license)
* [Contact](#contact)

 Project Overview

CurioQuiz aims to automate the generation of multiple-choice questions based on user-provided text inputs. This is particularly useful for educators and students to create quizzes for study or evaluation purposes quickly. The system supports user registration and login to personalize quiz data and tracks quiz history, allowing users to review past attempts.

The backend leverages Flask, a lightweight Python web framework, combined with NLP libraries like spaCy to parse and extract meaningful information from the text. The frontend uses Bootstrap and JavaScript to create a responsive and user-friendly interface.


 Features

* **Automated MCQ Generation:** Converts raw text input into meaningful multiple-choice questions.
* **User Authentication:** Secure registration, login, and logout functionalities to personalize quiz experiences.
* **Quiz History Tracking:** Users can view their past quizzes and filter them by date or difficulty level.
* **Responsive UI:** Clean and intuitive interface powered by Bootstrap, optimized for all devices.
* **Difficulty Levels:** Supports categorizing generated questions by difficulty for better customization.



Technologies Used

* **Backend:** Python, Flask, spaCy
* **Frontend:** HTML5, CSS3, JavaScript, Bootstrap
* **Database:** SQLite (can be swapped with PostgreSQL or MySQL)
* **Version Control:** Git, GitHub



Installation

Follow these steps to set up and run CurioQuiz locally:

1. **Clone the repository:**

   
   git clone https://github.com/Akshaya-somu/CurioQuiz.git
   cd CurioQuiz
  

2. **Set up a virtual environment (recommended):**

   
   python -m venv venv
   

3. **Activate the virtual environment:**

   * On Windows:

     
     venv\Scripts\activate
     

   * On macOS/Linux:

     
     source venv/bin/activate
     

4. **Install required Python packages:**

   
   pip install -r requirements.txt
  

5. **Run the Flask application:**

  
   flask run
   

6. **Open your web browser and go to:**

   
   http://127.0.0.1:5000
   



 Usage

1. **Register or Login:** Create a new account or log into an existing one.
2. **Generate MCQs:** Input text in the provided form to generate multiple-choice questions automatically.
3. **Take Quizzes:** Attempt generated quizzes and submit answers.
4. **View Quiz History:** Access your quiz attempts, filter them by date or difficulty, and review performance.



Project Structure


CurioQuiz/
│
├── app.py               # Main Flask application
├── requirements.txt     # Python dependencies
├── templates/           # HTML templates (home, login, generate, history, etc.)
├── static/              # CSS, JS, and image assets
├── models.py            # Database models (if separated)
├── README.md            # Project documentation
└── venv/                # Virtual environment (optional, usually .gitignored)


Contributing:

Contributions are welcome! If you find bugs or want to add features:

1. Fork the repository
2. Create a new branch (`git checkout -b feature-name`)
3. Make your changes and commit (`git commit -m "Add new feature"`)
4. Push to your branch (`git push origin feature-name`)
5. Open a Pull Request

Please ensure code follows PEP8 style and is well-documented.



License:

This project is licensed under the [MIT License](LICENSE). You are free to use, modify, and distribute it.



Contact:

Akshaya Somu
Department of Computer Science and Engineering
Shri Vishnu Engineering College for Women, Bhimavaram
Email: [(mailto:akshayasomu2005@gmail.com)] 


