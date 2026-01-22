from graphviz import Digraph

def draw_tree(tree):
    dot = Digraph()
    count = 0

    def add(node, parent=None):
        nonlocal count
        my_id = str(count)
        dot.node(my_id, str(node.data if hasattr(node, 'data') else node))
        count += 1

        if parent is not None:
            dot.edge(parent, my_id)

        if hasattr(node, "children"):
            for child in node.children:
                add(child, my_id)

    add(tree)
    return dot
