from flask import Flask, abort, render_template, request, session
from quiz import quiz_list
import database

app = Flask(__name__)
app.secret_key = "quiz-secret"

options = ["A","B","C","D"]

@app.route("/", methods= ["GET","POST"])
def base():
    if request.method == "POST":
        return render_template("base.html")

    return render_template("base.html")

@app.route("/home")
def home():
    return render_template("home.html")

@app.route("/register", methods= ["GET","POST"])
def register():
    page = ""
    if request.method == "POST":
        if request.form.get("login") == "Login →":
            page = "login"
        else:
            page = "signup"

        return render_template("register.html", page= page)

@app.route("/database", methods= ["POST"])
def db():
    if request.form.get("action") == "Login":
        logged_user = (request.form.get("logged")).strip()
        user_name = database.user_check(logged_user)
        if logged_user == user_name:
            session["username"] = logged_user
            return render_template("category.html", lst = quiz_list, name = logged_user)
        else:
            return render_template("success-error.html", account = "Not Found")
    else:
        username = (request.form.get("signed")).strip()
        database.add_user(username)
        return render_template("success-error.html", account = "Created")

@app.route("/quiz", methods=["POST"])
def quiz():
    topic = request.form.get("topics")
    if topic not in quiz_list:
        abort(400, description="Select a valid quiz topic.")

    session["topic"] = topic
    # Start a new quiz.
    session["idx"] = 0
    session["answers"] = {}

    return render_template(
        "quiz.html",
        idx=session["idx"],
        question=quiz_list[topic],
        options=options,
    )


@app.route("/submit", methods=["POST"])
def submit():
    # This route saves questions before the final one.
    topic = session.get("topic")
    if topic not in quiz_list:
        abort(400, description="Start a quiz before submitting answers.")

    idx = session.get("idx", 0)
    answer = request.form.get(f"q{idx + 1}")

    answers = dict(session.get("answers", {}))
    if answer is not None:
        answers[f"q{idx + 1}"] = answer
    session["answers"] = answers

    # Move to the next question.
    session["idx"] = idx + 1

    return render_template(
        "quiz.html",
        idx=session["idx"],
        question=quiz_list[topic],
        options=options,
    )

@app.route("/category", methods = ["POST"])
def topics():
    username = session.get("username")
    return render_template("category.html", lst = quiz_list,name = username )

@app.route("/results", methods=["POST"])
def result():
    topic = session.get("topic")
    if topic not in quiz_list:
        abort(400, description="Start a quiz before viewing results.")

    questions = quiz_list[topic]
    answers = dict(session.get("answers", {}))

    # The final question is submitted directly to /results.
    idx = session.get("idx", 0)
    final_answer = request.form.get(f"q{idx + 1}")
    if final_answer is not None:
        answers[f"q{idx + 1}"] = final_answer
    session["answers"] = answers

    # Score the answers, treating a missing answer as unanswered.
    score = 0
    user_ans = []

    for index, ques in enumerate(questions):
        answer = answers.get(f"q{index + 1}")
        user_ans.append(answer)

        if answer == ques["answer"]:
            score += 1

    percentage = (score / len(questions)) * 100
    username = session.get("username")
    database.add_score(username, score, f"{percentage:.0f}")

    return render_template(
        "result.html",
        name = username,
        score=score,
        percentage=percentage,
        questions=questions,
        user_ans=user_ans,
        enumerate=enumerate,
    )
