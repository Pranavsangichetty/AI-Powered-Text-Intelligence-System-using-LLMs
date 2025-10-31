from transformers import pipeline

def classify_text(text):
    """
    Classifies text into categories like risk, malicious, or safe.
    """
    classifier = pipeline("text-classification", model="distilbert-base-uncased-finetuned-sst-2-english")
    result = classifier(text)[0]
    label = result['label']
    score = result['score']
    return {"label": label, "confidence": round(score, 3)}
