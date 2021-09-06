def n1(a):
    a = a + 11
    return a


def n2(n1):
    n3 = n1 + 5
    return n3


resposta = n1(n2(2))
print(resposta)



