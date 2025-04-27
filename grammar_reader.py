def read_grammar(file_path: str) -> dict:
    grammar = {}
    current_head = None

    with open(file_path, 'r', encoding='utf-8') as f:
        for raw in f:
            line = raw.strip()
            if not line or line.startswith('#'):
                continue

            # Si contiene '->', se arranca una nueva cabecera
            if '->' in line:
                head, bodies = line.split('->', 1)
                head = head.strip()
                current_head = head
            # Si empieza con '|', es continuación de la última cabecera
            elif line.startswith('|'):
                if current_head is None:
                    raise ValueError(f"Línea de alternativa sin cabecera previa: {raw!r}")
                head = current_head
                bodies = line.lstrip('|').strip()
            else:
                # Ni comentario, ni producción válida → saltamos
                continue

            # Parseamos las alternativas separadas por '|'
            prods = [b.strip().split() for b in bodies.split('|')]
            grammar.setdefault(head, []).extend(prods)

    return grammar
