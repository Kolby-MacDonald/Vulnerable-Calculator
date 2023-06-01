# --------------------------------------------------------------------------------
# Name: Kolby MacDonald
# Project: Vulnerable Calculator 
# 
# Purpose:
#     Python is not as secure as some may think, eval() demonstrates
# one of pythons biggest security flaws, command injection. SQL
# controllers, system modules, subprocess functions and even some 
# built-in python functions are not secure against command injection. 
# I built this mini-calculator as a demonstration of a programming 
# mistake that could be fatal to a system.
#
#     Another use-case for command injection would be external command
# injection. For example downloading a simple python calculator that
# uses eval() and a hidden socket communication to control your PC 
# remotely. Please understand not only what you are doing with your 
# code, but what others can do with your code as well.
# --------------------------------------------------------------------------------

# Import GUI Module
from PyQt5 import QtWidgets, uic

# Update the GUI everytime a conditional change is made.
def update_screen():
    global input_string, output_string
    gui.input_line_edit.setText(input_string)
    gui.output_line_edit.setText(output_string)

# Update the input string before evaluating an expression.
def confirm_input():
    global input_string
    input_string = gui.input_line_edit.text()

# Determin which button was pressed and respond accrodingly.
def pressed_button(button):
    global input_string, output_string

    # For most buttons, we simply just add their value to the expression.
    if (button in range(10)) or button in ['+', '-', '(', ')', '/', '*', '**']:
        input_string += str(button)

    # sign_button changes the expressions sign.
    elif button == 'sign_button':
        try:
            tempList = list(input_string)
            if tempList[0] == '-' or (tempList[0] == '-' and tempList[1] == '('):
                input_string = '+' + input_string[1:]
            elif tempList[0] == '+' or (tempList[0] == '+' and tempList[1] == '('):
                input_string = '-' + input_string[1:]
            else:
                input_string = '-(' + input_string + ')'
        except:
            pass
    
    # Only add decimals after numbers.
    elif button == ".": #Could be updated to not allow edge cases. (Eg. 8.7.2).
        tempList = list(input_string)
        if tempList[-1] not in ['+', '-', '(', ')', '/', '*', '**', '.']:
            input_string += button

    # If the button is "=" then evaluate the expression.
    elif button == 'evaluate_button':
        confirm_input()
        try: #HERE IS THE SECURITY FLAW - Notice how simple of a mistake this can be.
            output_string = str(eval(input_string)) # One simple oversight can...
            input_string = output_string # Completely control your system.
        except:
            pass
    
    # Percent "%" simply divides by 100 and rounds to two decimal places.
    elif button == 'percent_button':
        try:
            input_string = str(round((float(input_string)/100),2))
            output_string = input_string
        except:
            pass
    
    # Clear all just resets our input and output string.
    elif button == 'clear_all_button':
        input_string = ''
        output_string = ''

    # Clear Input simply resets the input string.
    elif button == 'clear_input_button':
        input_string = ''      

    # Delete last just removes a character from the input string.
    elif button == 'delete_last_button':
        try:
            input_string = input_string[:-1]
        except:
            pass
    
    # When the line-edit is manually edited, updated the input string.
    elif button == 'input_edited':
        confirm_input()

    #After every button press, update the gui accordingly.
    update_screen()

# Holds the current values for input and output to be displayed.
input_string = ''
output_string = ''

# Define the UI and application.
app = QtWidgets.QApplication([])

#gui = uic.loadUi("calculator_vuln_demovid.ui") #Bigger version for demo purposes.
gui = uic.loadUi("calculator_vuln.ui")

# Map buttons to their respective funcions.
gui.input_line_edit.editingFinished.connect(lambda: pressed_button('input_edited'))
gui.sign_button.clicked.connect(lambda: pressed_button('sign_button'))
gui.zero_button.clicked.connect(lambda: pressed_button(0))
gui.decimal_button.clicked.connect(lambda: pressed_button('.'))
gui.evaluate_button.clicked.connect(lambda: pressed_button('evaluate_button'))     
gui.one_button.clicked.connect(lambda: pressed_button(1))     
gui.two_button.clicked.connect(lambda: pressed_button(2))    
gui.three_button.clicked.connect(lambda: pressed_button(3))    
gui.add_button.clicked.connect(lambda: pressed_button('+'))
gui.four_button.clicked.connect(lambda: pressed_button(4))
gui.five_button.clicked.connect(lambda: pressed_button(5)) 
gui.six_button.clicked.connect(lambda: pressed_button(6))    
gui.subtract_button.clicked.connect(lambda: pressed_button('-'))    
gui.seven_button.clicked.connect(lambda: pressed_button(7))
gui.eight_button.clicked.connect(lambda: pressed_button(8))  
gui.nine_button.clicked.connect(lambda: pressed_button(9))
gui.multiply_button.clicked.connect(lambda: pressed_button('*'))
gui.left_bracket_button.clicked.connect(lambda: pressed_button('('))
gui.right_bracket_button.clicked.connect(lambda: pressed_button(')'))
gui.power_button.clicked.connect(lambda: pressed_button('**'))
gui.divide_button.clicked.connect(lambda: pressed_button('/'))
gui.percent_button.clicked.connect(lambda: pressed_button('percent_button'))
gui.clear_all_button.clicked.connect(lambda: pressed_button('clear_all_button'))
gui.clear_input_button.clicked.connect(lambda: pressed_button('clear_input_button'))
gui.delete_last_button.clicked.connect(lambda: pressed_button('delete_last_button'))

gui.show()
app.exec()