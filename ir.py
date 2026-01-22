from lark import Tree, Token

temp_count = 0
label_count = 0

def new_temp():
    global temp_count
    temp_count += 1
    return f"t{temp_count}"

def new_label():
    global label_count
    label_count += 1
    return f"L{label_count}"

def generate_ir(tree):
    code = []

    # ---------------- EXPRESSIONS ---------------- #

    def eval_expr(node):
        if isinstance(node, Token):
            return node.value

        if not isinstance(node, Tree):
            return None

        if node.data == "number":
            return node.children[0].value

        if node.data == "var":
            return node.children[0].value

        if node.data in ("add", "mul"):
            left = eval_expr(node.children[0])
            right = eval_expr(node.children[1])
            op = "+" if node.data == "add" else "*"
            t = new_temp()
            code.append(f"{t} = {left} {op} {right}")
            return t

        return None

    # ---------------- CONDITIONS ---------------- #

    def eval_condition(node):
        left = eval_expr(node.children[0])
        op = node.children[1].value
        right = eval_expr(node.children[2])
        t = new_temp()
        code.append(f"{t} = {left} {op} {right}")
        return t

    # ---------------- STATEMENTS ---------------- #

    def walk(node):

        # Program root
        if node.data == "start":
            for stmt in node.children:
                walk(stmt)

        # Assignment
        elif node.data == "statement" and isinstance(node.children[0], Token):
            var = node.children[0].value
            expr = node.children[1]
            value = eval_expr(expr)
            code.append(f"{var} = {value}")

        # Print
        elif node.data == "statement" and node.children[0] == "print":
            var = node.children[1].children[0].value
            code.append(f"PRINT {var}")

        # IF statement
        elif node.data == "statement" and node.children[0] == "if":
            cond_node = node.children[1]
            block_node = node.children[2]

            end_label = new_label()
            cond = eval_condition(cond_node)
            code.append(f"IF_FALSE {cond} GOTO {end_label}")

            for stmt in block_node.children:
                walk(stmt)

            code.append(f"LABEL {end_label}")

        # WHILE loop
        elif node.data == "statement" and node.children[0] == "while":
            cond_node = node.children[1]
            block_node = node.children[2]

            start_label = new_label()
            end_label = new_label()

            code.append(f"LABEL {start_label}")
            cond = eval_condition(cond_node)
            code.append(f"IF_FALSE {cond} GOTO {end_label}")

            for stmt in block_node.children:
                walk(stmt)

            code.append(f"GOTO {start_label}")
            code.append(f"LABEL {end_label}")

        # Block
        elif node.data == "block":
            for stmt in node.children:
                walk(stmt)

    walk(tree)
    return code
