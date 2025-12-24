// Chat.tsx

import { useState } from "react";
import { chat, feedback, ingest, type ChatResponse } from "./api";
import { MessageInput } from "./components/MessageInput/MessageInput";
import { Feedback } from "./components/Feedback/Feedback";

// Define the Chat component
export default function Chat() {
  const [resp, setResp] = useState<ChatResponse | null>(null);
  const [isChatting, setIsChatting] = useState(false);
  const [isIngesting, setIsIngesting] = useState(false);

  // Define the send function for user messages
  const send = async (text: string) => {
    setIsChatting(true);
    try {
      const r = await chat(text);
      setResp(r.data);
    } catch (error) {
      console.error("Failed to send message:", error);
      // In a real app, use a toast notification here instead of alert
      alert("Error sending message.");
    } finally {
      setIsChatting(false);
    }
  };

  // Define the ingest function for RAG
  const handleIngest = async (text: string) => {
    setIsIngesting(true);
    try {
      await ingest(text);
      alert("Text ingested into Knowledge Base!");
    } catch (error) {
      console.error("Failed to ingest text:", error);
      alert("Error ingesting text.");
    } finally {
      setIsIngesting(false);
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

  // Render the input message and feedback components
  return (
    <div>
      <MessageInput onSend={send} onIngest={handleIngest} />

      {isIngesting && <p>Ingesting knowledge...</p>}
      {isChatting && <p>Thinking...</p>}

      {resp && (
        <>
          <p>{resp.answer}</p>
          <Feedback onRate={rate} />
        </>
      )}
    </div>
  );
}
