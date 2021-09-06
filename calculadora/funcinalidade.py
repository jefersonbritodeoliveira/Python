'''
class Carro():
    def __init__(self, *dados ):
        self.dados = dados
        

    def caracteristica(self):
        print(f'Minha cor é {self.dados}')

       

carrovermelho = Carro('vermelho','verde')
carrovermelho.caracteristica()

def filmes_favoritos(nome, *filmes):
    print(f'Os filmes favoritos de {nome}:')
    for i, filmes in enumerate(filmes, start=1): 
        print(f'\t{i}. {filmes}')


filmes_favoritos('jel', 'dracula', 'rua do medo', 'star wars')
'''
'''def chaves(**diciona):
    for key, value in diciona.items():
        print(f'{key} tem {value} anos')

print(chaves(berlim=3, rose= 40, jel = 46, vera=69 ))

perfil={'nome':'jel', 'idade':46}
perfil2={'nome':'jel', 'idade':46, 'idade':49}

def f(**kwargs):
    for key, value in kwargs.items():
        print(key, value)

print(f(**perfil))
print(f(**perfil2))

nomes = ['jel','rose', 'belim','mainha']
primeiro, *restante = nomes

print(nomes)
print(primeiro)
print(restante)
'''
class uppe(object):
    def __init__(self, f):
        self.f = f
    def __call__(self,*args):
        self.f(args[0].upper())
@uppe
def nome(nome):
    print({nome})

print(nome('jeferson brito'))
        

