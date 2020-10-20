def fabrica_de_multiplicadores():
    def dobro(n):
        return n * 2

    return dobro


dobro_externo = fabrica_de_multiplicadores()

print(dobro_externo(2))
