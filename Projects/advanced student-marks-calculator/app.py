from flask import Flask, render_template, request

app = Flask(__name__)
app.secret_key = "my-secret-key"


@app.after_request
def add_calculator_styles(response):
    if response.mimetype == "text/html":
        styles = """
<style>
    * { box-sizing: border-box; }
    body { max-width: 820px; margin: 36px auto; padding: 0 20px;
           background: #f3f6fb; color: #243247; font: 16px/1.5 Arial, sans-serif; }
    nav ul { display: flex; gap: 20px; padding: 0; list-style: none; }
    a { color: #2563a6; text-decoration: none; }
    a:hover { text-decoration: underline; }
    main { margin: 20px 0; padding: 26px; background: #fff;
           border: 1px solid #dce4ef; border-radius: 10px; }
    h2, legend { color: #1d3557; }
    label { display: inline-block; margin: 8px 0 4px; font-weight: 600; }
    input[type="text"], input[type="number"] { display: block; width: 100%; max-width: 420px;
        padding: 10px 12px; border: 1px solid #bdc9d8; border-radius: 6px; font: inherit; }
    input:focus { outline: 2px solid #8bb8ed; border-color: #4385cf; }
    input[type="submit"], button { margin-top: 10px; padding: 10px 16px; border: 0;
        border-radius: 6px; background: #2563a6; color: #fff; font: inherit; cursor: pointer; }
    input[type="submit"]:hover, button:hover { background: #194d83; }
    fieldset { margin: 16px 0; padding: 16px; border: 1px solid #d2dce8; border-radius: 8px; }
    table { width: 100%; margin: 12px 0; border-collapse: collapse; }
    th, td { padding: 10px; border: 1px solid #d2dce8; text-align: left; }
    th { background: #edf3fa; }
    @media (max-width: 520px) { body { margin: 18px auto; } main { padding: 18px; } }
</style>
"""
        html = response.get_data(as_text=True)
        if "</head>" in html:
            response.set_data(html.replace("</head>", styles + "</head>", 1))
    return response


@app.route("/")
def home():
    return render_template("base.html")


@app.route("/about")
def about():
    return "Calculate your marks easily using my Calculator :)"

@app.route("/student", methods=["POST"])
def student():
    return render_template("students_details.html")


@app.route("/subjects", methods=["POST"])
def subjects():
    name = request.form.get("name")
    subject_count = request.form.get("subject_count", type=int)

    if not name or not subject_count or not 1 <= subject_count <= 20:
        return "Please enter a valid name and subject count.", 400

    return render_template("subjects.html", name= name, subject_count= subject_count)

@app.route("/results", methods= ["POST"])
def results():
    subject_name = request.form.getlist("subject_name")
    marks_obtained = request.form.getlist("marks", type=int)
    full_marks = request.form.getlist("maximum_marks", type=int)
    total_marks = sum(request.form.getlist("marks", type=int))
    maximum_marks = sum(request.form.getlist("maximum_marks", type=int))
    percentage = (total_marks/maximum_marks) * 100

    grade_sys = {
        "Excellent": "A+",
        "Very Good": "A",
        "Good": "B",
        "Satisfactory": "C",
        "Disqualified": "D"
    }

    if total_marks<= maximum_marks:
        return render_template("calculator.html", total_marks= total_marks, percentage= percentage,
                               subject_name = subject_name, enumerate= enumerate,
                               marks_obtained= marks_obtained, full_marks= full_marks,
                               grade_sys = grade_sys)
    
    return "You provided wrong marks! Check again."
    