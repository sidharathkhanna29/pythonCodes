'''
@Author: Sidharath Khanna
@StudentId: C0901950
@Date: 28/11/2023
@Program: To create a GUI Currency Converter application using Tkinter.
'''

import tkinter as tk

def convert_currency():
    try:
        amount = float(input_value.get())
        if selected_currency.get() == "USD":
            conversion_rate = 0.74
            result = amount * conversion_rate
            sign = '$'
        if selected_currency.get() == "INR":
            conversion_rate = 61.42
            result = amount * conversion_rate
            sign = '₹'
        if selected_currency.get() == "EUR":
            conversion_rate = 0.67
            result = amount * conversion_rate
            sign = '€'
            
        result_label_currency.config(text=f"${amount} CAD is {sign}{result:.2f} {selected_currency.get()}")
    except ValueError:
        result_label_currency.config(text="Invalid input. Please enter a valid number!")


def exit_program():
    window.destroy()


# Window setup
window = tk.Tk()
window.title("Currency Coverter Tool")
window.geometry("600x300")

# Frame setup
top_frame = tk.Frame(window)
top_frame.pack(pady=10, padx=20)

conversion_frame = tk.Frame(window)
conversion_frame.pack(padx=20)

btn_frame = tk.Frame(window)
btn_frame.pack(side='right', pady=10, padx=100)

# User Input area
label = tk.Label(top_frame, text="Enter CAD currency:", font=('arial', 12))
label.pack(side='left')

input_value = tk.Entry(top_frame)
input_value.pack(pady=20)


# Conversion options
selected_currency = tk.StringVar()
conversion_options = ["USD", "INR", "EUR"]
for option in conversion_options:
    tk.Radiobutton(conversion_frame, text=option, variable=selected_currency, value=option).pack()
selected_currency.set(conversion_options[0])


# Buttons
convert_btn = tk.Button(btn_frame, text='Convert', padx='20', bg="red", fg="white", command=convert_currency)
convert_btn.pack(side='left')

exit_btn = tk.Button(btn_frame, text='Exit', padx='20', bg="red", fg="black", command=exit_program)
exit_btn.pack(side='left')


# Result Display
result_label_currency = tk.Label(window, text="", padx='50')
result_label_currency.pack()


# Start the GUI event loop
window.mainloop()