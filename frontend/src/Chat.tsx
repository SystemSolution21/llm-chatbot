// Chat.tsx

// Import React
import { useState } from "react";

// Import API functions
import { chat, feedback, ingest } from "./api";

// Define the Chat component
export default function Chat() {
  const [msg, setMsg] = useState("");
  const [resp, setResp] = useState<any>(null);

  const send = async () => {
    const r = await chat(msg);
    setResp(r.data);
  };

  const handleIngest = async () => {
    await ingest(msg);
    alert("Text ingested into Knowledge Base!");
    setMsg("");
  };

  const rate = (rating: number) => {
    feedback({
      conversation_id: resp.conversation_id,
      rating
    });
  };

  return (
    <div style={{ whiteSpace: "pre-wrap" }}>
      <textarea value={msg} onChange={e => setMsg(e.target.value)} />
      <button onClick={send}>Send</button>
      <button onClick={handleIngest} style={{ marginLeft: "10px" }}>Ingest (RAG)</button>

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
