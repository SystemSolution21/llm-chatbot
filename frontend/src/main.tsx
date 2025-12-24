// frontend/src/main.tsx

import React from "react";
import ReactDOM from "react-dom/client";
import App from "./App";
import ReadmeRenderer from "./components/ReadmeRenderer";

// Render the README.md file
ReactDOM.createRoot(document.getElementById("container")!).render(
  <ReadmeRenderer />
);

// Render the App component
ReactDOM.createRoot(document.getElementById("root")!).render(
  <React.StrictMode>
    <App />
  </React.StrictMode>
);