import re

# Mapping of English number words to integers (non-composite only)
# e.g. "one" -> 1, "twenty" -> 20
EN_WORD_TO_INT = {
    "one": 1, "two": 2, "three": 3, "four": 4, "five": 5,
    "six": 6, "seven": 7, "eight": 8, "nine": 9, "ten": 10,
    "eleven": 11, "twelve": 12, "thirteen": 13, "fourteen": 14,
    "fifteen": 15, "sixteen": 16, "seventeen": 17,
    "eighteen": 18, "nineteen": 19,
    "twenty": 20, "thirty": 30, "forty": 40, "fifty": 50,
    "sixty": 60, "seventy": 70, "eighty": 80, "ninety": 90,
}

# Reverse mapping: integer -> English word
# Used when the incremented value still has an English representation
INT_TO_EN_WORD = {v: k for k, v in EN_WORD_TO_INT.items()}

# Regex for English number words
# - Longer words are matched first to avoid partial matches
WORD_RE = re.compile(
    "(" + "|".join(sorted(EN_WORD_TO_INT.keys(), key=len, reverse=True)) + ")",
    re.I
)

# Regex for Arabic numbers (integers only)
DIGIT_RE = re.compile(r"\d+")

def inflate_string(text: str) -> str:
    """
    Increment all numbers found in the input string:
    - Arabic integers (e.g. 2 -> 3)
    - English number words, including substrings (e.g. someone -> sometwo)
    """

    # 1) Increment Arabic numbers
    def repl_digits(m):
        # Convert matched digits to int, add 1, and convert back to string
        return str(int(m.group(0)) + 1)

    text = DIGIT_RE.sub(repl_digits, text)

    # 2) Increment English number words
    def repl_word(m):
        word = m.group(1).lower()
        value = EN_WORD_TO_INT[word] + 1

        # If the incremented value has an English word, use it;
        # otherwise, fall back to a numeric string
        return INT_TO_EN_WORD.get(value, str(value))

    return WORD_RE.sub(repl_word, text)


if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        print(inflate_string(" ".join(sys.argv[1:])))
    else:
        print(inflate_string(sys.stdin.read()))