import "./App.css";
import { useEffect, useState } from "react";

function App() {
  const [age, setAge] = useState(null);
  const [bmi, setBmi] = useState(null);
  const [numChildren, setNumChildren] = useState(null);
  const [prediction, setPrediction] = useState(null);
  const [people, setPeople] = useState([]);

  const peopleData = [
    { name: "John", age: 25, bmi: 22, children: 0 },
    { name: "Jane", age: 30, bmi: 25, children: 1 },
    { name: "Jim", age: 35, bmi: 30, children: 2 },
  ];

  useEffect(() => {
    const getQuotes = async () => {
      const newPeople = await Promise.all(
        peopleData.map(async (person) => {
          const quote = await getInsuranceQuoteTable(
            person.age,
            person.bmi,
            person.children
          );
          return { ...person, quote: quote };
        })
      );
      setPeople(newPeople);
    };

    getQuotes();
  }, []);

  const getInsuranceQuote = async () => {
    const FLASK_API_URL = "http://localhost:8000/charges_api";
    const DJANGO_API_URL = "http://localhost:8000/charges";
    const ASP_API_URL = "http://localhost:5109/charges_api";

    const response = await fetch(FLASK_API_URL, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ age: age, bmi: bmi, children: numChildren }),
    });
    const data = await response.json();
    // console.log(data);
    setPrediction(data.prediction);
  };

  const getInsuranceQuoteTable = async (age, bmi, children) => {
    const FLASK_API_URL = "http://localhost:8000/charges_api";
    const DJANGO_API_URL = "http://localhost:8000/charges";
    const ASP_API_URL = "http://localhost:5109/charges_api";

    const response = await fetch(FLASK_API_URL, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ age: age, bmi: bmi, children: children }),
    });
    const data = await response.json();
    // console.log(data);
    return data.prediction.toFixed(2);
  };

  return (
    <div className="App">
      <h1>Insurance Quote</h1>
      <label>Age:</label>
      <input type="text" onChange={(e) => setAge(e.target.value)} />
      <br />
      <br />
      <label>BMI:</label>
      <input type="text" onChange={(e) => setBmi(e.target.value)} />
      <br />
      <br />
      <label>Number of children:</label>
      <input type="text" onChange={(e) => setNumChildren(e.target.value)} />
      <br />
      <br />
      <button onClick={getInsuranceQuote}>Get Quote</button>
      <h2>Quote:{prediction}</h2>

      <br />
      <h2>People</h2>
      <table style={{ marginRight: "auto", marginLeft: "auto" }}>
        <thead>
          <tr>
            <th>Name</th>
            <th>Age</th>
            <th>BMI</th>
            <th>Children</th>
            <th>Quote</th>
          </tr>
        </thead>
        <tbody>
          {people.map((person, index) => (
            <tr key={index}>
              <td>{person.name}</td>
              <td>{person.age}</td>
              <td>{person.bmi}</td>
              <td>{person.children}</td>
              <td>{person.quote}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

export default App;
