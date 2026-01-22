from lark import Lark

grammar = """
start: statement+

statement: ID "=" expr
         | "print" "(" ID ")"
         | "if" "(" condition ")" block
         | "while" "(" condition ")" block

block: "{" statement+ "}"

condition: expr REL_OP expr

REL_OP: ">" | "<" | "=="

?expr: expr "+" term   -> add
     | term

?term: term "*" factor -> mul
     | factor

?factor: NUMBER        -> number
       | ID            -> var
       | "(" expr ")"

%import common.CNAME -> ID
%import common.NUMBER
%import common.WS
%ignore WS
"""

parser = Lark(grammar, start="start", parser="lalr")

def parse_code(code):
    return parser.parse(code)
