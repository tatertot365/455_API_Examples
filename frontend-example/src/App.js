import "./App.css";
import { useState } from "react";

function App() {
  const [age, setAge] = useState(null);
  const [bmi, setBmi] = useState(null);
  const [numChildren, setNumChildren] = useState(null);
  const [prediction, setPrediction] = useState(null);

  const getInsuranceQuote = async () => {
    const response = await fetch("http://localhost:5109/charges_api", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ age: age, bmi: bmi, children: numChildren }),
    });
    const data = await response.json();
    console.log(data);
    setPrediction(data.prediction);
  };

  return (
    <div className="App">
      <h1>Insurance Quote</h1>
      <label>Age:</label>
      <input type="text" onChange={(e) => setAge(e.target.value)} />
      <label>BMI:</label>
      <input type="text" onChange={(e) => setBmi(e.target.value)} />
      <label>Number of children:</label>
      <input type="text" onChange={(e) => setNumChildren(e.target.value)} />
      <button onClick={getInsuranceQuote}>Get Quote</button>
      <h2>Quote:{prediction}</h2>
    </div>
  );
}

export default App;
