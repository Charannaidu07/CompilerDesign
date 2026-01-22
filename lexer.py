import re

TOKEN_SPEC = [
    ("NUMBER",   r"\d+"),
    ("PRINT",    r"print"),
    ("WHILE",    r"while"),
    ("IF",       r"if"),

    # Relational operators (IMPORTANT)
    ("EQ",       r"=="),
    ("LT",       r"<"),
    ("GT",       r">"),

    # Arithmetic operators
    ("ASSIGN",   r"="),
    ("PLUS",     r"\+"),
    ("MUL",      r"\*"),

    # Brackets
    ("LPAREN",   r"\("),
    ("RPAREN",   r"\)"),
    ("LBRACE",   r"\{"),
    ("RBRACE",   r"\}"),

    # Identifiers
    ("ID",       r"[a-zA-Z_]\w*"),

    ("NEWLINE",  r"\n"),
    ("SKIP",     r"[ \t]+"),
    ("MISMATCH", r"."),
]

def tokenize(code):
    regex = "|".join(f"(?P<{name}>{pattern})" for name, pattern in TOKEN_SPEC)
    tokens = []

    for match in re.finditer(regex, code):
        kind = match.lastgroup
        value = match.group()

        if kind in ("SKIP", "NEWLINE"):
            continue
        elif kind == "MISMATCH":
            raise RuntimeError(f"Unexpected character: {value}")
        else:
            tokens.append((kind, value))

    return tokens
