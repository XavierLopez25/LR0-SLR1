# Script principal que lee gramática, calcula FIRST y FOLLOW e imprime resultados.

import sys
from grammar_reader import read_grammar
from first import compute_first
from follow import compute_follow

def main():
    if len(sys.argv) != 2:
        print("Uso: python main.py <archivo_gramatica>")
        sys.exit(1)
    archivo = sys.argv[1]
    grammar = read_grammar(archivo)
    # Primer no-terminal definido como start
    start_symbol = list(grammar.keys())[0]
    FIRST = compute_first(grammar)
    FOLLOW = compute_follow(grammar, FIRST, start_symbol)

    print("FIRST sets:")
    for nt, s in FIRST.items():
        print(f"{nt}: {{ {', '.join(sorted(s))} }}")

    print("\nFOLLOW sets:")
    for nt, s in FOLLOW.items():
        print(f"{nt}: {{ {', '.join(sorted(s))} }}")

if __name__ == "__main__":
    main()
