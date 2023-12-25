"""
@Author: Sidharath Khanna
@Date: 28/11/2023
@Program: Unit Conversion tool using Tkinter.
"""

import tkinter as tk

def unit_converter():
    try:
        value = float(input_value.get())
        if selected_conversion.get() == "Celsius to Fahrenheit":
            result = (value * 9 / 5) + 32
        elif selected_conversion.get() == "Fahrenheit to Celsius":
            result = (value - 32) * 5 / 9
        elif selected_conversion.get() == "Kilometers to Miles":
            result = value * 0.621371
        elif selected_conversion.get() == "Miles to Kilometers":
            result = value * 1.60934
        result_label.config(text=f"Result: {result:.2f}")
    except ValueError:
        result_label.config(text="Please enter a valid number")


def exit_program():
    window.destroy()


# Window setup
window = tk.Tk()
window.title("Unit Conversion Tool")
window.geometry("500x300")

# Frame setup
top_frame = tk.Frame(window)
conversion_frame = tk.Frame(window)
btn_frame = tk.Frame(window)

# Input area
label = tk.Label(top_frame, text="Enter Value:", font=('arial', 14))
input_value = tk.Entry(top_frame)
label.pack(side='left')
input_value.pack(pady=20)
top_frame.pack(pady=10, padx=20)

# Conversion options
selected_conversion = tk.StringVar()
conversion_options = ["Celsius to Fahrenheit", "Fahrenheit to Celsius", "Kilometers to Miles", "Miles to Kilometers"]
for option in conversion_options:
    tk.Radiobutton(conversion_frame, text=option, variable=selected_conversion, value=option).pack(anchor='w')
selected_conversion.set(conversion_options[0])
conversion_frame.pack(padx=20)

# Buttons
convert_btn = tk.Button(btn_frame, text='Convert', padx='20', bg="lightgreen", fg="black", command=unit_converter)
exit_btn = tk.Button(btn_frame, text='Exit', padx='20', bg="red", fg="white", command=exit_program)
convert_btn.pack(side='left')
exit_btn.pack(side='left')
btn_frame.pack(side='right', pady=10, padx=100)

# Result label
result_label = tk.Label(window, text="")
result_label.pack()

window.mainloop()