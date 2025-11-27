from src.core.interfaces import Tokenizer

class SimpleTokenizer(Tokenizer):
    def tokenize(self, text: str) -> list[str]:
        text = text.lower()
        token = []

        for word in text.split():
            current_word = ""
            for char in word:
                if char in ".,!?;:-'\"()[]{}":
                    if current_word:
                        token.append(current_word)
                        current_word = ""
                    token.append(char)
                else:
                    current_word += char
            if current_word:
                token.append(current_word)

        return token