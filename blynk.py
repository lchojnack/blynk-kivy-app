#!/usr/bin/env python
import kivy
kivy.require('1.10.0')

from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.config import Config

from kivy.network.urlrequest import UrlRequest
from urllib2 import Request, urlopen

Config.set('graphics', 'width', '400')
Config.set('graphics', 'height', '100')

class BlynkApp(App):
    _desk_lamp_token = "your_token"
    _desk_lamp_pin = "V1"

    def build(self):
        self.title="Smart room application"

        layout = GridLayout(cols=3, row=2)

        desk_lamp_btn_on =  Button(text='Turn On')
        desk_lamp_btn_on.bind(on_press=self.desk_lamp_on)

        desk_lamp_btn_off = Button(text='Turn Off')
        desk_lamp_btn_off.bind(on_press=self.desk_lamp_off)

        value = self.blynk_get(self._desk_lamp_token, self._desk_lamp_pin)
        self.desk_lamp_label = Label(text="Desk Lamp\nis {}".format(value),
                                     halign="center"
                                     )
        layout.add_widget(self.desk_lamp_label)
        layout.add_widget(desk_lamp_btn_on)
        layout.add_widget(desk_lamp_btn_off)


        # night_lamp_btn_on =  Button(text='Turn On')
        # night_lamp_btn_on.bind(on_press=self.night_lamp_on)
        #
        # night_lamp_btn_off = Button(text='Turn Off')
        # night_lamp_btn_off.bind(on_press=self.night_lamp_off)
        #
        # layout.add_widget(Label(text="Night Lamp"))
        # layout.add_widget(night_lamp_btn_on)
        # layout.add_widget(night_lamp_btn_off)

        return layout

    def blynk_update(self, token, pin, value):
        url = r"http://blynk-cloud.com/{}/update/{}?value={}".format(token, pin, value)
        request = UrlRequest(url)
        request.wait()
        # request = Request(url)

    def blynk_get(self, token, pin):
        url = r"http://blynk-cloud.com/{}/get/{}".format(token, pin)
        request = Request(url)
        response_body = urlopen(request).read()
        if "1" in response_body:
            return "On"
        else:
            return "Off"

    def desk_lamp_on(self, event):
        self.blynk_update(self._desk_lamp_token, self._desk_lamp_pin, 1)
        value = self.blynk_get(self._desk_lamp_token, self._desk_lamp_pin)
        self.desk_lamp_label.text = "Desk Lamp\nis {}".format(value)

    def desk_lamp_off(self, event):
        self.blynk_update(self._desk_lamp_token, self._desk_lamp_pin, 0)
        value = self.blynk_get(self._desk_lamp_token, self._desk_lamp_pin)
        self.desk_lamp_label.text = "Desk Lamp\nis {}".format(value)

    # def night_lamp_on(self, event):
    #     pass
    #
    # def night_lamp_off(self, event):
    #     pass

if __name__ == '__main__':
    BlynkApp().run()
