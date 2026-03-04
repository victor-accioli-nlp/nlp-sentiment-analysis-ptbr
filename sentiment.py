# sentiment.py

# 1. Dataset manual para testes
dataset = [
    ("O atendimento foi excelente", "positivo"),
    ("O produto é horrível", "negativo"),
    ("A entrega foi ok", "neutro"),
    ("Estou muito feliz com a compra", "positivo"),
    ("Foi uma experiência ruim", "negativo")
]

# 2. Palavras-chave
positive_words = ["bom", "ótimo", "excelente", "feliz", "gostei", "legal"]
negative_words = ["ruim", "péssimo", "triste", "odiei", "horrível", "difícil"]

def analisar_sentimento(frase):
    frase = frase.lower()
    palavras = frase.split()
    
    score = 0
    for p in palavras:
        if p in positive_words:
            score += 1
        elif p in negative_words:
            score -= 1
            
    if score > 0: return "positivo"
    elif score < 0: return "negativo"
    else: return "neutro"

# 3. Avaliação simples
acertos = 0
for frase, real in dataset:
    previsao = analisar_sentimento(frase)
    if previsao == real:
        acertos += 1

print(f"Acurácia: {(acertos/len(dataset))*100}%")

