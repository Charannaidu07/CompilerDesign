import streamlit as st
from lexer import tokenize
from parser import parse_code
from semantic import build_symbol_table
from ir import generate_ir
from optimizer import optimize
from codegen import generate_target
from utils import draw_tree

st.set_page_config(page_title="Smart Mini Compiler", layout="wide")

st.title("🧠 Smart Mini Language Compiler with Visualizer")

code = st.text_area("Enter MiniLang Code", height=200)

if st.button("🚀 Compile"):
    try:
        # Lexical
        tokens = tokenize(code)
        st.subheader("1️⃣ Tokens")
        st.write(tokens)

        # Parsing
        tree = parse_code(code)
        st.subheader("2️⃣ Parse Tree")
        st.graphviz_chart(draw_tree(tree))

        # Semantic
        symbols = build_symbol_table(tree)
        st.subheader("3️⃣ Symbol Table")
        st.write(symbols)

        # IR
        ir_code = generate_ir(tree)
        st.subheader("4️⃣ Intermediate Code")
        st.code("\n".join(ir_code))

        # Optimization
        opt_code = optimize(ir_code)
        st.subheader("5️⃣ Optimized Code")
        st.code("\n".join(opt_code))

        # Target Code
        target = generate_target(opt_code)
        st.subheader("6️⃣ Target Code")
        st.code("\n".join(target))

    except Exception as e:
        st.error(f"Error: {e}")
