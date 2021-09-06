from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.lang import Builder, builder
from kivy.properties import ObjectProperty
from kivy.core.window import Window

Window.size =(500,700)

#Builder.load_file('calc.kv')

class MyLayout(Widget):
    def clear(self):
        self.ids.calc_input.text = '0'
    # funções de pressionar butões
    def button_press(self, button):
        # variavel para guardar o que esta no input
        prior = self.ids.calc_input.text

        #verificar se zero está no input
        if prior == "0":
            self.ids.calc_input.text = ''
            self.ids.calc_input.text = f'{button}'
        else:
            self.ids.calc_input.text = f'{prior}{button}'
    
    #criando a função de adição

    def add(self):
        # variavel para guardar o que esta no input
        prior = self.ids.calc_input.text
        #colocar o sinal de mais no input text
        self.ids.calc_input.text = f'{prior}+'
    
    # criando a função de subtrair
    def sub(self):
        # variavel para guardar o que esta no input
        prior = self.ids.calc_input.text
        #colocar o sinal de menos no input text
        self.ids.calc_input.text = f'{prior}-'

    # criando a função de multiplicar
    def mult(self):
        # variavel para guardar o que esta no input
        prior = self.ids.calc_input.text
        #colocar o sinal de multiplicar no input text
        self.ids.calc_input.text = f'{prior}*'     

    # criando a função de dividir
    def math_sign(self, sign):
        # variavel para guardar o que esta no input
        prior = self.ids.calc_input.text
        #colocar o sinal de dividir no input text
        self.ids.calc_input.text = f'{prior}{sign}'
    # função para remover o ultimo caracter do text box
    def remove(self):
        prior = self.ids.calc_input.text
        # remove o caracter
        prior = prior[:-1]
        # imprime 
        self.ids.calc_input.text = prior

    # criando a função do ponto decimal
    def dot(self):
        prior = self.ids.calc_input.text
        
        if '.' in prior:
            pass
        else:
            # adcionando um ponto ao final
            prior = f'{prior}.'
        
            # depois colocar de volta no input
            self.ids.calc_input.text = prior

    # criando a função de igual para aparecer os sinais e aparecer o proximo numero
    def igual(self):
        prior = self.ids.calc_input.text
        #adição
        if "+" in prior:
            num_list = prior.split("+")
            answer = 0
            #loop na lista
            for numero in num_list:
                answer = answer + int(numero)
            # colocando o resultado no input
            self.ids.calc_input.text = str(answer)
            
            
        

class calcApp(App):
    def build(self):
        return MyLayout()

if __name__ == '__main__':
    calcApp().run()

