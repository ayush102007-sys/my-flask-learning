# Student Marks Calculator

A beginner-friendly web application built with **Python, Flask, HTML, and Jinja2** that allows students to enter their details, add multiple subjects dynamically, and prepare their marks for calculation.

## Features

- Enter the student's name.
- Choose the number of subjects.
- Dynamically generate subject-entry fields using Jinja2.
- Enter subject names, marks obtained, and maximum marks.
- Validate basic student details and subject count.
- Use HTML forms to send data to the Flask backend.
- Navigate between pages using Flask routes.

## Technologies Used

- **Python** — application logic
- **Flask** — web framework and routing
- **HTML5** — webpage structure and forms
- **Jinja2** — dynamic HTML rendering and loops

## Project Structure

```text
student-marks-calculator/
│
├── app.py
├── templates/
│   ├── base.html
│   └── calculator.html
│   ├── student_details.html
│   └── subjects.html
│
└── README.md
```

## Installation and Setup

### 1. Clone the repository

```bash
git clone YOUR_REPOSITORY_URL
```

Replace `YOUR_REPOSITORY_URL` with your GitHub repository URL.

### 2. Open the project directory

```bash
cd student-marks-calculator
```

### 3. Install Flask

```bash
python -m pip install flask
```

### 4. Run the application

```bash
python app.py
```

### 5. Open it in your browser

Visit:

```text
http://127.0.0.1:5000/
```

## How It Works

1. The user enters their name and the number of subjects.
2. Flask receives the submitted form data and checks the basic inputs.
3. Jinja2 generates the required number of subject-entry fields.
4. The user enters subject names and marks.
5. The submitted data can then be processed by Flask to calculate and display the student's results.

## What I Learned

Through this project, I practised:

- Creating routes in Flask.
- Handling HTML form submissions using `request`.
- Passing Python variables to HTML templates using `render_template()`.
- Using Jinja2 variables and `for` loops.
- Collecting repeated form fields.
- Validating user input.
- Calculating total marks and percentage.
- Displaying a subject-wise results table.
- Adding grade and pass/fail calculations.
- Connecting multiple HTML pages through a Flask application.

## Future Improvements

- Improve input validation and error messages.
- Add CSS for a responsive user interface.
- Store student results for future access.

## Learning Project

This project was created as part of my journey to learn **Python web development with Flask**. The goal was to understand the fundamentals of backend development, HTML forms, routing, and dynamic templates through hands-on practice.
