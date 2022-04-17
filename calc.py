import kivy
kivy.require('2.1.0')
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.core.window import Window


# designate Our .kv desin file
Builder.load_string("""#:kivy 2.1.0
<MyLayout>
    BoxLayout:
        orientation: "vertical"
        size: root.width,root.height

        TextInput:
            id: calc_input
            text: "0"
            halign: "right"
            font_size: 65
            foreground_color: (0, 0.5, 0, 1)
            size_hint: (1,0.15)
        

        GridLayout:
            cols: 4
            rows: 5

            # Row
            Button:
                text: "%"
                font_size: 32
                size_hint:(0.2,0.2)
                color: (0,1,1,1)
                on_press: root.math_sign("%")

            Button:
                text: "c"
                font_size: 32
                size_hint:(0.2,0.2)
                color: (0,1,1,1)
                on_press: root.clear()
            
            Button:
                text: u"\u00AB"
                font_size: 32
                size_hint:(0.2,0.2)
                color: (0,1,1,1)
                on_press: root.remove()
                

            Button:
                text: "/"
                font_size: 32
                size_hint:(0.2,0.2)
                color: (0,1,1,1)
                on_press: root.math_sign("/")

            Button:
                text: "7"
                font_size: 32
                size_hint:(0.2,0.2)
                on_press: root.button_press(7)

            Button:
                text: "8"
                font_size: 32
                size_hint:(0.2,0.2)
                on_press: root.button_press(8)

            Button:
                text: "9"
                font_size: 32
                size_hint:(0.2,0.2)
                on_press: root.button_press(9)

            Button:
                text: "*"
                font_size: 32
                size_hint:(0.2,0.2)
                color: (0,1,1,1)
                on_press: root.math_sign("*")

            Button:
                text: "4"
                font_size: 32
                size_hint:(0.2,0.2)
                on_press: root.button_press(4)

            Button:
                text: "5"
                font_size: 32
                size_hint:(0.2,0.2)
                on_press: root.button_press(5)

            Button:
                text: "6"
                font_size: 32
                size_hint:(0.2,0.2)
                on_press: root.button_press(6)

            Button:
                text: "-"
                font_size: 32
                size_hint:(0.2,0.2)
                color: (0,1,1,1)
                on_press: root.math_sign("-")


            Button:
                text: "1"
                font_size: 32
                size_hint:(0.2,0.2)
                on_press: root.button_press(1)

            Button:
                text: "2"
                font_size: 32
                size_hint:(0.2,0.2)
                on_press: root.button_press(2)

            Button:
                text: "3"
                font_size: 32
                size_hint:(0.2,0.2)
                on_press: root.button_press(3)

            Button:
                text: "+"
                font_size: 32
                size_hint:(0.2,0.2)
                color: (0,1,1,1)
                on_press: root.math_sign("+")

            Button:
                text: "+/-"
                font_size: 32
                size_hint:(0.2,0.2)
                color: (0,1,1,1)
                on_press: root.pos_neg()

            Button:
                text: "0"
                font_size: 32
                size_hint:(0.2,0.2)
                on_press: root.button_press(0)

            Button:
                text: "."
                font_size: 32
                size_hint:(0.2,0.2)
                color: (0,1,1,1)
                on_press: root.dot()

            Button:
                text: "="
                font_size: 32
                size_hint:(0.2,0.2)
                color: (0,1,1,1)
                on_press: root.equals()

            

""")

class MyLayout(Widget):
    # create a clear funtion
    def clear(self):
        self.ids.calc_input.text='0'

    # create a remove funtion
    def remove(self):
        prior=self.ids.calc_input.text
        # remove the last item in the text box
        prior=prior[:-1]
        # output back to the text box
        self.ids.calc_input.text=prior

    # creat a button pressing function
    def button_press(self,button):
        # create a variable that contains window
        prior=self.ids.calc_input.text

        # Test for error first
        if "Error" in prior:
            prior=''

        # determine if 0 is sitting there
        if prior=="0":
            self.ids.calc_input.text=''
            self.ids.calc_input.text=f'{button}'
        else:
            self.ids.calc_input.text=f'{prior}{button}'


    # create a decimal function
    def dot(self):
        prior=self.ids.calc_input.text
        
        if "." in prior and "{sign}" in prior:
            pass
        else:
            # add decimal to the end of text
            prior=f'{prior}.'
            # output back to the text box
            self.ids.calc_input.text=prior

    # create a function to make text box positive or negative
    def pos_neg(self):
        prior=self.ids.calc_input.text
        # Test to see if there's a - sign already
        if "-" in prior:
            self.ids.calc_input.text=f'{prior.replace("-","")}'
        else:
            self.ids.calc_input.text=f'-{prior}'

    # create math_sign function
    def math_sign(self,sign):
        # create a variable that contains window
        prior=self.ids.calc_input.text
        # slap a plus sign to the text
        self.ids.calc_input.text=f'{prior}{sign}'



    def equals(self):
        # create a variable that contains window
        prior=self.ids.calc_input.text
        # error handling
        try:
            # Evaluate the math from the text box
            ans=eval(prior)
            # output the ans
            self.ids.calc_input.text=str(ans)
        except:
            self.ids.calc_input.text="Error"



class CalculatorApp(App):
    def build(self):
        self.icon='calc.png'
        return MyLayout()

if __name__=='__main__':
    CalculatorApp().run()
    