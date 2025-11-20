"use client";
import { useState } from "react";
import { questions } from "../../edusco/questions"; // JSON veya JS export ile

export default function Home() {
  const [answers, setAnswers] = useState({});
  const [results, setResults] = useState({});

  const handleChange = (id, value) => {
    setAnswers({ ...answers, [id]: value });
  };

  const handleSubmit = async (question) => {
    const res = await fetch("/api/evaluate", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ question_id: question.id, answer: answers[question.id] || "" }),
    });
    const data = await res.json();
    setResults({ ...results, [question.id]: data });
  };

  return (
    <div style={{ maxWidth: 800, margin: "auto", padding: 20 }}>
      <h1>Açık Uçlu Değerlendirme Sistemi</h1>
      {questions.map((q) => (
        <div key={q.id} style={{ marginBottom: 30 }}>
          <h3>{q.id}. {q.question}</h3>
          <textarea
            rows={3}
            style={{ width: "100%" }}
            onChange={(e) => handleChange(q.id, e.target.value)}
          />
          <button onClick={() => handleSubmit(q)}>Değerlendir</button>

          {results[q.id] && (
            <div style={{ marginTop: 10, border: "1px solid #ddd", padding: 10 }}>
              <p><b>Düzeltilmiş Cevap:</b> {results[q.id].duzeltmis}</p>
              <p><b>Skor:</b> {results[q.id].skor}</p>
              <p><b>Seviye:</b> {results[q.id].seviye} ({results[q.id].etiket})</p>
              <p><b>Ortak Kelimeler:</b> {results[q.id].ortak_kelimeler.join(", ")}</p>
              <p><b>Eksik Kavramlar:</b> {results[q.id].missing_keywords.join(", ") || "Tüm kritik kavramlar mevcut"}</p>
            </div>
          )}
        </div>
      ))}
    </div>
  );
}
