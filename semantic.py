from lark import Tree, Token

def build_symbol_table(tree):
    symbols = {}

    def walk(node):
        # If assignment statement
        if isinstance(node, Tree) and node.data == "statement":
            first = node.children[0]

            # Only assignments have ID on left
            if isinstance(first, Token) and first.type == "ID":
                symbols[first.value] = "int"

        # Traverse children
        if hasattr(node, "children"):
            for child in node.children:
                walk(child)

    walk(tree)
    return symbols
