from random import shuffle
lista = []
for c in range(1, 5):
    a = str(input(f'{c}° aluno: '))
    lista.append(a)
shuffle(lista)
print(f'A ordem de apresentação será \n{lista}')
