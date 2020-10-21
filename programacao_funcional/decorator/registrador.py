_marcadas = []


def marcar(f):
    _marcadas.append(f)
    return f


def get_marcadas():
    return _marcadas
