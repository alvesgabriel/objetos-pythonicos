import operator

alunos = [("Renzo", 0), ("Ada", 10), ("Luciano", 9)]

print("Usando filter")
print([(nome, nota) for nome, nota in alunos if nota > 5])


def possui_nota_maior_que_5(aluno):
    _, nota = aluno
    return nota > 5


print(list(filter(possui_nota_maior_que_5, alunos)))

print("Usando map")
print([nome for nome, nota in alunos if nota > 5])


def extrair_nome(aluno):
    nome, _ = aluno
    return nome


print(list(map(extrair_nome, alunos)))
print(list(map(extrair_nome, filter(possui_nota_maior_que_5, alunos))))

print(list(map(operator.itemgetter(0), filter(possui_nota_maior_que_5, alunos))))
