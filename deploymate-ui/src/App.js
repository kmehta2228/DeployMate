import React, { useEffect, useState } from 'react';

function App() {
  const [logs, setLogs] = useState(null);
  const [version, setVersion] = useState(null);
  const [resources, setResources] = useState(null);

  useEffect(() => {
    fetch('http://localhost:8000/logs').then(res => res.json()).then(setLogs);
    fetch('http://localhost:8000/version').then(res => res.json()).then(setVersion);
    fetch('http://localhost:8000/resources').then(res => res.json()).then(setResources);
  }, []);

  return (
    <div style={{ padding: '30px', fontFamily: 'Arial' }}>
      <h1>🚀 DeployMate Dashboard (React)</h1>

      <h2>📦 Deployment Logs</h2>
      <pre>{JSON.stringify(logs, null, 2)}</pre>

      <h2>🔖 Version Info</h2>
      <pre>{JSON.stringify(version, null, 2)}</pre>

      <h2>📊 Resource Usage</h2>
      <pre>{JSON.stringify(resources, null, 2)}</pre>
    </div>
  );
}

export default App;
