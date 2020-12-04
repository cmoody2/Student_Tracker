#!/usr/bin/python
# -*- coding: utf-8 -*-
#   Python ver:     3.7.8
#
#   Author:         Christopher A. Moody
#
#   Purpose:        Creating a Student Tracking System. This will demonstrate
#                   OOP, Tkinter GUI module, and using Tkinter Parent
#                   and child relationships.
#
#   Tested OS:      Written and tested with Windows 10.

from tkinter import *
import tkinter as tk
from tkinter import messagebox


import student_tracker_gui
import student_tracker_func


class ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)


        self.master = master
        self.master.minsize(450, 350)
        self.master.maxsize(450, 350)

        student_tracker_func.center_window(self, 450, 350)
        self.master.title("Mojave High School Student Tracker")
        self.master.configure(bg="#90ee90")
        self.master.protocol("WM_DELETE_WINDOW", lambda: student_tracker_func.ask_quit(self))
        arg = self.master

        student_tracker_gui.load_gui(self)


if __name__ == "__main__":
   root = tk.Tk()
   App = ParentWindow(root)
   root.mainloop()
