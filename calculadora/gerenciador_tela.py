from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen

class Gerenciador(ScreenManager):
    pass

class Primeira_Tela(Screen):
    pass

class Segunda_Tela(Screen):
    pass

class Terceira_Tela(Screen):
    pass

class Meu_Layout(Widget):
    pass
        
class gerenciador_tela(App):
    def build(self):
        return Gerenciador()

if __name__ == '__main__':
    gerenciador_tela().run()





