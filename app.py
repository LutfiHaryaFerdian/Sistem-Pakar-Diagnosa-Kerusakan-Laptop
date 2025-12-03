from flask import Flask, render_template, request
from rules import SYMPTOMS, FAULTS, SYMPTOM_CATEGORIES, diagnose

app = Flask(__name__)

# Helper function untuk mendapatkan kategori gejala
def get_symptom_category(symptom_code):
    for category, codes in SYMPTOM_CATEGORIES.items():
        if symptom_code in codes:
            return category
    return "Other"

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
    # Buat dictionary kategori untuk setiap gejala
    symptom_categories = {}
    for code in SYMPTOMS.keys():
        symptom_categories[code] = get_symptom_category(code)
    
    return render_template(
        "form.html",
        symptoms=SYMPTOMS,
        symptom_categories=symptom_categories
    )

@app.route("/diagnose", methods=["POST"])
def do_diagnose():
    symptoms = {}
    for code in request.form:
        value = request.form[code]
        if value != "0":
            symptoms[code] = float(value)

    result = diagnose(symptoms)

    # Jika tidak ada hasil
    if result is None:
        return render_template(
            "error.html",
            message="Tidak dapat mendiagnosa. Silakan pilih minimal satu gejala dengan intensitas."
        )

    # ---- PERBAIKAN UTAMA: gunakan result["top_3"] ----
    top3_list = []
    for item in result["top_3"]:
        top3_list.append({
            "fault_code": item["fault_code"],
            "fault_name": item["fault_name"],
            "cf_percent": item["cf_percent"],
            "details_count": len(item["details"])
        })

    import json

    return render_template(
        "result.html",
        result=result,
        top3_json=json.dumps(top3_list),
        enumerate=enumerate
    )


if __name__ == "__main__":
    app.run(debug=True)
