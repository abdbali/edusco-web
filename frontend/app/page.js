import { useState } from "react";
import QuestionForm from "./components/QuestionForm";
import questions from "../../edusco/questions";

export default function Home() {
  const [currentIndex, setCurrentIndex] = useState(0);
  const [results, setResults] = useState([]);

  const handleNext = (res) => {
    setResults([...results, res]);
    if (currentIndex + 1 < questions.length) {
      setCurrentIndex(currentIndex + 1);
    } else {
      alert("Tüm sorular tamamlandı!");
      console.log(results);
    }
  };

  return (
    <div style={{ padding: 20, fontFamily: "Arial" }}>
      <h1>Açık Uçlu Değerlendirme Sistemi</h1>
      <QuestionForm
        question={questions[currentIndex]}
        onNext={handleNext}
      />
    </div>
  );
}
