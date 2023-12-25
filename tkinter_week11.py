"""
tkinter --> forms or application

class --> to model your window

"""
'''
import tkinter as tk

class kiloConvertor:
    def _init_(self):
        #------------window-----------
        self.window = tk.Tk()
        self.window.title("kilo Convertor")
        self.window.geometry("500x200")
        #------------Frame(grid)---------

        self.topFrame = tk.Frame(self.window)
        self.btnFrame = tk.Frame(self.window)


        #-----------widget----------------
        self.label = tk.Label(self.topFrame, text ="Enter kg amount: ", font=('serif'))
        self.kiloEntry = tk.Entry(self.topFrame, bg="lightblue")
        self.entryBtn = tk.Button(self.btnFrame, text = 'Enter', padx = '20', bg="lightgreen", fg ="black")
        self.exitBtn = tk.Button(self.btnFrame, text='Exit', padx = "20")

        #--------Packing-----------------
        self.label.pack(side = 'left')
        self.kiloEntry.pack(pady = 20)
        self.topFrame.pack(pady = 10, padx = 20)
        self.entryBtn.pack(side='left')
        self.exitBtn.pack(side="left")
        self.btnFrame.pack(side='right', pady = 10, padx = 100)

        self.window.mainloop()


kiloConvertor()
'''


# without Classes 

import tkinter as tk

def convert_kg():
    try:
        kg = float(kg_entry.get())
        grams = kg * 1000
        result_label.config(text=f"Result: {grams} grams")
    except ValueError:
        result_label.config(text="Please enter a valid number")

def exit_program():
    window.destroy()

# Window setup
window = tk.Tk()
window.title("Kilo Converter")
window.geometry("500x200")

# Frame setup
top_frame = tk.Frame(window)
btn_frame = tk.Frame(window)

# Widgets
label = tk.Label(top_frame, text="Enter kg amount:", font=('serif', 12))
kg_entry = tk.Entry(top_frame, bg="lightblue")
entry_btn = tk.Button(btn_frame, text='Convert', padx='20', bg="lightgreen", fg="black", command=convert_kg)
exit_btn = tk.Button(btn_frame, text='Exit', padx='20', command=exit_program)

# Packing widgets
label.pack(side='left')
kg_entry.pack(pady=20)
top_frame.pack(pady=10, padx=20)
entry_btn.pack(side='left')
exit_btn.pack(side='left')
btn_frame.pack(side='right', pady=10, padx=100)

# Result label
result_label = tk.Label(window, text="")
result_label.pack()

window.mainloop()
