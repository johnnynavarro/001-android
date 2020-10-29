from kivymd.app import MDApp
from kivy.lang.builder import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.theming import ThemeManager

class Tela1(Screen):
    pass


class Tela2(Screen):
    pass


class Tela3(Screen):
    pass


# Create the screen manager
sm = ScreenManager()
sm.add_widget(Tela1(name='tela1'))
sm.add_widget(Tela2(name='tela2'))
sm.add_widget(Tela3(name='tela3'))


class DemoApp(MDApp):

    def build(self):
        screen = Builder.load_file('android.kv')
        return screen


DemoApp().run()
