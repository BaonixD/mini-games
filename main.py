from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout

#55

class Container (BoxLayout):
    pass


class MyApp (App):
    def build (self):
        return Container()
    
    
if __name__ == '__main__':
    MyApp().run()
    