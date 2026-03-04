# NLP Sentiment Analysis (PT-BR)

Projeto simples de análise de sentimento em português utilizando abordagem baseada em regras (Rule-Based).

## 📌 Objetivo

Classificar frases como:

- Positivo
- Negativo
- Neutro

Utilizando listas de palavras-chave.

## 🧠 Como funciona

O algoritmo:

1. Converte o texto para minúsculo
2. Divide a frase em palavras
3. Conta quantas palavras positivas e negativas aparecem
4. Retorna a classificação com maior pontuação

## 📊 Estrutura do Projeto

- `sentiment.py` → código principal
- Dataset manual para testes
- Função de avaliação com cálculo de acurácia

## 🚀 Como executar

Execute o arquivo:

```bash
python sentiment.py
