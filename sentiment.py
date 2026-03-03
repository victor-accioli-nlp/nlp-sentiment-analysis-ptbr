# Sentiment Analysis - Rule Based (Improved Version) - PTBR

# -----------------------------
# 1. Dataset manual (para testes)
# -----------------------------

dataset = [
    ("O atendimento foi excelente", "positivo"),
    ("O produto é horrível", "negativo"),
    ("A entrega foi ok", "neutro"),
    ("Estou muito feliz com a compra", "positivo"),
    ("Foi uma experiência ruim", "negativo"),
]

# -----------------------------
# 2. Palavras-chave
# -----------------------------

positive_words = ["bom", "ótimo", "excelente", "feliz", "maravilhoso"]
negative_words = ["ruim", "péssimo", "triste", "horrível", "terrível"]


# -----------------------------
# 3. Função principal
# -----------------------------

def analyze_sentiment(text):
    text = text.lower()
    words = text.split()

    positive_score = 0
    negative_score = 0

    for word in words:
        if word in positive_words:
            positive_score += 1
        if word in negative_words:
            negative_score += 1

    if positive_score > negative_score:
        return "positivo"
    elif negative_score > positive_score:
        return "negativo"
    else:
        return "neutro"


# -----------------------------
# 4. Avaliação simples
# -----------------------------

def evaluate_model(dataset):
    correct = 0

    for sentence, true_label in dataset:
        prediction = analyze_sentiment(sentence)

        print(f"Frase: {sentence}")
        print(f"Previsão: {prediction} | Real: {true_label}")
        print("-" * 40)

        if prediction == true_label:
            correct += 1

    accuracy = correct / len(dataset)
    print(f"Acurácia: {accuracy:.2f}")


# -----------------------------
# 5. Executar teste
# -----------------------------

if __name__ == "__main__":
    evaluate_model(dataset)
