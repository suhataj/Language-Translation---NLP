from flask import Flask , render_template , request
from textblob import TextBlob 

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/data" , methods = ["post"])
def data():
    t = request.form.get("detect")
    t_from = request.form.get("languages")
    t_to = request.form.get("translate")
    
    a = TextBlob(t)
    data = a.translate(from_lang=t_from , to=t_to)

    return render_template("home.html" , data = data)

app.run()