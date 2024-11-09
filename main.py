import tkinter as tk
from datetime import datetime

def calculate_age():
    try:
        # Get the input values
        name = name_entry.get()
        day = int(day_entry.get())
        month = int(month_entry.get())
        year = int(year_entry.get())
        
        # Calculate age
        birth_date = datetime(year, month, day)
        today = datetime.now()
        age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
        
        # Display a personalized message with age
        result_label.config(text=f"Hello, {name}! You are {age} years old.")
    except ValueError:
        result_label.config(text="Please enter valid date, month, and year.")

# Create the main window
root = tk.Tk()
root.title("Age Calculator")
root.geometry("400x400")

# Input fields for name, day, month, and year
tk.Label(root, text="Enter your name:").pack()
name_entry = tk.Entry(root)
name_entry.pack()

tk.Label(root, text="Enter your birth date (day):").pack()
day_entry = tk.Entry(root)
day_entry.pack()

tk.Label(root, text="Enter your birth month (month):").pack()
month_entry = tk.Entry(root)
month_entry.pack()

tk.Label(root, text="Enter your birth year (year):").pack()
year_entry = tk.Entry(root)
year_entry.pack()

# Button to calculate age
calc_button = tk.Button(root, text="Calculate Age", command=calculate_age)
calc_button.pack()

# Label to display the result
result_label = tk.Label(root, text="")
result_label.pack()

# Run the application
root.mainloop()
