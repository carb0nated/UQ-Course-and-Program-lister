from tkinter import *


root = Tk()
root.geometry("900x700")
root.title('The Unofficial UQ Program Planner')
root.resizable(0,0)


# Add a grid
mainframe = Frame(root)
mainframe.grid(column=0,row=0, sticky=(N,W,E,S) )

mainframe.grid_rowconfigure(0, weight=10)
mainframe.grid_columnconfigure(0, weight=20)

mainframe.grid_rowconfigure(1, weight=10)
mainframe.grid_columnconfigure(1, weight=10)

mainframe.grid_rowconfigure(2, weight=10)
mainframe.grid_columnconfigure(2, weight=10)

mainframe.grid_rowconfigure(3, weight=10)
mainframe.grid_columnconfigure(3, weight=10)

mainframe.configure(background='black')



#Drop Down Box
tkvar = StringVar(root)
programs = {'Software Engineering (Single Major)',
            'Software Engineering (Extended Major)',
            'Software Engineering (With Data Science Minor)',
            'Software Engineering / Electrical Engineering (Dual Major)'}
tkvar.set('Software Engineering (Single Major)')
drpPrograms = OptionMenu(mainframe, tkvar, *programs).grid(row=1, column=0, sticky="n")




lblMain = Label(mainframe, text="The Unofficial UQ Program Planner (Software Engineering)",
                 fg="black", font="SegoeUI 16 bold")
lblMain.grid(row=0, column=0, sticky="n")


lblSelectProgram = Label(mainframe, text="Please select your program from the following list: ")
lblSelectProgram.grid(row=1, column=0, sticky="n")


lblCredits = Label(mainframe,
                   text="| Created by Fouad Khalaf 2018 | github: carb0nated | Last update: December 2018 |")
lblCredits.grid(row=3, column=1, sticky="s")







root.mainloop()

