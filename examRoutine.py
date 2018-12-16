import tkinter
from tkinter import messagebox
import time
exams = '''
Date\tSubject\n
22\tWeb\n
26\tACA\n
29\tML\n
02\tCC\n
05\tSAN
'''
while True:
    # hide main window
    root = tkinter.Tk()
    root.withdraw()

    # message box display
    #p = messagebox.showwarning("Warning","Hey Udipta! \nYour Coursera Machine Learing Assingment Is Pending !")
    p = messagebox.showinfo("Exam Routine",exams)