# 🧠 Smart Mini Language Compiler with Optimization Visualizer

A web-based educational compiler that demonstrates all **six phases of compiler design** with live visualization.

Users can write programs in a custom mini language (MiniLang), and the system visually displays:

✔️ Lexical Analysis (Tokens)  
✔️ Syntax Analysis (Parse Tree)  
✔️ Semantic Analysis (Symbol Table)  
✔️ Intermediate Code Generation (Three Address Code)  
✔️ Code Optimization  
✔️ Target Code Generation  

This project is designed for **Compiler Design PBL / Academic Demonstration**.

---

## 🚀 Features

- ✅ Supports variables and arithmetic expressions
- ✅ Supports `if` conditional statements
- ✅ Supports `while` loops
- ✅ Automatic token generation
- ✅ Parse tree visualization
- ✅ Symbol table generation
- ✅ Three Address Code generation
- ✅ Code optimization (constant folding)
- ✅ Pseudo assembly code generation
- ✅ Interactive web UI using Streamlit

---

## 🛠️ Technology Stack

- **Python 3.9+**
- **Streamlit** – Web UI
- **Lark Parser** – Grammar parsing
- **Graphviz** – Parse tree visualization
- **Pandas** – Table display

---

## 📁 Project Structure

smart-compiler/
│
├── app.py # Streamlit UI
├── lexer.py # Lexical Analyzer
├── parser.py # Syntax Analyzer
├── semantic.py # Symbol Table Builder
├── ir.py # Intermediate Code Generator
├── optimizer.py # Code Optimization
├── codegen.py # Target Code Generator
├── utils.py # Tree Visualization Utilities
├── requirements.txt # Dependencies
└── README.md


---

## ⚙️ Installation & Setup

### 1️⃣ Clone or Download Project

git clone <your-repo-url>
cd smart-compiler


---

### 2️⃣ Install Dependencies

pip install -r requirements.txt


> ⚠️ Graphviz software must also be installed separately:  
https://graphviz.org/download/

---

### 3️⃣ Run Application

streamlit run app.py


Open browser automatically at:

http://localhost:8501


---

## ✍️ Sample Input

a = 1
while (a < 5) {
a = a + 1
}
if (a > 3) {
print(a)
}


---

## 📤 Sample Output

The system displays:

1️⃣ Tokens  
2️⃣ Parse Tree  
3️⃣ Symbol Table  
4️⃣ Intermediate Code  
5️⃣ Optimized Code  
6️⃣ Target Code  

---

## 🧪 Supported Mini Language Syntax

### ✔️ Assignment
x = 10


### ✔️ Arithmetic Expressions
y = x + 5 * 2


### ✔️ Print
print(x)


### ✔️ If Statement
if (x > 10) {
print(x)
}


### ✔️ While Loop
while (x < 5) {
x = x + 1
}


---

## 🎓 Compiler Phases Implemented

| Phase | Description |
|--------|-------------|
| Lexical Analysis | Tokenizes input source code |
| Syntax Analysis | Builds parse tree using grammar |
| Semantic Analysis | Builds symbol table |
| Intermediate Code | Generates Three Address Code |
| Optimization | Performs constant folding |
| Code Generation | Generates pseudo assembly |

---

## 📌 Future Enhancements

- 🔲 Else statement support
- 🔲 Boolean operators (AND / OR)
- 🔲 Live code execution
- 🔲 Error highlighting
- 🔲 Control Flow Graph visualization
- 🔲 Export report to PDF

---

## 👩‍💻 Developed By

**Your Name**  
Department of Computer Science and Engineering  
Sathyabama Institute of Science and Technology  
Batch – 2025  

---

## 📜 License

MID License
All rights - Charan Edamalapati
