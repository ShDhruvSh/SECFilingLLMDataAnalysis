import React, { useState } from 'react';
import axios from 'axios';

function App() {
  const [symbol, setSymbol] = useState('');
  const [markdownText, setMarkdownText] = useState('');

  const handleSubmit = async () => {
    try {
      const response = await axios.post('http://localhost:5000/get_markdown', { symbol });
      setMarkdownText(response.data);
    } catch (error) {
      console.error('Error fetching data:', error);
    }
  };

  return (
    <div>
      <h1>Stock SEC 10-K Filing Analysis</h1>
      <input type="text" value={symbol} onChange={(e) => setSymbol(e.target.value)} />
      <button onClick={handleSubmit}>Submit</button>
      <div>
        <h2>Analysis:</h2>
        <div dangerouslySetInnerHTML={{ __html: markdownText }} />
      </div>
    </div>
  );
}

export default App;
