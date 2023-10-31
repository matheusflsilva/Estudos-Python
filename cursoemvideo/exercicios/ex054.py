from datetime import date
atual = date.today().year
totmai = 0
totmen = 0
for pess in range(1, 8):
    nasc = int(input(f'Em que ano a {pess}º pessoa nasceu? '))
    idade = atual - nasc
    if idade >= 21:
        totmai += 1
    else:
        totmen += 1
print(f'Ao todo tivemos {totmai} pessoas maiores de idade')
print(f'E também tivemos {totmen} pessoas menores de idade')
