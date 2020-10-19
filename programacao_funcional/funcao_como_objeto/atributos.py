from dis import dis


def dobro(x):
    return x * 2


# dobro2 = lambda x: x * 2


for d in dir(dobro):
    print(d)


print(dobro.__name__)
print(dobro.__module__)
print(dobro.__code__)
print(dobro.__code__.co_code)

print("Código da função dobro:")
dis(dobro.__code__.co_code)

dobro.n = 42
print(dobro.n)

print("Atribuindo a função dobro a variavel g:")
g = dobro
print(g)
print(g.__name__)
print(g(21))

# print(dobro.__code__.co_code == dobro2.__code__.co_code)
