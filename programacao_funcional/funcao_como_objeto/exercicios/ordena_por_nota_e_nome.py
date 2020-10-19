"""
Construa uma função de ordenação que ordene os alunos por nota. Se houver empate em nota o nome 
deverá definir a ordem

>>> alunos = [('Renzo', 0), ('Luciano', 10), ('Ada Lovelace', 10), ('Ada L', 10), ('Ada King', 10)]
>>> alunos.sort(key=ordena_por_nota_e_nome)
>>> alunos
[('Renzo', 0), ('Ada King', 10), ('Ada L', 10), ('Ada Lovelace', 10), ('Luciano', 10)]
"""


def ordena_por_nota_e_nome(aluno):
    nome, nota = aluno
    return nota, nome
