// Chat.tsx

import { useState } from "react";
import { chat, feedback, ingest } from "./api";
import { MessageInput } from "./components/MessageInput/MessageInput";
import { Feedback } from "./components/Feedback/Feedback";

// Define the shape of the API response
interface ChatResponse {
  conversation_id: string;
  answer: string;
}

// Define the Chat component
export default function Chat() {
  const [resp, setResp] = useState<ChatResponse | null>(null);

  // Define the send function for user messages
  const send = async (text: string) => {
    try {
      const r = await chat(text);
      setResp(r.data);
    } catch (error) {
      console.error("Failed to send message:", error);
      alert("Error sending message.");
    }
  };

  // Define the ingest function for RAG
  const handleIngest = async (text: string) => {
    try {
      await ingest(text);
      alert("Text ingested into Knowledge Base!");
    } catch (error) {
      console.error("Failed to ingest text:", error);
      alert("Error ingesting text.");
    }
  };

  // Define the rate function for feedback
  const rate = async (rating: number) => {
    if (!resp) return;
    try {
      await feedback({
        conversation_id: resp.conversation_id,
        rating
      });
    } catch (error) {
      console.error("Failed to submit feedback:", error);
    }
  };

  // Render the components
  return (
    <div>
      <MessageInput onSend={send} onIngest={handleIngest} />

      {resp && (
        <>
          <p>{resp.answer}</p>
          <Feedback onRate={rate} />
        </>
      )}
    </div>
  );
}
