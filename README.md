# Vulnerable-Calculator
Python is not as safe as people believe.

Python is not as secure as some may think, eval() demonstrates one of pythons biggest security flaws, command injection. SQL
controllers, system modules, subprocess functions and even some built-in python functions are not secure against command injection. I built this mini-calculator as a demonstration of a programming mistake that could be fatal to a system.

Another use-case for command injection would be external command injection. For example downloading a simple python calculator that uses eval() and a hidden socket communication to control your PC remotely. Please understand not only what you are doing with your code, but what others can do with your code as well.

--------------------------------------------------------------------------------
Examples To Use in calc_vuln.py:
Use the calculator normally, then attempt the following:
1. __import__('cmdline_loadbar.py').run()
2. __import__('os').system('start cmd')
3. __import__('subprocess').Popen('C:\\Windows\\System32\\calc.exe')
4. __import__('webbrowser').open('https://www.linkedin.com/in/kolby-macdonald/')
--------------------------------------------------------------------------------