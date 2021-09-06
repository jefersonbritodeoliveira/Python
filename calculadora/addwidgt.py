from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView



class Tarefas(BoxLayout):
        def __init__(self, tarefas, **kwargs ):
            super().__init__(**kwargs)
            for tarefa in tarefas:
                self.ids.box.add_widget(Tarefa(text=tarefa))
        def addWidget(self):
            texto = self.ids.escreve.text
            self.ids.box.add_widget(Tarefa(text=texto))
            self.ids.escreve.text = ''
          


class Tarefa(BoxLayout):
        def __init__(self, text='', **kwargs):
            super().__init__(**kwargs)
            self.ids.label.text = text

class addwidgt(App):
    def build(self):
        return Tarefas([])

addwidgt().run()
