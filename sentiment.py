from textblob import TextBlob


def analyze_sentiment(text: str) -> dict:
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity

    if polarity > 0:
        label = "Positive 😊"
    elif polarity < 0:
        label = "Negative 😞"
    else:
        label = "Neutral 😐"

    return {
        "text": text,
        "label": label,
        "score": round(polarity, 4)
    }


def analyze_multiple(text_input: str) -> list:
    sentences = [s.strip() for s in text_input.split(",") if s.strip()]
    results = []
    for sentence in sentences:
        result = analyze_sentiment(sentence)
        results.append(result)
    return results
