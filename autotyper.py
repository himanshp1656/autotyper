# @himanshp1656
# pip install pyautogui
# pip install tk

import tkinter as tk
import pyautogui
import random
import time
#  pyinstaller --noconsole --onefile autotyper.py
def start_typing_with_delay():
    delay_time = delay_var.get()  # Get selected delay time
    typing_content = text_input.get("1.0", "end-1c")  # Get content from text input
    time.sleep(delay_time)  # Add the selected delay time
    
    for char in typing_content:
        # Introduce errors with 20% probability (80% accuracy)
        if random.random() < 0.1:
            # Insert a random wrong character
            wrong_char = random.choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^')
            pyautogui.typewrite(wrong_char)
            time.sleep(random.uniform(0.7, 1.12))  # Wait between 0.7 to 1.12 seconds
            # Use backspace to delete the wrong character
            pyautogui.press('backspace')
        if char == '@':
            pyautogui.press('enter')  # Press enter if special character is '@'
        else:
            pyautogui.typewrite(char)  # Type the character
        time.sleep(random.uniform(0.1, 0.3))  # Add a small delay between each character

# Create the main window
root = tk.Tk()
root.title("Auto Typing Application")
root.state("zoomed")  # Maximize the window


# Add label at the top
created_by_label = tk.Label(root, text="Created by @himanshp1656")
created_by_label.pack(side="top", pady=5)

# Create text input area
text_input = tk.Text(root, height=35, width=150)
text_input.pack(pady=10)

# Create a frame for delay options
delay_frame = tk.Frame(root)
delay_frame.pack(pady=10)
delay_label = tk.Label(delay_frame, text="Autotyper will start after: ")
delay_label.pack(side="left")
# Delay options
delay_var = tk.IntVar(value=30)  # Default delay time is 30 seconds
delay_options = [("30 sec", 30), ("60 sec", 60), ("120 sec", 120), ("180 sec", 180)]

# Create radio buttons for delay options
for text, value in delay_options:
    tk.Radiobutton(delay_frame, text=text, variable=delay_var, value=value).pack(side="left", padx=10)

# Create start typing button with delay
start_button = tk.Button(root, text="Start Typing", command=start_typing_with_delay)
start_button.pack()

# Run the application
root.mainloop()
