distancia = float(input('Qual é a distancia da sua viagem? '))
print(f'Você está prestes a começar uma viagem de {distancia}Km.')
preco = distancia * 0.50 if distancia <= 200 else distancia * 0.45
print(f'E o preço da sua passagem será de R${preco:.2f}')
