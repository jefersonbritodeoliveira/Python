from random import randint


sorteio = []
contador = 1

while contador <= 6:
    numero = randint(1,60)
    if not numero in sorteio:
        sorteio.append(numero)
        contador += 1
        
print(sorted(sorteio))

'''
 ganhei = [random.randint(1,6), random.randint(1,6),random.randint(1,6), random.randint(1,6),random.randint(1,6), random.randint(1,6)]
        ganhei = tuple(ganhei)
        '''