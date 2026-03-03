# Simple Sentiment Analysis (Rule-Based) - PTBR

positive_words = ["bom", "ótimo", "excelente", "feliz", "maravilhoso"]
negative_words = ["ruim", "péssimo", "triste", "horrível", "terrível"]

def analyze_sentiment(text):
    text = text.lower()
    
    positive_score = sum(word in text for word in positive_words)
    negative_score = sum(word in text for word in negative_words)

    if positive_score > negative_score:
        return "Positive"
    elif negative_score > positive_score:
        return "Negative"
    else:
        return "Neutral"


# Test example
sentence = "O atendimento foi excelente e maravilhoso"
result = analyze_sentiment(sentence)

print("Sentence:", sentence)
print("Sentiment:", result)
