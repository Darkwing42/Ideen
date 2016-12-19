from kivy.app import App
from kivy.uix.accordion import Accordion, AccordionItem
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.properties import ObjectProperty
from kivy.uix.gridlayout import GridLayout
from kivy.core.window import Window
from kivy.uix.popup import Popup
from kivy.uix.button import Button
from kivy.uix.label import Label
import os.path
import DatabaseConnection
import sys
import json

class LoginScreen(Screen):
    username = ObjectProperty()
    password = ObjectProperty()
    login_button = ObjectProperty()
    Window.size = (500, 120)


    def __init__(self, **kwargs):
        super(LoginScreen, self).__init__(**kwargs)
        self.dbu = DatabaseConnection.MySqlConnection()

    def ErrorPopup(Popup):
        content = Label(text='Username/Passwort falsch!'), Button(text='Close me!')
        popup = Popup(title='Login ERROR!', content=content, auto_dismiss=False)
        content.bind(on_press=popup.dismiss)
        popup.open()



    def AttemptLogin(self, *args):
        test = self.dbu.CheckUserLogin(self.username.text, self.password.text)
        print(test)
        if test == True:
            self.parent.current = 'main'



class MainScreen(Screen):
    pass

class Registrierung(Screen):

    registrierung_username = ObjectProperty()
    registrierung_password = ObjectProperty()

    def __init__(self, **kwargs):
        super(Registrierung, self).__init__(**kwargs)
        self.dbu = DatabaseConnection.MySqlConnection()



class Manager(ScreenManager):
    login_screen = ObjectProperty()
    main_screen = ObjectProperty()
    registrierung = ObjectProperty()

class DatabaseScreen(GridLayout):

    Window.size = (640, 200)

    username = ObjectProperty()
    password = ObjectProperty()
    host = ObjectProperty()
    database = ObjectProperty()

    def json_creation(self, *args):
        database_data = {}
        database_data['limsdb'] = {'username': self.username.text,
                                    'passwd': self.password.text,
                                   'host': self.host.text,
                                   'database': self.database.text}
        s = json.dumps(database_data)
        with open('/home/darkwing/database.json', '+w') as f:
            f.write(s)
    def __del__(self):
        sys.exit()

class DatabaseTestApp(App):
    def build(self):
        return DatabaseScreen()

class TestApp(App):
    def __init__(self, **kwargs):
        super(TestApp, self).__init__(**kwargs)


    def build(self):
        return Manager()


if __name__ == '__main__':
    if not os.path.isfile('/home/darkwing/database.json'):
        DatabaseTestApp().run()
    else:
        TestApp().run()
