import re
from collections import Counter
from typing import List, Tuple

WORD_RE = re.compile(r"\w+", flags=re.UNICODE)

def _tokenize(text: str) -> List[str]:
    return [w.lower() for w in WORD_RE.findall(text)]

def word_count(text: str) -> int:
    return len(_tokenize(text))

def char_count(text: str, with_spaces: bool = False) -> int:
    if with_spaces:
        return len(text)
    return len(text.replace(" ", "").replace("\n", ""))

def top_words(text: str, n: int = 10) -> List[Tuple[str, int]]:
    tokens = _tokenize(text)
    counter = Counter(tokens)
    return counter.most_common(n)

def estimate_reading_time(text: str, wpm: int = 200) -> float:
    wc = word_count(text)
    return wc / float(wpm)
