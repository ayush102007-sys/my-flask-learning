from flask import Flask, abort, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = "my-secret-key"

@app.route("/")
def home():
    return render_template("base.html")

@app.route("/marks")
def marks():
    return render_template("marks.html")

@app.route("/calculate", methods = ["POST"])
def calculator():
    maths = request.form.get("maths", type=int)
    phy = request.form.get("phy", type=int)
    cs = request.form.get("cs", type=int)

    marks = (maths, phy, cs)
    if any(mark is None for mark in marks):
        flash("Enter valid obtained marks!")
        return redirect(url_for("marks"))

    result = sum(marks)
    if any(mark > 100 for mark in marks) or result > 300:
        flash("Each subject mark must be 100 or less, and the total must be 300 or less!")
        return redirect(url_for("marks"))

    percentage = (result / 300) * 100
    return render_template("calculate.html", total_marks=result, percentage=percentage)
