# Computa conjuntos FIRST para cada no-terminal de la gramática.

def compute_first(grammar: dict) -> dict:
    FIRST = {nt: set() for nt in grammar}
    changed = True
    while changed:
        changed = False
        for nt, prods in grammar.items():
            for prod in prods:
                before = FIRST[nt].copy()
                # Caso epsilon (#)
                if prod == ['#']:
                    FIRST[nt].add('#')
                else:
                    # Si la producción contiene símbolos, se procesan uno por uno en orden.
                    for symbol in prod:
                        if symbol not in grammar:
                            # Si el símbolo no está en la gramática (es un terminal), se agrega directamente al conjunto FIRST del no terminal y se detiene el procesamiento de la producción.
                            FIRST[nt].add(symbol)
                            break
                        # Si el símbolo es un no terminal, se agrega al conjunto FIRST del no terminal actual todo el conjunto FIRST del símbolo, excepto # (epsilon).
                        FIRST[nt] |= (FIRST[symbol] - {'#'})
                        if '#' in FIRST[symbol]:
                            # Se continúa al siguiente símbolo
                            continue
                        else:
                            break
                    else:
                        # Si todos los símbolos de la producción pueden derivar epsilon, se agrega # al conjunto FIRST del no terminal.
                        FIRST[nt].add('#')
                if before != FIRST[nt]:
                    changed = True
    return FIRST