// Chat.tsx

import { useState } from "react";
import { chat, feedback, ingest } from "./api";
import { MessageInput } from "./components/MessageInput/MessageInput";

// Define the shape of the API response
interface ChatResponse {
  conversation_id: string;
  answer: string;
}

// Define the Chat component
export default function Chat() {
  const [resp, setResp] = useState<ChatResponse | null>(null);

  const send = async (text: string) => {
    try {
      const r = await chat(text);
      setResp(r.data);
    } catch (error) {
      console.error("Failed to send message:", error);
      alert("Error sending message.");
    }
  };

  const handleIngest = async (text: string) => {
    try {
      await ingest(text);
      alert("Text ingested into Knowledge Base!");
    } catch (error) {
      console.error("Failed to ingest text:", error);
      alert("Error ingesting text.");
    }
  };

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

  return (
    <div>
      <MessageInput onSend={send} onIngest={handleIngest} />

      {resp && (
        <>
          <p>{resp.answer}</p>
          <button onClick={() => rate(1)}>👍</button>
          <button onClick={() => rate(-1)}>👎</button>
        </>
      )}
    </div>
  );
}
