from flask import Flask, render_template, request, session
from quiz import quiz_list

app = Flask(__name__)
app.secret_key = "quiz-secret"

quiz_database = []
options = ["A","B","C","D"]

@app.route("/")
def home():
    return render_template("base.html")

@app.route("/quiz", methods=["POST"])
def quiz():
    topic = request.form.get("topics")
    for x in (quiz_list[f"{topic}"]):
        quiz_database.append(x)
    # Start a new quiz.
    session["idx"] = 0
    session["answers"] = {}

    return render_template(
        "quiz.html",
        idx=session["idx"],
        question=quiz_database,
        options=options,
    )


@app.route("/submit", methods=["POST"])
def submit():
    # This route saves questions before the final one.
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
        question=quiz_database,
        options=options,
    )

@app.route("/category", methods = ["POST"])
def topics():
    return render_template("category.html", lst = quiz_list)

@app.route("/results", methods=["POST"])
def result():
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

    for index, ques in enumerate(quiz_database):
        answer = answers.get(f"q{index + 1}")
        user_ans.append(answer)

        if answer == ques["answer"]:
            score += 1

    percentage = (score / len(quiz_database)) * 100

    return render_template(
        "result.html",
        score=score,
        percentage=percentage,
        questions=quiz_database,
        user_ans=user_ans,
        enumerate=enumerate,
    )
