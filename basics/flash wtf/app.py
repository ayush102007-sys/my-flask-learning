from flask import Flask, render_template, redirect, url_for, request,flash
from forms import RegistrationForm

app = Flask(__name__)
app.secret_key = "my-secret-key"

@app.route("/", methods = ["GET","POST"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():  # Returns True when submitted form passes all validators.
        name = form.name.data   # access name from the reg form
        email = form.email.data
        flash(f"Welcome {name}, You registerd successfully!", "success")
        return redirect(url_for("success"))
    return render_template("register.html", form= form)

@app.route("/success")
def success():
    return render_template("success.html")
