import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.preprocessing.regex_tokenizer import RegexTokenizer
from src.representations.count_vectorizer import CountVectorizer

tokenizer = RegexTokenizer()
vectorizer = CountVectorizer(tokenizer)

corpus = [
    "I love NLP.",
    "I love programming.",
    "NLP is a subfield of AI."
]

document_term_matrix = vectorizer.fit_transform(corpus)

print("Learned Vocabulary (token: index):")
for token, index in vectorizer.vocabulary_.items():
    print(f"  {token}: {index}")

print("\nDocument-Term Matrix (count vectors):")
for i, vector in enumerate(document_term_matrix):
    print(f"  Document {i + 1}: {vector}")

print("\nDocument-Term Matrix with Tokens:")
token_list = sorted(vectorizer.vocabulary_.items(), key=lambda x: x[1])
tokens = [token for token, _ in token_list]

print(f"  Tokens: {tokens}")
for i, vector in enumerate(document_term_matrix):
    print(f"  Document {i + 1}: {corpus[i]}")
    print(f"  Counts: {vector}")
    
    non_zero_counts = []
    for token, count in zip(tokens, vector):
        if count > 0:
            non_zero_counts.append(f"{token}: {count}")
    print(f"  Non-zero counts: {', '.join(non_zero_counts)}")
    print()

from src.core.dataset_loaders import load_raw_text_data
dataset_path = "UD_English-EWT/en_ewt-ud-train.txt"
raw_text = load_raw_text_data(dataset_path)

sample_text = raw_text[:500]

print("--- Tokenizing Sample Text from UD_English-EWT ---")
print(f"Original Sample: {sample_text[:100]}...")

tokens = tokenizer.tokenize(sample_text)
print(f"Tokens: {tokens[:20]}...")

vector = vectorizer.transform([sample_text])[0]
print(f"Count Vector (first 20 counts): {vector[:20]}...")
print(f"Vocabulary Size: {len(vectorizer.vocabulary_)}")

print(f"Sample Text Count Vector (non-zero counts):")
non_zero_counts = []
for token, index in vectorizer.vocabulary_.items():
    count = vector[index]
    if count > 0:
        non_zero_counts.append(f"{token}: {count}")
print(f"  {', '.join(non_zero_counts)}")