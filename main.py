from sentiment import analyze_sentiment, analyze_multiple
from datetime import datetime

HISTORY_FILE = "history.txt"

BANNER = """
╔══════════════════════════════════════════════╗
║         🧠  SENTIMENT ANALYSIS TOOL          ║
║         Powered by TextBlob NLP              ║
╚══════════════════════════════════════════════╝
"""

MENU = """
  ┌─────────────────────────────────────┐
  │           MAIN MENU                 │
  │                                     │
  │  1. Analyze Text                    │
  │  2. Analyze Multiple Sentences      │
  │  3. Show History                    │
  │  4. Exit                            │
  └─────────────────────────────────────┘
"""


def save_to_history(entry: str) -> None:
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(HISTORY_FILE, "a", encoding="utf-8") as f:
        f.write(f"[{timestamp}]\n{entry}\n{'-' * 50}\n")


def show_history() -> None:
    print("\n" + "=" * 50)
    print("  📋  ANALYSIS HISTORY")
    print("=" * 50)
    try:
        with open(HISTORY_FILE, "r", encoding="utf-8") as f:
            content = f.read().strip()
        if content:
            print(content)
        else:
            print("  No history found. Start analyzing some text!")
    except FileNotFoundError:
        print("  No history file found yet. Analyze some text first.")
    print("=" * 50 + "\n")


def menu_analyze_text() -> None:
    print("\n── Analyze Text ──────────────────────────────")
    user_input = input("  Enter text: ").strip()

    if not user_input:
        print("  ⚠️  Error: Input cannot be empty. Please try again.")
        return

    result = analyze_sentiment(user_input)

    output = (
        f"\n  Text      : {result['text']}\n"
        f"  Sentiment : {result['label']}\n"
        f"  Score     : {result['score']}  (range: -1.0 = most negative → +1.0 = most positive)\n"
    )
    print(output)

    history_entry = (
        f"[Single Analysis]\n"
        f"Text      : {result['text']}\n"
        f"Sentiment : {result['label']}\n"
        f"Score     : {result['score']}"
    )
    save_to_history(history_entry)
    print("  ✅  Result saved to history.txt")


def menu_analyze_multiple() -> None:
    print("\n── Analyze Multiple Sentences ────────────────")
    print("  Enter sentences separated by commas.")
    user_input = input("  Input: ").strip()

    if not user_input:
        print("  ⚠️  Error: Input cannot be empty. Please try again.")
        return

    results = analyze_multiple(user_input)

    if not results:
        print("  ⚠️  No valid sentences found after splitting. Please check your input.")
        return

    print(f"\n  Found {len(results)} sentence(s):\n")
    print(f"  {'#':<4} {'Sentiment':<18} {'Score':<10} Text")
    print("  " + "─" * 70)

    history_lines = ["[Multiple Analysis]"]
    for i, res in enumerate(results, start=1):
        print(f"  {i:<4} {res['label']:<18} {res['score']:<10} {res['text']}")
        history_lines.append(
            f"  {i}. [{res['label']}] (score: {res['score']}) → {res['text']}"
        )

    print()
    save_to_history("\n".join(history_lines))
    print("  ✅  Results saved to history.txt")


def main() -> None:
    print(BANNER)

    while True:
        print(MENU)
        choice = input("  Enter your choice (1-4): ").strip()

        if choice == "1":
            menu_analyze_text()

        elif choice == "2":
            menu_analyze_multiple()

        elif choice == "3":
            show_history()

        elif choice == "4":
            print("\n  👋  Thank you for using the Sentiment Analysis Tool. Goodbye!\n")
            break

        else:
            print(f"\n  ⚠️  Invalid choice '{choice}'. Please enter a number between 1 and 4.\n")


if __name__ == "__main__":
    main()
