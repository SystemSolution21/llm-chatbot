// frontend/vite.config.ts

// Import necessary modules
import { defineConfig } from "vite";
import react from "@vitejs/plugin-react";

// Define the Vite configuration
export default defineConfig({
  plugins: [react()],
  server: {
    port: 5173
  }
});