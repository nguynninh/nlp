import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.core.dataset_loaders import load_raw_text_data
from src.preprocessing.simple_tokenizer import SimpleTokenizer
from src.preprocessing.regex_tokenizer import RegexTokenizer

print("Task 1: Simple Tokenizer")
simple_tokenizer = SimpleTokenizer()
text1 = "Hello, world! This is a test."
tokens1 = simple_tokenizer.tokenize(text1)
print(f"Original: {text1}")
print(f"Tokens: {tokens1}")

text2 = "NLP is fun: let's learn it."
tokens2 = simple_tokenizer.tokenize(text2)
print(f"Original: {text2}")
print(f"Tokens: {tokens2}")

print("\nTask 2: Regex Tokenizer")
regex_tokenizer = RegexTokenizer()
text3 = "Hello, world! This is a test."
tokens3 = regex_tokenizer.tokenize(text3)
print(f"Original: {text3}")
print(f"Tokens: {tokens3}")

text4 = "NLP is fun: let's learn it."
tokens4 = regex_tokenizer.tokenize(text4)
print(f"Original: {text4}")
print(f"Tokens: {tokens4}")

print("\nTask 3:")
dataset_path = "UD_English-EWT/en_ewt-ud-train.txt"
raw_text = load_raw_text_data(dataset_path)

sample_text = raw_text[:500]

print("--- Tokenizing Sample Text from UD_English-EWT ---")
print(f"Original Sample: {sample_text[:100]}...")

simple_tokens = simple_tokenizer.tokenize(sample_text)
print(f"SimpleTokenizer Output (first 20 tokens): {simple_tokens[:20]}")

regex_tokens = regex_tokenizer.tokenize(sample_text)
print(f"RegexTokenizer Output (first 20 tokens): {regex_tokens[:20]}")