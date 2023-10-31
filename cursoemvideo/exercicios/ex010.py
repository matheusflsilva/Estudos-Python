dinheiro = float(input('Quando dinheiro você tem na carteira? R$'))
print(f'Com R${dinheiro:.2f} você pode comprar US${dinheiro / 5.05:.2f}') # dolar
print(f'Com R${dinheiro:.2f} você pode comprar €{dinheiro / 5.31:.2f}') # euro
print(f'Com R${dinheiro:.2f} você pode comprar {dinheiro / 0.014:.2f} ARS') # peso argentino
print(f'Com R${dinheiro:.2f} você pode comprar {dinheiro / 0.0012:.2f} COP') # peso colombiano
print(f'Com R${dinheiro:.2f} você pode comprar {dinheiro / 0.28:.2f} MXN') # peso mexicano
