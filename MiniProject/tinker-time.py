import tkinter as tk
from tkinter import ttk, messagebox
import ttkbootstrap as tb  # Modern styling

def calculate_end_time():
    try:
        hour = int(hour_var.get())
        mins = int(minute_var.get())
        dura = int(duration_entry.get())

        if dura < 0:
            messagebox.showerror("Invalid Input", "Duration must be positive.")
            return

        # Compute new time
        total_minutes = hour * 60 + mins + dura
        end_hour = (total_minutes // 60) % 24
        end_minute = total_minutes % 60

        # 12-hour format conversion
        am_pm = "AM" if end_hour < 12 else "PM"
        display_hour = end_hour if 1 <= end_hour <= 12 else (12 if end_hour in [0, 12] else end_hour % 12)

        # Update UI
        result_24hr.config(text=f"24-Hour Format: {end_hour:02}:{end_minute:02}")
        result_12hr.config(text=f"12-Hour Format: {display_hour:02}:{end_minute:02} {am_pm}")

    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid numbers.")

# Create themed window
root = tb.Window(themename="superhero")  # Modern theme
root.title("Time Calculator")
root.geometry("400x300")
root.resizable(False, False)

# Layout using frames
frame = ttk.Frame(root, padding=20)
frame.pack(expand=True)

# Labels and Inputs
ttk.Label(frame, text="Starting Time:", font=("Arial", 12)).grid(row=0, column=0, columnspan=2, pady=5)

hour_var = tk.StringVar()
minute_var = tk.StringVar()

hour_dropdown = ttk.Combobox(frame, textvariable=hour_var, values=[f"{i:02}" for i in range(24)], width=5)
hour_dropdown.grid(row=1, column=0, padx=5)
hour_dropdown.set("00")

minute_dropdown = ttk.Combobox(frame, textvariable=minute_var, values=[f"{i:02}" for i in range(60)], width=5)
minute_dropdown.grid(row=1, column=1, padx=5)
minute_dropdown.set("00")

ttk.Label(frame, text="Event Duration (minutes):", font=("Arial", 12)).grid(row=2, column=0, columnspan=2, pady=5)
duration_entry = ttk.Entry(frame, width=10)
duration_entry.grid(row=3, column=0, columnspan=2)

# Calculate Button
calculate_btn = ttk.Button(frame, text="Calculate End Time", command=calculate_end_time, style="primary.TButton")
calculate_btn.grid(row=4, column=0, columnspan=2, pady=10)

# Results Labels
result_24hr = ttk.Label(frame, text="24-Hour Format: --:--", font=("Arial", 12, "bold"))
result_24hr.grid(row=5, column=0, columnspan=2, pady=5)

result_12hr = ttk.Label(frame, text="12-Hour Format: --:-- --", font=("Arial", 12, "bold"))
result_12hr.grid(row=6, column=0, columnspan=2, pady=5)

# Run GUI
root.mainloop()
