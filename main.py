# -*- coding: utf-8 -*-
import kivy
from kivy.app import App
from kivy.uix.screenmanager import (ScreenManager,
        Screen, RiseInTransition)
from kivy.uix.button import Button
from kivy.properties import ListProperty
from kivy.properties import NumericProperty, StringProperty
from kivy.core.audio import SoundLoader
from kivy.clock import Clock
#from kivy.core.window import Window
import csv
import random

kivy.require('1.9.1')


class BotonRedondo(Button):
    color_fondo = ListProperty([1, 1, 1, 1])  # Color de fondo, por defecto blanco
    color_texto = ListProperty([0, 0, 0, 1])  # Color del texto, por defecto negro

class MenuScreen(Screen):
    def __init__(self, **kwargs):
        super(MenuScreen, self).__init__(**kwargs)

class Ajustes(Screen):
    def __init__(self, **kwargs):
        super(Ajustes, self).__init__(**kwargs)

    def __init__(self, **kwargs):
        super(Ajustes, self).__init__(**kwargs)

class Application(Screen):
    def __init__(self, **kwargs):
        super(Application, self).__init__(**kwargs)


class Main(App):
    def build(self):
        #Window.maximize()

        sm = ScreenManager(transition=RiseInTransition())
        sm.add_widget(MenuScreen(name='menu'))
        sm.add_widget(Ajustes(name='ajustes'))
        sm.add_widget(Application(name='app'))

        return sm

if __name__ == '__main__':
    Main().run()