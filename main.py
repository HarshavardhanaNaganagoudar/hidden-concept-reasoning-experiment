from pathlib import Path

import ollama

from scenario import SCENARIO
from prompt import build_prompt


MODEL = "qwen3.5:9b"
RUNS = 10

OUTPUT_DIR = Path("outputs")
OUTPUT_DIR.mkdir(exist_ok=True)


def run_experiment(run_number):
    prompt = build_prompt(
        SCENARIO["hidden_concept"],
        SCENARIO["task"],
    )

    response = ollama.chat(
        model=MODEL,
        messages=[
            {
                "role": "user",
                "content": prompt,
            }
        ],
        think=True,
    )

    thinking = response.message.thinking
    answer = response.message.content

    run_dir = OUTPUT_DIR / f"run_{run_number:02d}"
    run_dir.mkdir(exist_ok=True)

    (run_dir / "thinking.txt").write_text(
        thinking or "",
        encoding="utf-8",
    )

    (run_dir / "answer.txt").write_text(
        answer or "",
        encoding="utf-8",
    )

    print(f"\n--- RUN {run_number:02d} ---")
    print("\n--- THINKING ---")
    print(thinking)

    print("\n--- ANSWER ---")
    print(answer)


if __name__ == "__main__":
    for run_number in range(1, RUNS + 1):
        run_experiment(run_number)