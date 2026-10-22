from flask import Flask, render_template, request, session

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
},
{
    "question": "Which planet is known as the Red Planet?",
    "options": ["Venus", "Mars", "Jupiter", "Mercury"],
    "answer": "B"
},
{
    "question": "What is the capital of Japan?",
    "options": ["Seoul", "Beijing", "Tokyo", "Bangkok"],
    "answer": "C"
},
{
    "question": "Which is the largest ocean on Earth?",
    "options": ["Atlantic Ocean", "Indian Ocean", "Arctic Ocean", "Pacific Ocean"],
    "answer": "D"
},
{
    "question": "What is the chemical symbol for gold?",
    "options": ["Ag", "Au", "Fe", "Go"],
    "answer": "B"
},
{
    "question": "Who wrote the play Romeo and Juliet?",
    "options": ["Charles Dickens", "William Shakespeare", "Jane Austen", "Mark Twain"],
    "answer": "B"
},
{
    "question": "How many sides does a hexagon have?",
    "options": ["Five", "Six", "Seven", "Eight"],
    "answer": "B"
},
{
    "question": "Which gas do plants absorb during photosynthesis?",
    "options": ["Oxygen", "Nitrogen", "Carbon dioxide", "Hydrogen"],
    "answer": "C"
},
{
    "question": "What is the largest mammal in the world?",
    "options": ["African elephant", "Blue whale", "Giraffe", "Hippopotamus"],
    "answer": "B"
},
{
    "question": "Which country is home to the Great Pyramids of Giza?",
    "options": ["Greece", "Mexico", "Egypt", "India"],
    "answer": "C"
},
{
    "question": "What is the square root of 144?",
    "options": ["10", "11", "12", "14"],
    "answer": "C"
},
{
    "question": "Which organ pumps blood throughout the human body?",
    "options": ["Lungs", "Brain", "Liver", "Heart"],
    "answer": "D"
},
{
    "question": "Which programming language is commonly used with the Flask web framework?",
    "options": ["Java", "Python", "C++", "PHP"],
    "answer": "B"
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
            
        