import tkinter as tk
from PIL import Image, ImageTk
import os
import subprocess

def run_kittu():
    command = ['python', 'kittu.py']
    output = subprocess.check_output(" ".join(command), shell=True, text=True)
    output_text.config(state=tk.NORMAL)
    output_text.delete('1.0', tk.END)
    output_text.insert(tk.END, output)
    output_text.config(state=tk.DISABLED)

def close_window():
    root.destroy()

root = tk.Tk()
root.geometry("800x780")

# Open image file using Pillow
image = Image.open("image.jpg")

# Resize image
image = image.resize((1000, 170), Image.ANTIALIAS)

# Create PhotoImage object from Pillow image
photo = ImageTk.PhotoImage(image)

# Create label widget to display image
image_label = tk.Label(root, image=photo)
image_label.pack()

run_button = tk.Button(root, text="Run", command=run_kittu, width=20, height=2 )
run_button.pack(pady=10)

close_button = tk.Button(root, text="Close", command=close_window, width=20, height=2 )
close_button.pack(pady=10)

output_text = tk.Text(root, height=10, state=tk.DISABLED)
output_text.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

root.mainloop()
