import kivy
kivy.require("1.11.1")

from kivy.app import App
from kivy.uix.label import Label

class WineApp(App):
    def build(self):
        return Label(text="Have a wine")

if __name__ == "__main__":
    WineApp().run()
