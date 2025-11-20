from flask import Flask, request, jsonify
from edusco import Edusco, EduscoModel
from edusco.questions import questions

app = Flask(__name__)
edusco = Edusco()

@app.route("/api/evaluate", methods=["POST"])
def evaluate():
    data = request.json
    question_id = data["question_id"]
    answer = data["answer"]

    # Soru modelini bul
    question = next((q for q in questions if q["id"] == question_id), None)
    if not question:
        return jsonify({"error": "Soru bulunamadı"}), 404

    model = EduscoModel(yanitlar=[question["ideal_answer"]])
    result = edusco.değerlendir(model, answer)
    missing_keywords = [k for k in question["keywords"] if k.lower() not in answer.lower()]

    return jsonify({
        "duzeltmis": result["duzeltmis"],
        "skor": result["skor"],
        "seviye": result["seviye"],
        "etiket": result["etiket"],
        "ortak_kelimeler": result["ortak_kelimeler"],
        "relations": result["relations"],
        "missing_keywords": missing_keywords
    })

if __name__ == "__main__":
    app.run()
