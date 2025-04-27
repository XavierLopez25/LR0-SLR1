# Computa conjuntos FOLLOW para cada no-terminal usando FIRST y la gramática.

def compute_follow(grammar: dict, FIRST: dict, start_symbol: str) -> dict:
    FOLLOW = {nt: set() for nt in grammar}
    # Marca el inicio con $ en FOLLOW
    FOLLOW[start_symbol].add('$')
    changed = True
    while changed:
        changed = False
        for nt, prods in grammar.items():
            for prod in prods:
                trailer = FOLLOW[nt].copy()
                # Recorre la produccion al revés
                for symbol in reversed(prod):
                    if symbol in grammar:
                        before = FOLLOW[symbol].copy()
                        # agrega trailer
                        FOLLOW[symbol] |= trailer
                        if '#' in FIRST[symbol]:
                            trailer |= (FIRST[symbol] - {'#'})
                        else:
                            trailer = FIRST[symbol].copy()
                        if before != FOLLOW[symbol]:
                            changed = True
                    else:
                        # terminal reinicia trailer
                        trailer = {symbol}
    return FOLLOW