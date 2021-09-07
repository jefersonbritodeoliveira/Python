def calcular(*args):
    r = sum(args)
    for indice in args:
        r += indice
    return r

def diminuir (a,b):
    resultado= a-b
    return resultado + 25


print(calcular(264,4,5))
print(diminuir(4,20))
print(diminuir(5,52))
print(calcular(4,1))
print(calcular(4,666))





