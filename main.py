from tkinter import *
from datetime import *

def calculateAge():
    try:
        today = date.today()
        year = int(yearEntry.get())
        month = int(monthEntry.get())
        day = int(dayEntry.get())

      
        if year < 0 or year > today.year:
            raise ValueError("The year cannot be negative or in the future.")
        if month < 1 or month > 12:
            raise ValueError("Month must be between 1 and 12.")
        if day < 1 or (month == 2 and day > 29) or (month in [4, 6, 9, 11] and day > 30) or (month in [1, 3, 5, 7, 8, 10, 12] and day > 31):
            raise ValueError("Invalid day for the given month.")

        birthDate = date(year, month, day)
        age = today.year - birthDate.year - ((today.month, today.day) < (birthDate.month, birthDate.day))

        resultLabel.config(text=f"{nameValue.get()}'s age is {age} years.", fg="green")
    except ValueError as e:
        resultLabel.config(text=f"Error: {str(e)}", fg="red")

root = Tk()
root.geometry("800x600")
root.resizable(False, False)
root.title("Age Calculator")



Label(text="Name", font=("Arial", 20)).place(x=200, y=250)
Label(text="Year", font=("Arial", 20)).place(x=200, y=300)
Label(text="Month", font=("Arial", 20)).place(x=200, y=350)
Label(text="Day", font=("Arial", 20)).place(x=200, y=400)

nameValue = StringVar()
yearValue = StringVar()
monthValue = StringVar()
dayValue = StringVar()

nameEntry = Entry(root, textvariable=nameValue, width=30, font=("Arial", 20))
nameEntry.place(x=300, y=250)

yearEntry = Entry(root, textvariable=yearValue, width=30, font=("Arial", 20))
yearEntry.place(x=300, y=300)

monthEntry = Entry(root, textvariable=monthValue, width=30, font=("Arial", 20))
monthEntry.place(x=300, y=350)

dayEntry = Entry(root, textvariable=dayValue, width=30, font=("Arial", 20))
dayEntry.place(x=300, y=400)

calculate_button = Button(root, text="Calculate Age", font=("Arial", 15), command=calculateAge)
calculate_button.place(x=300, y=450)

resultLabel = Label(root, font=("Arial", 20), bg="#dae6f6")
resultLabel.place(x=300, y=500)

root.mainloop()
