// MessageInput.tsx

import { useState } from "react";
import styles from "./MessageInput.module.css";

type Props = {
  onSend: (text: string) => void;
  onIngest?: (text: string) => void;
};

export function MessageInput({ onSend, onIngest }: Props) {
  const [text, setText] = useState("");

  const handleSend = () => {
    if (!text.trim()) return;
    onSend(text);
    setText("");
  };

  const handleIngest = () => {
    if (!text.trim()) return;
    onIngest?.(text);
    setText("");
  };

  return (
    <div className={styles.container}>
      <textarea
        className={styles.textarea}
        value={text}
        onChange={(e) => setText(e.target.value)}
        placeholder="Type your message..."
        rows={3}
      />

      <button className={styles.sendButton} onClick={handleSend}>
        Send
      </button>

      {onIngest && (
        <button className={styles.ingestButton} onClick={handleIngest}>
          Ingest (RAG)
        </button>
      )}
    </div>
  );
}