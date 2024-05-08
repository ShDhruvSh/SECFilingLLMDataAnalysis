import React, { useState } from 'react';
import axios from 'axios';
import ReactMarkdown from 'react-markdown';
import { CircularProgress } from '@material-ui/core';

function App() {
  const [symbol, setSymbol] = useState('');
  const [markdownText, setMarkdownText] = useState('');
  const [loading, setLoading] = useState(false); // Add a loading state

  const handleSubmit = async () => {
    try {
      setLoading(true);
      console.log(process.env.REACT_APP_API_URL)
      const response = await axios.post(process.env.REACT_APP_API_URL+'get_markdown', { symbol });
      setMarkdownText(response.data);
    } catch (error) {
      console.error('Error fetching data:', error);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div>
      <h1>Stock SEC 10-K Filing Analysis</h1>
      <input type="text" value={symbol} onChange={(e) => setSymbol(e.target.value)} />
      <button onClick={handleSubmit}>Submit</button>
      <div>
        {loading ? ( // Render CircularProgress if loading is true
          <div style={{ display: 'flex', justifyContent: 'center', alignItems: 'center', minHeight: '100px' }}>
            <CircularProgress />
          </div>
        ) : (
          <div>
            <h2>Analysis:</h2>
            <ReactMarkdown>{markdownText}</ReactMarkdown>
          </div>
        )}
      </div>
    </div>
  );
}

export default App;
