# Python program to implement client side of chat room.
import socket
import select
import sys
from details import *

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


server.connect((ip, port))
import kivy
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.core.window import Window

Window.size = (200, 200)


class Main(App):

    def build(self):
        return MyApp()


class MyApp(GridLayout):

    def __init__(self, **kwargs):
        super(MyApp, self).__init__(**kwargs)
        self.cols = 1
        self.button = Button(text='Buzzer', font_size=25)
        self.button.bind(on_press=lambda i: server.send('1'.encode('utf-8')))
        self.add_widget(self.button)


if __name__ == '__main__':
    Main().run()
