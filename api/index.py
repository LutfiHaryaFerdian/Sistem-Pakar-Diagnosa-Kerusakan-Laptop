from flask import Flask, render_template, request
from rules import SYMPTOMS, FAULTS, SYMPTOM_CATEGORIES, diagnose
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

app = Flask(
    __name__,
    template_folder=os.path.join(BASE_DIR, "templates"),
    static_folder=os.path.join(BASE_DIR, "static")
)


# Helper function untuk mendapatkan kategori gejala
def get_symptom_category(symptom_code):
    for category, codes in SYMPTOM_CATEGORIES.items():
        if symptom_code in codes:
            return category
    return "Other"


@app.route("/")
def index():
    return render_template("index.html", symptoms=SYMPTOMS)


@app.route("/gejala")
def gejala_page():
    return render_template("gejala.html", symptoms=SYMPTOMS)


@app.route("/kerusakan")
def kerusakan_page():
    return render_template("kerusakan.html", faults=FAULTS)


@app.route("/tentang")
def tentang_page():
    return render_template("tentang.html")


@app.route("/diagnose-start")
def diagnose_start():
    symptom_categories = {
        code: get_symptom_category(code)
        for code in SYMPTOMS.keys()
    }

    return render_template(
        "form.html",
        symptoms=SYMPTOMS,
        symptom_categories=symptom_categories
    )


@app.route("/diagnose", methods=["POST"])
def do_diagnose():
    symptoms = {}

    for code, value in request.form.items():
        if value != "0":
            symptoms[code] = float(value)

    result = diagnose(symptoms)

    if result is None:
        return render_template(
            "error.html",
            message="Tidak dapat mendiagnosa. Silakan pilih minimal satu gejala dengan intensitas."
        )

    # ambil top 3 hasil
    top3_list = [
        {
            "fault_code": item["fault_code"],
            "fault_name": item["fault_name"],
            "cf_percent": item["cf_percent"],
            "details_count": len(item["details"])
        }
        for item in result["top_3"]
    ]

    import json

    return render_template(
        "result.html",
        result=result,
        top3_json=json.dumps(top3_list),
        enumerate=enumerate
    )


# hanya jalan di lokal, diabaikan oleh Vercel
if __name__ == "__main__":
    app.run(debug=True)
