import React, { useState } from "react";
import axios from "axios";
import "./App.css";

function App() {
  const [pdfFile, setPdfFile] = useState(null);
  const [query, setQuery] = useState("");
  const [answer, setAnswer] = useState("");
  const [chunks, setChunks] = useState([]);
  const [loading, setLoading] = useState(false);

  const API_BASE = process.env.REACT_APP_BACKEND_URL || "http://localhost:8000";


  const handleFileChange = (e) => {
    setPdfFile(e.target.files[0]);
  };

  const handleQueryChange = (e) => {
    setQuery(e.target.value);
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (!pdfFile || !query) {
      alert("Please upload a PDF and enter your query.");
      return;
    }

    const formData = new FormData();
    formData.append("file", pdfFile);
    formData.append("query", query);

    setLoading(true);
    setAnswer("");
    setChunks([]);

    try {
      const response = await axios.post(`${API_BASE}/query`, formData, {
        headers: {
          "Content-Type": "multipart/form-data",
        },
      });

      setAnswer(response.data.answer);
      setChunks(Array.from(new Set(response.data.used_chunks)).slice(0, 3));
    } catch (err) {
      console.error("Error communicating with backend:", err);
      alert("Error from backend.");
    }

    setLoading(false);
  };

  const parseAnswer = () => {
    let titleContent = "";
    let scopeContent = "";

    const titleMatch = answer.match(/(?:^|\n)title[:-]?\s*(.*?)(?=\n{2,}|scope and objective[:-]?)/is);
    const scopeMatch = answer.match(/scope and objective[:-]?\s*(.*)/is);

    if (titleMatch && titleMatch[1]) titleContent = titleMatch[1].trim();
    if (scopeMatch && scopeMatch[1]) scopeContent = scopeMatch[1].trim();

    // fallback if parsing fails
    if ((!titleContent || titleContent.length < 10) && answer) {
      titleContent = answer.trim();
      scopeContent = "";
    }

    return { titleContent, scopeContent };
  };

  const { titleContent, scopeContent } = parseAnswer();

  return (
    <div className="App">
      <h1 className="page-title">Product Requirement Generator</h1>

      <form className="input-form" onSubmit={handleSubmit}>
        <div className="upload-area">
          <label className="upload-label">📄 Upload Specification Document:</label>
          <input type="file" accept="application/pdf" onChange={handleFileChange} />
        </div>

        <div className="query-box">
          <label className="query-label">🧾 Enter Your Requirement Topic:</label>
          <textarea
            rows="4"
            placeholder="e.g., Write requirements for authentication process, including user validation, login, and multi-factor checks..."
            value={query}
            onChange={handleQueryChange}
          />
        </div>

        <button type="submit" disabled={loading}>
          {loading ? "Generating..." : "Generate Requirement"}
        </button>
      </form>

      {answer && (
        <div className="response-section">
          <div className="response-block">
            <h3 className="section-header blue">📌 Definition</h3>
            <p>{titleContent}</p>
          </div>

          <div className="response-block">
            <h3 className="section-header green">🎯 Scope and Objective</h3>
            <p>{scopeContent}</p>
          </div>
        </div>
      )}

      {chunks.length > 0 && (
        <div className="chunk-section">
          <h3>📚 Source Chunks Used</h3>
          {chunks.map((chunk, index) => (
            <div className="chunk-box" key={index}>
              <strong>Chunk {index + 1}</strong>
              <pre>{chunk}</pre>
            </div>
          ))}
        </div>
      )}
    </div>
  );
}

export default App;
