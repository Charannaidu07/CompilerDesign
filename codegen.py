def generate_target(code):
    target = []

    for line in code:
        if "=" in line:
            left, expr = line.split("=")
            target.append(f"LOAD {expr.strip()}")
            target.append(f"STORE {left.strip()}")

    return target
