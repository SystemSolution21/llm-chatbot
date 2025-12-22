// Chat.tsx

import { useState } from "react";
import { chat, feedback, ingest } from "./api";
import { MessageInput } from "./components/MessageInput/MessageInput";

// Define the Chat component
export default function Chat() {
  const [msg, setMsg] = useState("");
  const [resp, setResp] = useState<any>(null);

  const send = async (text: string) => {
    const r = await chat(text);
    setResp(r.data);
  };

  const handleIngest = async (text: string) => {
    await ingest(text);
    alert("Text ingested into Knowledge Base!");
  };

  const rate = (rating: number) => {
    feedback({
      conversation_id: resp.conversation_id,
      rating
    });
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
