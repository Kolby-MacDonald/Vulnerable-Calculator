# Vulnerable-Calculator

Python is not as secure as some may think,
It's built in eval() function demonstrates one of pythons biggest security flaws, command injection. SQL controllers, system modules, subprocess functions and even some built-in python functions are not secure against command injection. I built this mini-calculator as a demonstration of a programming mistake that could be fatal to a system.

Another use-case for command injection would be external command injection. For example downloading a simple python calculator that uses eval() and a hidden socket communication to control your PC remotely. If that python program was put through PyInstaller and became an executable, it would be rather hard to reverse engineer in a program like ghidra. Please understand not only what you are doing with your code, but what others can do with your code as well.

-----------------------------------------------------------------------------------------------------------------

Examples To Use in calc_vuln.py:

- Use the calculator normally, then attempt the following:

1. Python Injection: print('This shouldn't display anything')
2. Script Injection: __import__('cmdline_loadbar.py').run()
3. Command Line Injection: __import__('os').system('start cmd')
4. Process Control: __import__('subprocess').Popen('C:\\Windows\\System32\\calc.exe')
5. Web Control: __import__('webbrowser').open('https://www.linkedin.com/in/kolby-macdonald/')

The above examples demonstrate how giving users control of certain modules
can become incredibly dangerous. Note: We will look at SQLi in a later project

-----------------------------------------------------------------------------------------------------------------