#!/usr/bin/env python
import kivy
kivy.require('1.10.0')

from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.config import Config

from blynkapi import Blynk

Config.set('graphics', 'width', '400')
Config.set('graphics', 'height', '100')

class BlynkApp(App):
    _auth_token = "your_token_here"
    _desk_lamp = Blynk(_auth_token, pin="d17")

    def build(self):
        self.title="Smart room application"

        layout = GridLayout(cols=3, row=2)

        desk_lamp_btn_on =  Button(text='Turn On')
        desk_lamp_btn_on.bind(on_press=self.desk_lamp_on)

        desk_lamp_btn_off = Button(text='Turn Off')
        desk_lamp_btn_off.bind(on_press=self.desk_lamp_off)

        layout.add_widget(Label(text="Desk Lamp"))
        layout.add_widget(desk_lamp_btn_on)
        layout.add_widget(desk_lamp_btn_off)

        # layout.add_widget(Label(text="Night Lamp"))
        return layout

    def desk_lamp_on(self, event):
        self._desk_lamp.on()

    def desk_lamp_off(self, event):
        self._desk_lamp.off()

if __name__ == '__main__':
    BlynkApp().run()