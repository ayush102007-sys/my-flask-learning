# Flask Quiz App

A beginner-friendly quiz application built with **Python and Flask**. Users can answer multiple-choice questions, submit their quiz, and review their results with question-by-question feedback.

## Features

- Multiple-choice quiz with radio-button options
- Displays the final score and percentage
- Shows each question with its available options
- Displays the user's answer alongside the correct answer
- Identifies correct, incorrect, and unanswered questions
- Retry option to attempt the quiz again
- Responsive styling with CSS using GitHub Copilot

## Tech Stack

- **Python** — quiz logic and score calculation
- **Flask** — web application and routing
- **HTML** — page structure and forms
- **CSS** — styling and responsive layout
- **Jinja2** — dynamic HTML rendering

## Project Structure

```text
flask-quiz-app/
├── app.py
├── templates/
    ├── base.html
    ├── quiz.html
    └── submit.html
├── requirements.txt
├── .gitignore
└── README.md
```

*The structure above is illustrative. Update it to match your actual files.*

## Getting Started

### 1. Clone the repository

```bash
git clone YOUR_REPOSITORY_URL
cd flask-quiz-app
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the application

```bash
flask run
```

Open the local address shown in your terminal, usually `http://127.0.0.1:5000/`.

## Screenshots

Add screenshots of your quiz page and results page here once you have saved them in the `screenshots/` directory.

## What I Learned

Through this project, I practised:

- Handling HTML form submissions in Flask
- Working with Python lists and dictionaries
- Retrieving submitted answers
- Comparing user responses with correct answers
- Calculating scores and percentages
- Passing data from Flask routes to Jinja2 templates
- Displaying dynamic results and answer feedback

## Future Improvements

- Add more questions and quiz categories
- Improve accessibility and user experience
- Add a timer and difficulty levels

## Author

**Ayush Das**

GitHub: [ayush102007-sys](https://github.com/ayush102007-sys)

---

This project was built as part of my hands-on learning journey with Python and Flask.