import styles from "./Feedback.module.css";

interface FeedbackProps {
    onRate: (rating: number) => void;
}

export function Feedback({ onRate }: FeedbackProps) {
    return (
        <div className={styles.container}>
            <button className={styles.button} onClick={() => onRate(1)} aria-label="Thumbs up">
                👍
            </button>
            <button className={styles.button} onClick={() => onRate(-1)} aria-label="Thumbs down">
                👎
            </button>
        </div>
    );
}
