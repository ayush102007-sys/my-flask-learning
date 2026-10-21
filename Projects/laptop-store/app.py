from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("base.html")

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/submit", methods=["POST"])
def submit():
    username = request.form.get("username")
    password = request.form.get("password")

    if not username or not password:
        return "Missing username or password", 400

    if username == "admin" and password == "123":
        return render_template("submit.html", username=username)

    return "Invalid username or password", 401
    
@app.route("/products")
def pdts():
    return render_template("products.html")

@app.route("/cart", methods = ["POST"])
def cart():
    return render_template("cart.html")

@app.route("/about")
def about():
    return render_template("about.html")

if __name__ == "__main__":
    app.run(debug=True)