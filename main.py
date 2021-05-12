# --[Start platform specific code]
"""This code to detect it's Android or not
if it's not android than app window size change in android phone size"""
from kivy.utils import platform

if platform != 'android':
    from kivy.config import Config

    Config.set("graphics", "width", 360)
    Config.set("graphics", "height", 740)
# --[End platform specific code]

# --[Start Soft_Keyboard code ]
"""code for android keyboard. when in android keyboard show textbox 
automatic go to top of keyboard so user can see when he type msg"""
from kivy.core.window import Window
Window.size = (400, 700)

Window.keyboard_anim_args = {"d": .2, "t": "linear"}
Window.softinput_mode = "below_target"
# --[End Soft_Keyboard code ]

from pages.startpage.startpage import StartPage
from pages.homepage.homepage import HomePage
from pages.messagepage.messagepage import MessagePage
from pages.profilepage.profilepage import ProfilePage
from pages.manualpage.manualpage import ManualPage
from pages.loginpage.loginpage import LoginPage
from pages.signuppage.signuppage import SignupPage
from pages.forgotpage.forgotpage import ForgotPage
from pages.verificationpage.verificationpage import VerificationPage
from pages.root.root import Root
from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen, ScreenManager


class MyApp(MDApp):
    """
    App start from here this class is root of app.
    in kivy (.kv) file when use app.method_name app is start from here
    """

    def __init__(self, **kwargs):
        super(MyApp, self).__init__(**kwargs)

        self.APP_NAME = "Wound Butler"
        self.COMPANY_NAME = "WoundButler.org"

    def build(self):
        """
        This method call before on_start() method so anything
        that need before start application all other method and code
        write here.
        """
        self.icon = "appimage/ckt.jpg"
        self.theme_cls.primary_palette = "Blue"
        self.theme_cls.primary_hue = "500"

        self.theme_cls.accent_palette = "Amber"
        self.theme_cls.accent_hue = "500"

        self.theme_cls.theme_style = "Light"

        self.load_kv("pages/homepage/homepage.kv")
        self.load_kv("pages/profilepage/profilepage.kv")
        self.load_kv("pages/startpage/startpage.kv")
        self.load_kv("pages/messagepage/messagepage.kv")
        self.load_kv("pages/manualpage/manualpage.kv")
        self.load_kv("pages/loginpage/loginpage.kv")
        self.load_kv("pages/signuppage/signuppage.kv")
        self.load_kv("pages/forgotpage/forgetpage.kv")
        self.load_kv("pages/verificationpage/verificationpage.kv")

        self.screen_manager = Root()
        self.screen_manager.add_widget(HomePage(name="home"))
        self.screen_manager.add_widget(StartPage(name="start"))
        self.screen_manager.add_widget(MessagePage(name='message'))
        self.screen_manager.add_widget(ProfilePage(name="profile"))
        self.screen_manager.add_widget(ManualPage(name="manual"))
        self.screen_manager.add_widget(LoginPage(name="login"))
        self.screen_manager.add_widget(SignupPage(name="signup"))
        self.screen_manager.add_widget(ForgotPage(name="forgot"))
        self.screen_manager.add_widget(VerificationPage(name="verification"))

        return self.screen_manager

    def on_start(self):
        """
        Anything we want to run when start application that code is here.
        """
        self.screen_manager.change_screen("login")


if __name__ == "__main__":
    # Start application from here.
    recite_app = MyApp()
    # Set title
    recite_app.title = 'Wound Butler'
    recite_app.run()
