import tkinter as tk
import math

# Class containing methods that create functionality (OOP Approach)
class Calculator:
    def __init__(self):
        self.calculation = ""

    def add_to_calculation(self, symbol):
        self.calculation += str(symbol)
        self.update_entry()
    
    def clear_calculation(self):
        self.calculation = ""
        self.update_entry()
        text_result.delete(1.0, "end")
        text_result.insert(1.0, self.calculation)

    def perform_calculation(self):
        try:
            self.calculation = self.calculation.replace('sin', 'math.sin')
            self.calculation = self.calculation.replace('cos', 'math.cos')
            self.calculation = self.calculation.replace('tan', 'math.tan')
            self.calculation = self.calculation.replace('log', 'math.log10')
            self.calculation = self.calculation.replace('pi', 'math.pi')
            self.calculation = self.calculation.replace('e', 'math.e')
            self.calculation = self.calculation.replace('ln', 'math.log')
            self.calculation = self.calculation.replace('abs', 'math.fabs')
            self.calculation = self.calculation.replace('fct', 'math.factorial')
            result = str(eval(self.calculation))
            text_result.delete(1.0, "end")
            text_result.insert(1.0, result)
        except Exception as e:
            text_result.delete(1.0, "end")
            text_result.insert(1.0, "Error: " + str(e))
                
    def update_entry(self):
        text_enter.delete(1.0, "end")
        text_enter.insert(1.0, self.calculation)


# Create tkinter window and set its dimensions
root = tk.Tk()
calculator = Calculator()
root.geometry("400x550")
root.title("Calculator")

# Create operation and result boxes for calculations
enter_label = tk.Label(root, text="Operation", font=('Arial', 12))
text_enter = tk.Text(root, height=2, font=('Arial', 16))
enter_label.pack(padx=5, pady=5)
text_enter.pack(padx=10, pady=10)

result_label = tk.Label(root, text="Result", font=('Arial', 12))
text_result = tk.Text(root, height=1, font=('Arial', 16))
result_label.pack(padx=5, pady=5)
text_result.pack(padx=10, pady=10)

# Create calculator buttons and add functionality
button_frame = tk.Frame(root)
button_frame.columnconfigure(0, weight=1)
button_frame.columnconfigure(1, weight=1)
button_frame.columnconfigure(2, weight=1)
button_frame.columnconfigure(3, weight=1)

buttonpi = tk.Button(button_frame, text='\u03c0', command=lambda: calculator.add_to_calculation('pi'), font=('Arial', 16))
buttonpi.grid(column=0, row=0, sticky="we")

buttonpoint = tk.Button(button_frame, text='.', command=lambda: calculator.add_to_calculation('.'), font=('Arial', 16))
buttonpoint.grid(column=1, row=0, sticky="we")

buttonleftbkt = tk.Button(button_frame, text='(', command=lambda: calculator.add_to_calculation('('), font=('Arial', 16))
buttonleftbkt.grid(column=2, row=0, sticky="we")

buttonrightbkt = tk.Button(button_frame, text=')', command=lambda: calculator.add_to_calculation(')'), font=('Arial', 16))
buttonrightbkt.grid(column=3, row=0, sticky="we")

buttonsin = tk.Button(button_frame, text='sin', command=lambda: calculator.add_to_calculation('sin'), font=('Arial', 16))
buttonsin.grid(column=0, row=1, sticky="we")

buttoncos = tk.Button(button_frame, text='cos', command=lambda: calculator.add_to_calculation('cos'), font=('Arial', 16))
buttoncos.grid(column=1, row=1, sticky="we")

buttontan = tk.Button(button_frame, text='tan', command=lambda: calculator.add_to_calculation('tan'), font=('Arial', 16))
buttontan.grid(column=2, row=1, sticky="we")

buttonlog = tk.Button(button_frame, text='log', command=lambda: calculator.add_to_calculation('log'), font=('Arial', 16))
buttonlog.grid(column=3, row=1, sticky="we")

buttonabs = tk.Button(button_frame, text='abs', command=lambda: calculator.add_to_calculation('abs'), font=('Arial', 16))
buttonabs.grid(column=0, row=2, sticky="we")

buttonfct = tk.Button(button_frame, text='!', command=lambda: calculator.add_to_calculation('fct'), font=('Arial', 16))
buttonfct.grid(column=1, row=2, sticky="we")

buttoneuler = tk.Button(button_frame, text='e', command=lambda: calculator.add_to_calculation('e'), font=('Arial', 16))
buttoneuler.grid(column=2, row=2, sticky="we")

buttonln = tk.Button(button_frame, text='ln', command=lambda: calculator.add_to_calculation('ln'), font=('Arial', 16))
buttonln.grid(column=3, row=2, sticky="we")

buttonexp = tk.Button(button_frame, text='x\u207f', command=lambda: calculator.add_to_calculation('**'), font=('Arial', 16))
buttonexp.grid(column=0, row=3, sticky="we")

buttonsqrt = tk.Button(button_frame, text='\u221ax', command=lambda: calculator.add_to_calculation('**(1/2)'), font=('Arial', 16))
buttonsqrt.grid(column=1, row=3, sticky="we")

buttoncbrt = tk.Button(button_frame, text='\u00b3\u221ax', command=lambda: calculator.add_to_calculation('**(1/3)'), font=('Arial', 16))
buttoncbrt.grid(column=2, row=3, sticky="we")

buttonmod = tk.Button(button_frame, text='mod', command=lambda: calculator.add_to_calculation('%'), font=('Arial', 16))
buttonmod.grid(column=3, row=3, sticky="we")

button7 = tk.Button(button_frame, text='7', command=lambda: calculator.add_to_calculation(7), font=('Arial', 16))
button7.grid(column=0, row=4, sticky="we")

button8 = tk.Button(button_frame, text='8', command=lambda: calculator.add_to_calculation(8), font=('Arial', 16))
button8.grid(column=1, row=4, sticky="we")

button9 = tk.Button(button_frame, text='9', command=lambda: calculator.add_to_calculation(9), font=('Arial', 16))
button9.grid(column=2, row=4, sticky="we")

buttonplus = tk.Button(button_frame, text='+', command=lambda: calculator.add_to_calculation('+'), font=('Arial', 16))
buttonplus.grid(column=3, row=4, sticky="we")

button4 = tk.Button(button_frame, text='4', command=lambda: calculator.add_to_calculation(4), font=('Arial', 16))
button4.grid(column=0, row=5, sticky="we")

button5 = tk.Button(button_frame, text='5', command=lambda: calculator.add_to_calculation(5), font=('Arial', 16))
button5.grid(column=1, row=5, sticky="we")

button6 = tk.Button(button_frame, text='6', command=lambda: calculator.add_to_calculation(6), font=('Arial', 16))
button6.grid(column=2, row=5, sticky="we")

buttonminus = tk.Button(button_frame, text='-', command=lambda: calculator.add_to_calculation('-'), font=('Arial', 16))
buttonminus.grid(column=3, row=5, sticky="we")

button1 = tk.Button(button_frame, text='1', command=lambda: calculator.add_to_calculation(1), font=('Arial', 16))
button1.grid(column=0, row=6, sticky="we")

button2 = tk.Button(button_frame, text='2', command=lambda: calculator.add_to_calculation(2), font=('Arial', 16))
button2.grid(column=1, row=6, sticky="we")

button3 = tk.Button(button_frame, text='3', command=lambda: calculator.add_to_calculation(3), font=('Arial', 16))
button3.grid(column=2, row=6, sticky="we")

buttontimes = tk.Button(button_frame, text='*', command=lambda: calculator.add_to_calculation('*'), font=('Arial', 16))
buttontimes.grid(column=3, row=6, sticky="we")

buttonclr = tk.Button(button_frame, text='CLR', command= lambda: calculator.clear_calculation(), font=('Arial', 16))
buttonclr.grid(column=0, row=7, sticky="we")

button0 = tk.Button(button_frame, text='0', command=lambda: calculator.add_to_calculation(0), font=('Arial', 16))
button0.grid(column=1, row=7, sticky="we")

buttonequals = tk.Button(button_frame, text='=', command=lambda: calculator.perform_calculation() ,font=('Arial', 16))
buttonequals.grid(column=2, row=7, sticky="we")

buttondivide = tk.Button(button_frame, text='/', command=lambda: calculator.add_to_calculation('/'), font=('Arial', 16))
buttondivide.grid(column=3, row=7, sticky="we")

button_frame.pack(fill='x', pady=10)
root.mainloop()