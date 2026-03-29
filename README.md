# 🧠 Sentiment Analysis Tool

A beginner-friendly **CLI-based Sentiment Analysis Tool** built with Python and [TextBlob](https://textblob.readthedocs.io/). Analyze the emotional tone of text instantly — no dataset or model training required!

---

## 📁 Project Structure

```
sentiment_tool/
│
├── main.py           # CLI menu system (entry point)
├── sentiment.py      # Sentiment analysis logic (TextBlob)
├── history.txt       # Auto-created log of all analyses
├── requirements.txt  # Python dependencies
└── README.md         # Project documentation
```

---

## ⚙️ Setup Instructions

### 1. Prerequisites

Make sure you have **Python 3.7+** installed.

```bash
python --version
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

TextBlob also needs its language data (NLTK corpora). Run this **once** after installing:

```bash
python -m textblob.download_corpora
```

> If the above fails, try:
> ```bash
> python -c "import nltk; nltk.download('punkt'); nltk.download('averaged_perceptron_tagger')"
> ```

### 3. Run the Tool

```bash
python main.py
```

---

## 🖥️ How to Use

When you run the tool, you'll see a menu:

```
╔══════════════════════════════════════════════╗
║         🧠  SENTIMENT ANALYSIS TOOL          ║
║         Powered by TextBlob NLP              ║
╚══════════════════════════════════════════════╝

  ┌─────────────────────────────────────┐
  │           MAIN MENU                 │
  │                                     │
  │  1. Analyze Text                    │
  │  2. Analyze Multiple Sentences      │
  │  3. Show History                    │
  │  4. Exit                            │
  └─────────────────────────────────────┘
```

### Option 1 — Analyze Text

Enter a single sentence and get the sentiment label and score.

**Example:**
```
Enter text: I love coding!

  Text      : I love coding!
  Sentiment : Positive 😊
  Score     : 0.5  (range: -1.0 = most negative → +1.0 = most positive)
```

### Option 2 — Analyze Multiple Sentences

Enter several sentences separated by commas.

**Example:**
```
Input: The food was amazing, I hate waiting in queues, The weather is okay

  Found 3 sentence(s):

  #    Sentiment          Score      Text
  ──────────────────────────────────────────────────────────────────────
  1    Positive 😊        0.6        The food was amazing
  2    Negative 😞        -0.8       I hate waiting in queues
  3    Neutral 😐         0.0        The weather is okay
```

### Option 3 — Show History

Displays all past analyses saved to `history.txt`.

### Option 4 — Exit

Exits the program gracefully.

---

## 📊 Understanding the Score

| Score Range    | Sentiment |
|----------------|-----------|
| `> 0`          | Positive  |
| `= 0`          | Neutral   |
| `< 0`          | Negative  |
| Closer to `1`  | Very Positive |
| Closer to `-1` | Very Negative |

---

## 🛠️ Technology

| Component  | Library / Tool |
|------------|----------------|
| Language   | Python 3.7+    |
| NLP Engine | TextBlob       |
| Interface  | CLI (terminal) |
| Storage    | Plain text (`history.txt`) |

---

## 📝 Notes

- `history.txt` is created automatically the first time you run an analysis.
- All results are **appended** (not overwritten) so your history is preserved.
- The tool works entirely **offline** after the initial setup.

---

## 👨‍💻 Author

Built as a beginner-friendly Python CLI project. Feel free to extend it with more features!
