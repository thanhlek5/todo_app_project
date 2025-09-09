from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.screen import Screen
from kivymd.uix.button import MDFillRoundFlatButton
from kivy.core.window import Window
from kivymd.uix.toolbar import MDTopAppBar
Window.size = (360, 640)


class TestApp(MDApp):
    def build(self):
        self.icon = 'logo1-removebg-preview.png'
        self.title = 'Test App'
        screen = Screen()
        self.theme_cls.theme_style = "Dark"
        LoginBox = Builder.load_file('login.kv')
        #MainScreen = Builder.load_file('MainScreen.kv')
        screen.add_widget(LoginBox)
        #screen.add_widget(MainScreen)
        return screen

TestApp().run()