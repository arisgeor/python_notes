#kivy doesnt have colspan like Tkinter or other libraries.
#however you get what some may consider an even better practice, 
#much similar to traditional App Development.
#You will embed grids on grids.

import kivy
from kivy.app import App
from kivy.uix.label import Label            
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput    
from kivy.uix.button import Button

class MyGridLayout(GridLayout):   

    def __init__(self, **kwargs):
        
        super(MyGridLayout, self).__init__(**kwargs)

        #Set columns
        self.cols = 1                           #first do this 

        ####
        self.top_grid = GridLayout()            #and thats all there is to it! Now I can just call self.topgrid. instead of self. when adding widgets.
        self.top_grid.cols = 2

        #Add widgets
        self.top_grid.add_widget(Label(text = 'Name: ')) 
        #Add input Box
        self.name = TextInput(multiline = False)  #no need to put .top_grid. here. dont get confused!
        self.top_grid.add_widget(self.name)

        self.top_grid.add_widget(Label(text = 'Favorite number: '))
        #Add input Box
        self.number = TextInput(multiline = True)
        self.top_grid.add_widget(self.number)

        self.top_grid.add_widget(Label(text = 'Favorite Color: '))
        #Add input Box
        self.color = TextInput(multiline = False)
        self.top_grid.add_widget(self.color)

        #after I am done with the top grid, I need to add it to the main one, because this is a widget too after all!
        self.add_widget(self.top_grid)
        ####

        #create a submit-button                             #leave the button alone!
        self.submit = Button(text = 'Submit', font_size = 32)
        self.submit.bind(on_press = self.press) 
        self.add_widget(self.submit)            

    def press(self, instance):                  
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