import kivy
from kivy.app import App
from kivy.uix.label import Label            #track what you ll need and import them seperatly :(
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput    #notice how the class names are always Capitalized.
from kivy.uix.button import Button

class MyGridLayout(GridLayout):             ##inherits from GridLayout.
    #initialize infinite keywords
    def __init__(self, **kwargs):
        #Call the layout constructor        #recall OOP basics.
        super(MyGridLayout, self).__init__(**kwargs)

        #Set columns
        self.cols = 2                           #this will all make sense later on.

        #Add widgets
        self.add_widget(Label(text = 'Name: ')) #the way we add widgets. Every 'element' is a widget.
        #Add input Box
        self.name = TextInput(multiline = False)#here we ll do it as a 2-step process since there is more lines of code.
        self.add_widget(self.name)

        self.add_widget(Label(text = 'Favorite number: '))
        #Add input Box
        self.number = TextInput(multiline = True)
        self.add_widget(self.number)

        self.add_widget(Label(text = 'Favorite Color: '))
        #Add input Box
        self.color = TextInput(multiline = False)
        self.add_widget(self.color)

        #create a submit-button
        self.submit = Button(text = 'Submit', font_size = 32)
        self.submit.bind(on_press = self.press) #ofc you could have done this in one line. Also define the function outside of init!
        self.add_widget(self.submit)            #notice how the button is limited to the 1st column... We ll solve that later on.

    def press(self, instance):                  #when we bind something we need to pass an 'instance' similar to tkinter and events.
        name = self.name.text
        number = self.number.text
        color = self.color.text
        #display to the app
        self.add_widget(Label(text='Hello {}, your favorite number is {} and your favorite color is {}'.format(name,number,color)))

        #Clear the boxes so the user can type again.
        self.name.text = ''
        self.number.text = ''
        self.color.text = ''


class MyApp(App):
    def build(self):
        return MyGridLayout()                   #Now I ll return the entire 'MyGridLayout'
if __name__ == '__main__':
    MyApp().run()                               #notice again how eberything moves together. (dynamically resize)