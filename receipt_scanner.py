# receipt_scanner.py

import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from PIL import Image, ImageTk
import numpy as np
import easyocr

class ReceiptScannerPage(ttk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        label = ttk.Label(self, text="Receipt Scanner", font=("Arial", 18))
        label.pack(side="top", fill="x", pady=10)

        upload_button = ttk.Button(self, text="Upload Receipt", command=self.upload_receipt)
        upload_button.pack(side="top", pady=10)

        self.image_label = ttk.Label(self)
        self.image_label.pack(pady=10)

        scan_button = ttk.Button(self, text="Scan Receipt", command=self.scan_receipt)
        scan_button.pack(side="top", pady=10)

        self.result_label = ttk.Label(self, text="", font=("Arial", 12))
        self.result_label.pack(side="top", pady=10)

        navigate_button = ttk.Button(self, text="Go to Expense Tracker", command=lambda: controller.show_frame("ExpenseTrackerPage"))
        navigate_button.pack(side="bottom", pady=10)

    def upload_receipt(self):
        self.receipt_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg *.jpeg *.png")])
        if self.receipt_path:
            img = Image.open(self.receipt_path)
            img = img.resize((400, 300), Image.LANCZOS)  # Use Image.LANCZOS instead of Image.ANTIALIAS
            img = ImageTk.PhotoImage(img)
            self.image_label.config(image=img)
            self.image_label.image = img

    def scan_receipt(self):
        if hasattr(self, 'receipt_path'):
            img = Image.open(self.receipt_path)
            img = img.convert('RGB')  # Ensure image is in RGB format
            img_np = np.array(img)  # Convert image to numpy array
            reader = easyocr.Reader(['en'])
            result = reader.readtext(img_np)
            extracted_text = "\n".join([text[1] for text in result])
            self.result_label.config(text=extracted_text)
            self.extract_and_log_expenses(extracted_text)
        else:
            messagebox.showerror("No Image", "Please upload a receipt first.")

    def extract_and_log_expenses(self, text):
        # Dummy extraction: look for lines with "$" and log them as expenses
        for line in text.split('\n'):
            if "$" in line:
                try:
                    amount = float(line.strip().split('$')[-1])
                    self.controller.expenses.append(("Unknown", amount))
                except ValueError:
                    continue

"""
This section defines the receipt scanner page, which includes functionality for 
uploading and scanning receipt images using EasyOCR, and logging the extracted expenses.
"""