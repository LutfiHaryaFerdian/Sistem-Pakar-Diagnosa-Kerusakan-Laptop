from flask import Flask, render_template, request
from rules import SYMPTOMS, diagnose
from rules import SYMPTOMS, FAULTS

app = Flask(__name__)

@app.route("/gejala")
def gejala_page():
    return render_template("gejala.html", symptoms=SYMPTOMS)

@app.route("/kerusakan")
def kerusakan_page():
    return render_template("kerusakan.html", faults=FAULTS)

@app.route("/tentang")
def tentang_page():
    return render_template("tentang.html")

@app.route("/")
def index():
    return render_template("index.html", symptoms=SYMPTOMS)

@app.route("/diagnose-start")
def diagnose_start():
    return render_template("form.html", symptoms=SYMPTOMS)

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
