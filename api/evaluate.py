from edusco import Edusco, EduscoModel
from edusco.questions import questions
import json

edusco = Edusco()

def handler(request):
    try:
        body = json.loads(request['body'])
        qid = body.get("qid")
        answer = body.get("answer", "")
        
        question = next((q for q in questions if q["id"] == qid), None)
        if not question:
            return {"statusCode": 404, "body": json.dumps({"error": "Soru bulunamadı."})}

        model = EduscoModel(yanitlar=[question["ideal_answer"]])
        result = edusco.değerlendir(model, answer)

        missing_keywords = [k for k in question["keywords"] if k.lower() not in answer.lower()]
        result.update({"missing_keywords": missing_keywords})

        return {"statusCode": 200, "body": json.dumps(result, ensure_ascii=False)}
    except Exception as e:
        return {"statusCode": 500, "body": json.dumps({"error": str(e)})}
