from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.screen import MDScreen
from kivy.core.window import Window
from kivy.uix.scrollview import ScrollView
Window.size = (400, 700)


class ForgotPage(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class ForgotpageApp(MDApp):

    def build(self):
        return ForgotPage()


if __name__ == '__main__':
    ForgotpageApp().run()
