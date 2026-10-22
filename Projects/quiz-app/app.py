from flask import Flask, render_template, request

app = Flask(__name__)

quiz_database = [
    {
    "question": "What is the capital of India?",
    "options": ["Mumbai", "New Delhi", "Kolkata", "Chennai"],
    "answer": "B"
},
{
    "question": "How many days are there in a leap year?",
    "options": ["364", "370", "366", "365"],
    "answer": "C"
},
{
    "question": "On which day we celebrate Independence Day?",
    "options": ["2 October", "26 January", "25 December", "15 August"],
    "answer": "D"
}
]
options = ["A","B","C","D"]

@app.route("/")
def home():
    return render_template("base.html")

@app.route("/quiz", methods = ["POST"])
def quiz():
    return render_template("quiz.html", question= quiz_database,options=options, enumerate= enumerate)

@app.route("/submit", methods = ["POST"])
def submit():
    score = 0
    user_ans = []
    for index, ques in enumerate(quiz_database):
        ans = request.form.get(f"q{index+1}")
        if ans == ques["answer"]:
            score += 1
            user_ans.append(ans)
        else:
            user_ans.append(ans)
    
    percentage = (score/len(quiz_database)) * 100
    return render_template("submit.html", score= score, percentage= percentage,
                           questions = quiz_database, enumerate= enumerate, user_ans= user_ans)
            
        