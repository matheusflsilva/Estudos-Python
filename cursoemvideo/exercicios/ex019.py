from random import choice
alunos = []
for c in range(1, 5):
    a = str(input(f'{c}º aluno: '))
    alunos.append(a)
print(f'O aluno escolhido foi {choice(alunos)}')
