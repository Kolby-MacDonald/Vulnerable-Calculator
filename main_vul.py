from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QMessageBox, QLineEdit

input_string = ''
output_string = ''

def update_screen():
    global input_string, output_string
    gui.input_line_edit.setText(input_string)
    gui.output_line_edit.setText(output_string)

def confirm_input():
    global input_string
    input_string = gui.input_line_edit.text()

def pressed_button(button):
    global input_string, output_string

    if (button in range(10)) or button in ['+', '-', '(', ')', '/', '*', '**']:
        input_string += str(button)

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
    
    elif button == ".":
        tempList = list(input_string)
        if tempList[-1] not in ['+', '-', '(', ')', '/', '*', '**', '.']:
            input_string += button

    
    elif button == 'evaluate_button':
        confirm_input()
        try:
            output_string = str(eval(input_string))
            input_string = output_string
        except:
            pass
    
    elif button == 'percent_button':
        try:
            input_string = str(round((float(input_string)/100),2))
            output_string = input_string
        except:
            pass

    elif button == 'clear_all_button':
        input_string = ''
        output_string = ''

    elif button == 'clear_input_button':
        input_string = ''      

    elif button == 'delete_last_button':
        try:
            input_string = input_string[:-1]
        except:
            pass
    
    elif button == 'input_edited':
        confirm_input()

    update_screen()

app = QtWidgets.QApplication([])
gui = uic.loadUi(r'C:\Users\deadb\Desktop\vulns\calc_vuln\calculator_vuln.ui')

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