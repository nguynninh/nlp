from src.core.interfaces import Vectorizer, Tokenizer
from typing import List, Dict

class CountVectorizer(Vectorizer):
    def __init__(self, tokenizer: Tokenizer):
        self.tokenizer = tokenizer
        self.vocabulary_: Dict[str, int] = {}
        
    def fit(self, corpus: List[str]) -> None:
        unique_tokens = set()
        
        for document in corpus:
            tokens = self.tokenizer.tokenize(document)
        
            unique_tokens.update(tokens)
        
        sorted_tokens = sorted(unique_tokens)
        self.vocabulary_ = {token: idx for idx, token in enumerate(sorted_tokens)}
    
    def transform(self, documents: List[str]) -> List[List[int]]:
        if not self.vocabulary_:
            raise ValueError("Vocabulary not fitted. Call fit() before transform().")
        
        result = []
        vocab_size = len(self.vocabulary_)
        
        for document in documents:
            count_vector = [0] * vocab_size
            
            tokens = self.tokenizer.tokenize(document)
            
            for token in tokens:
                if token in self.vocabulary_:
                    index = self.vocabulary_[token]
                    count_vector[index] += 1
            
            result.append(count_vector)
        
        return result
    
    def fit_transform(self, corpus: List[str]) -> List[List[int]]:
        self.fit(corpus)
        return self.transform(corpus)
