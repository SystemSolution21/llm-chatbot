// api.ts

// Import the axios library
import axios from "axios";

// Create an axios instance with a base URL from environment variables
const apiClient = axios.create({
  baseURL: import.meta.env.VITE_API_URL || "http://localhost:8000",
  headers: {
    "Content-Type": "application/json",
  },
});

// Structure of the Chat response
export interface ChatResponse {
  conversation_id: string;
  answer: string;
}

// Structure of the Feedback request
export interface FeedbackRequest {
  conversation_id: string;
  rating: number;
  corrected_answer?: string;
  issue?: string;
}

// Define the API chat endpoints
export const chat = (message: string) =>
  apiClient.post<ChatResponse>("/chat", { message });

// Define the API feedback endpoint
export const feedback = (data: FeedbackRequest) =>
  apiClient.post("/feedback", data);

// Define the API ingest endpoint
export const ingest = (message: string) =>
  apiClient.post("/ingest", { message });
