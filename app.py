# app.py

import tkinter as tk
from tkinter import ttk
from receipt_scanner import ReceiptScannerPage
from expense_tracker_page import ExpenseTrackerPage

class ExpenseTrackerApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Receipt Scanner & Expense Tracker")
        self.geometry("800x600")

        self.expenses = []  # List to store expenses

        # Create a container for the frames
        container = ttk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}  # Dictionary to hold different frames

        for F in (ReceiptScannerPage, ExpenseTrackerPage):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("ReceiptScannerPage")

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()

"""
This section defines the main application window and sets up navigation between 
the receipt scanning and expense tracking pages.
"""