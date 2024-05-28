# expense_tracker_page.py

import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class ExpenseTrackerPage(ttk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        label = ttk.Label(self, text="Expense Tracker", font=("Arial", 18))
        label.pack(side="top", fill="x", pady=10)

        view_expenses_button = ttk.Button(self, text="View Expenses", command=self.view_expenses)
        view_expenses_button.pack(side="top", pady=10)

        self.expense_list = tk.Listbox(self)
        self.expense_list.pack(pady=20)

        navigate_button = ttk.Button(self, text="Go to Receipt Scanner", command=lambda: controller.show_frame("ReceiptScannerPage"))
        navigate_button.pack(side="bottom", pady=10)

        self.figure = plt.Figure(figsize=(5, 4), dpi=100)
        self.canvas = FigureCanvasTkAgg(self.figure, master=self)
        self.canvas.get_tk_widget().pack()

    def view_expenses(self):
        self.expense_list.delete(0, tk.END)
        for expense in self.controller.expenses:
            self.expense_list.insert(tk.END, f"{expense[0]}: ${expense[1]:.2f}")
        self.update_chart()

    def update_chart(self):
        self.figure.clear()
        if self.controller.expenses:
            labels, amounts = zip(*self.controller.expenses)
            plt.pie(amounts, labels=labels, autopct='%1.1f%%')
        self.canvas.draw()

"""
This section defines the expense tracker page, which allows users to view logged 
expenses in a list and see a pie chart visualization of their spending.
"""