alunos = [("Renzo", 0), ("Ada", 10), ("Luciano", 9)]

alunos.sort(key=lambda aluno: aluno[1])

print(alunos)


def aluno_por_nome(aluno):
    return aluno[0]


print(sorted(alunos, key=aluno_por_nome))
