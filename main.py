from tkinter import *
from datetime import *

root = Tk()
root.geometry("800x600")
root.resizable(False, False)
root.title("Age Calculator")


Label(text="Name", font=23).place(x=200, y=250)
Label(text="Year", font=23).place(x=200, y=300)
Label(text="Month", font=23).place(x=200, y=350)
Label(text="Day", font=23).place(x=200, y=400)

nameValue = StringVar()
yearValue = StringVar()
monthValue = StringVar()
dayValue = StringVar()

nameEntry = Entry(root, textvariable=nameValue, width=30)
nameEntry.place(x=300, y=250)

yearEntry = Entry(root, textvariable=yearValue, width=30)
yearEntry.place(x=300, y=300)

monthEntry = Entry(root, textvariable=monthValue, width=30)
monthEntry.place(x=300, y=350)

dayEntry = Entry(root, textvariable=dayValue, width=30)
dayEntry.place(x=300, y=400)

root.mainloop()
