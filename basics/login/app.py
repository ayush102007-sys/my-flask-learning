from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def login():
    return render_template("login.html")


@app.route("/submit", methods=["POST"])
def submit():
    email = request.form.get("email")
    password = request.form.get("password")

    if email == "abc@gmail.com" and password == "pass":
        return render_template("welcome.html")

    return "Invalid email or password", 401


if __name__ == "__main__":
    app.run(debug=True)
