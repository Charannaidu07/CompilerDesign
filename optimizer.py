def optimize(code):
    optimized = []

    for line in code:
        if "+" in line or "*" in line:
            parts = line.split("=")
            expr = parts[1].strip()

            try:
                value = eval(expr)
                optimized.append(f"{parts[0].strip()} = {value}")
            except:
                optimized.append(line)
        else:
            optimized.append(line)

    return optimized
