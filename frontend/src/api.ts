// api.ts

// Import the axios library
import axios from "axios";

// Define the API chat endpoints
export const chat = (message: string) =>
  axios.post("http://localhost:8000/chat", { message });

// Define the API feedback endpoints
export interface FeedbackRequest {
  conversation_id: string;
  rating: number;
  corrected_answer?: string;
  issue?: string;
}

export const feedback = (data: FeedbackRequest) =>
  axios.post("http://localhost:8000/feedback", data);
