// Chat.tsx

// Import React
import { useState } from "react";

// Import API functions
import { chat, feedback } from "./api";

// Define the Chat component
export default function Chat() {
  const [msg, setMsg] = useState("");
  const [resp, setResp] = useState<any>(null);

  const send = async () => {
    const r = await chat(msg);
    setResp(r.data);
  };

  const rate = (rating: number) => {
    feedback({
      conversation_id: resp.conversation_id,
      rating
    });
  };

  return (
    <div>
      <textarea onChange={e => setMsg(e.target.value)} />
      <button onClick={send}>Send</button>

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
