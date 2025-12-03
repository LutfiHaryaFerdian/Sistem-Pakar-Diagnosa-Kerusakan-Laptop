from flask import Flask, render_template, request
from rules import SYMPTOMS, diagnose

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html", symptoms=SYMPTOMS)

@app.route("/diagnose", methods=["POST"])
def do_diagnose():
    symptoms = {}
    for code in request.form:
        value = request.form[code]
        if value != "0":
            symptoms[code] = float(value)

    result = diagnose(symptoms)
    return render_template("result.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
