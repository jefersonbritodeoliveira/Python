from kivy.app import App
from kivy.core import text
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.lang import Builder, builder

class Add_tarefas(BoxLayout):
    def __init__(self, tarefas):
        super().__init__()
        for inserido in tarefas:
            self.add_widget(Label(text=inserido))
    
    def adcionando(self, button):
        a = 50
        b = 30
        if a > b:
            print('é maior')


class aulaApp(App):
    def build(self):
        return Add_tarefas(['01','02'])

if __name__ == '__main__':
    aulaApp().run()