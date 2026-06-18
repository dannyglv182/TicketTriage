import { useState } from "react";

export default function App() {
  const [ticket, setTicket] = useState("");
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);

  const handleSubmit = async () => {
    setLoading(true);

    try {
      const response = await fetch("http://localhost:8000/analyze-ticket", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        // Converts the user's ticket description into a JSON string
        body: JSON.stringify({
          description: ticket,
        }),
      });
      // Stores the ticket analysis and changes the state of result
      const data = await response.json();
      setResult(data);
      console.log(data);
    } catch (err) {
      console.error("Error:", err);
    }

    setLoading(false);
  };

  return (
    <div style={{ padding: "20px" }}>
      <h1>Ticket Triage</h1>

      <textarea
        rows={6}
        cols={60}
        placeholder="Enter support ticket..."
        value={ticket}
        onChange={(e) => setTicket(e.target.value)}
      />

      <br />

      <button onClick={handleSubmit} disabled={loading || !ticket}>
        {loading ? "Analyzing..." : "Analyze Ticket"}
      </button>

      {result && (
        <div style={{ marginTop: "20px" }}>
          <h3>Result</h3>
          <p><b>Category:</b> {result.category}</p>
          <p><b>Priority:</b> {result.priority}</p>
          <p><b>Team:</b> {result.team}</p>
          <p><b>Summary:</b> {result.summary}</p>
        </div>
      )}
    </div>
  );
}
