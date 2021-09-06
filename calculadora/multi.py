from types import ClassMethodDescriptorType
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.uix.screenmanager import ScreenManager, Screen

class Gerenciador(ScreenManager):
    pass

class Menu(Screen):
    pass


class Tarefas(Screen):
        def __init__(self, tarefas=[], **kwargs ):
            super().__init__(**kwargs)
            for entrada in tarefas:
                self.ids.box.add_widget(Inserir_Tarefa(text=entrada))
        def addWidget(self):
            texto = self.ids.escreve.text
            self.ids.box.add_widget(Inserir_Tarefa(text=texto))
            self.ids.escreve.text = ''
class Outra_tarefa(Screen):
        def __init__(self, tarefas=[], **kwargs ):
            super().__init__(**kwargs)
        def escrever(self, button):
            print('oi')          

class Inserir_Tarefa(BoxLayout):
        def __init__(self, text='', **kwargs):
            super().__init__(**kwargs)
            self.ids.label.text = text



class multi(App):
    def build(self):
        return Gerenciador()

multi().run()
