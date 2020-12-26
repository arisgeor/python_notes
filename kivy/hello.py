#my first kivy file!

import kivy
from kivy.app import App
from kivy.uix.label import Label    #we need to import all individual things

class MyApp(App):
    def build(self):
        return Label(text = 'Hello World')

if __name__ == '__main__':
    MyApp().run()                   #carefull here! You need () on MyApp as well!