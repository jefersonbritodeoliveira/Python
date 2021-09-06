from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.lang import Builder, builder
from kivy.properties import ObjectProperty
from kivy.core.window import Window

Window.size =(900,900)

#Builder.load_file('calc.kv')

class MyLayout(Widget):
    def apertando(self, button):
        self.ids.bot.text = 'pressionando'
        self.ids.mensagem.text= 'me pressionando'
        
    
    def soltei(self, button):
        self.ids.bot.text = 'soltei'
        self.ids.mensagem.text= 'soltou o botão'

    def escreve(self, button):
        self.ids.saida.text = 'escreveu mesmo'
    
    


class testeApp(App):
    def build(self):
        return MyLayout()

if __name__ == '__main__':
    testeApp().run()

