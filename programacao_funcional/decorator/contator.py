_contador = 0


def fabrica_de_contador():
    def contar():
        # nonlocal _contador
        global _contador
        _contador += 1
        return _contador

    return contar


contador1 = fabrica_de_contador()
contador2 = fabrica_de_contador()

print("contador1")
print(contador1())
print(contador1())
print(contador1())

print("contador2")
print(contador2())
print(contador2())
