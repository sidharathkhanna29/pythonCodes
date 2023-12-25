'''
@Author: Sihdarath Khanna
@Date: 24/12/2023
@Program: To design and implement a Attendance Application for managing student attandance in class.
'''


def menu():
    print("-------------------------")
    print("Attendance Application")
    print("-------------------------")
    print("1. Mark Attendance")
    print("2. View Attendance")
    print("3. Exit")
    print("-------------------------")
    return input("Enter your choice: ")

def main():
    while True:
        choice = menu()
        if choice == '1':
            pass
        elif choice == '2':
            pass
        elif choice == '3':
            print("Thanks for checking in! Goodbye!")
            break
        else:
            print("Bad Input!! Please choose a valid option!")


import tkinter as tk
from tkinter import messagebox
import sqlite3
from datetime import datetime

# Database initialization
conn = sqlite3.connect("attendance.db")
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS attendance
                  (id INTEGER PRIMARY KEY AUTOINCREMENT,
                   student_name TEXT NOT NULL,
                   status TEXT NOT NULL,
                   date TEXT NOT NULL)''')
conn.commit()

class AttendanceApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Attendance Management System")

        # GUI components
        self.label_name = tk.Label(root, text="Student Name:")
        self.entry_name = tk.Entry(root)
        self.label_status = tk.Label(root, text="Status:")
        self.entry_status = tk.Entry(root)

        self.btn_mark_attendance = tk.Button(root, text="Mark Attendance", command=self.mark_attendance)
        self.btn_view_attendance = tk.Button(root, text="View Attendance", command=self.view_attendance)

        # Layout
        self.label_name.grid(row=0, column=0, padx=10, pady=10)
        self.entry_name.grid(row=0, column=1, padx=10, pady=10)
        self.label_status.grid(row=1, column=0, padx=10, pady=10)
        self.entry_status.grid(row=1, column=1, padx=10, pady=10)
        self.btn_mark_attendance.grid(row=2, column=0, columnspan=2, pady=10)
        self.btn_view_attendance.grid(row=3, column=0, columnspan=2, pady=10)

    def mark_attendance(self):
        student_name = self.entry_name.get()
        status = self.entry_status.get()

        if not student_name or not status:
            messagebox.showerror("Error", "Please enter both student name and status.")
            return

        date_today = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        cursor.execute("INSERT INTO attendance (student_name, status, date) VALUES (?, ?, ?)",
                       (student_name, status, date_today))
        conn.commit()

        messagebox.showinfo("Success", f"Attendance marked for {student_name}.")

        # Clear input fields
        self.entry_name.delete(0, tk.END)
        self.entry_status.delete(0, tk.END)

    def view_attendance(self):
        view_window = tk.Toplevel(self.root)
        view_window.title("View Attendance")

        # Display attendance records in a listbox
        listbox = tk.Listbox(view_window, width=50)
        listbox.pack(padx=10, pady=10)

        # Fetch and display records
        cursor.execute("SELECT * FROM attendance")
        records = cursor.fetchall()
        for record in records:
            listbox.insert(tk.END, f"{record[3]} - {record[1]} ({record[2]})")

if __name__ == "__main__":
    root = tk.Tk()
    app = AttendanceApp(root)
    root.mainloop()

# Close the database connection
conn.close()