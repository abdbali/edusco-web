import { useState } from "react";

export default function QuestionForm({ question, onNext }) {
  const [answer, setAnswer] = useState("");
  const [result, setResult] = useState(null);

  const submitAnswer = async () => {
    const res = await fetch("/api/evaluate", {
      method: "POST",
      body: JSON.stringify({ qid: question.id, answer }),
      headers: { "Content-Type": "application/json" },
    });
    const data = await res.json();
    setResult(data);
    onNext(data);
  };

  return (
    <div style={{ marginTop: 20 }}>
      <h2>{question.question}</h2>
      <textarea
        value={answer}
        onChange={(e) => setAnswer(e.target.value)}
        rows={4}
        cols={50}
      />
      <br />
      <button onClick={submitAnswer} style={{ marginTop: 10 }}>
        Cevabı Gönder
      </button>

      {result && (
        <div style={{ marginTop: 20, border: "1px solid #ccc", padding: 10 }}>
          <p><strong>Düzeltilmiş:</strong> {result.duzeltmis}</p>
          <p><strong>Skor:</strong> {result.skor}</p>
          <p><strong>Seviye:</strong> {result.seviye} ({result.etiket})</p>
          <p><strong>Ortak Kelimeler:</strong> {result.ortak_kelimeler.join(", ")}</p>
          <p><strong>Eksik Kavramlar:</strong> {result.missing_keywords.join(", ")}</p>
        </div>
      )}
    </div>
  );
}
