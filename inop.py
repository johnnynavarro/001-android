from kivy.uix.floatlayout import FloatLayout
from kivymd.app import MDApp
from kivy.lang.builder import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.theming import ThemeManager
from kivy.properties import StringProperty
from kivy.properties import ObjectProperty
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.app import runTouchApp
import csv
# resposta = []
# ler = open("resultado.csv", "r")
# resposta = ler.readlines()
# ler.close()
from kivymd.uix.selectioncontrol import MDCheckbox


class Tela1(Screen):
    prefeito = StringProperty()
    def imprimir(self):
        print("candidato:".join([self.prefeito]))
    def __init__(self,tela1=[],**kwargs):
        super().__init__(**kwargs)
        for i in tela1:
            self.ids.texto.add_widget(Tela1(text=i))
    # pass
class Tela2(Screen):
    pass


class Tela3(Screen):
    pass


class Tela4(Screen):
    pass

class Tela5(Screen):
    pass


class Tela6(Screen):
    pass


class Tela7(Screen):
    pass


# Create the screen manager
sm = ScreenManager()
sm.add_widget(Tela1(name='tela1'))
sm.add_widget(Tela2(name='tela2'))
sm.add_widget(Tela3(name='tela3'))
sm.add_widget(Tela4(name='tela4'))
sm.add_widget(Tela5(name='tela5'))
sm.add_widget(Tela6(name='tela6'))
sm.add_widget(Tela7(name='tela7'))

class InopApp(MDApp):

    def build(self):
        screen = Builder.load_file('android.kv')
        # Um teste do scroolview


        return screen


InopApp().run()
