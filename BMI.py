import tkinter as tk
from tkinter import messagebox

def calculate_bmi():
    try:
        weight = float(weight_entry.get())
        height = float(height_entry.get())
        bmi = (weight * 703) / (height ** 2)

        if bmi <= 0:
            result = "Invalid BMI"
        elif bmi < 18.5:
            result = "Underweight"
        elif bmi <= 24.9:
            result = "Normal weight"
        elif bmi <= 29.9:
            result = "Overweight"
        elif bmi <= 34.9:
            result = "Obese"
        elif bmi <= 39.9:
            result = "Very obese"
        else:
            result = "Morbidly obese"

       
        messagebox.showinfo("BMI Result", f"Your BMI is {bmi:.2f} ({result})")
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers.")


root = tk.Tk()
root.title("BMI Calculator")
root.geometry("300x250")


tk.Label(root, text="Name:").pack()
name_entry = tk.Entry(root)
name_entry.pack()

tk.Label(root, text="Weight (pounds):").pack()
weight_entry = tk.Entry(root)
weight_entry.pack()

tk.Label(root, text="Height (inches):").pack()
height_entry = tk.Entry(root)
height_entry.pack()


tk.Button(root, text="Calculate BMI", command=calculate_bmi).pack(pady=10)

root.mainloop()
