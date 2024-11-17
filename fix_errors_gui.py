import tkinter as tk
from tkinter import messagebox
import os
import subprocess

def clear_temp_files():
    try:
        temp_path = os.environ.get('TEMP')
        if temp_path:
            for file in os.listdir(temp_path):
                file_path = os.path.join(temp_path, file)
                try:
                    if os.path.isfile(file_path) or os.path.islink(file_path):
                        os.unlink(file_path)
                    elif os.path.isdir(file_path):
                        os.rmdir(file_path)
                except Exception as e:
                    print(f"Failed to delete {file_path}. Reason: {e}")
        messagebox.showinfo("Success", "Temporary files cleared successfully!")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

def repair_system_files():
    try:
        subprocess.run("sfc /scannow", shell=True, check=True)
        messagebox.showinfo("Success", "System file scan completed. Repairs (if needed) were applied.")
    except subprocess.CalledProcessError as e:
        messagebox.showerror("Error", f"An error occurred while running SFC: {e}")

def restart_explorer():
    try:
        subprocess.run("taskkill /f /im explorer.exe", shell=True, check=True)
        subprocess.run("start explorer.exe", shell=True, check=True)
        messagebox.showinfo("Success", "Windows Explorer restarted successfully!")
    except subprocess.CalledProcessError as e:
        messagebox.showerror("Error", f"An error occurred while restarting Explorer: {e}")

def create_gui():
    root = tk.Tk()
    root.title("How to Fix Errors")
    root.geometry("400x300")

    label = tk.Label(root, text="Select an option to fix common Windows errors:", font=("Arial", 12))
    label.pack(pady=10)

    clear_temp_button = tk.Button(root, text="Clear Temporary Files", command=clear_temp_files, width=30, height=2)
    clear_temp_button.pack(pady=10)

    repair_button = tk.Button(root, text="Repair System Files (SFC)", command=repair_system_files, width=30, height=2)
    repair_button.pack(pady=10)

    restart_explorer_button = tk.Button(root, text="Restart Windows Explorer", command=restart_explorer, width=30, height=2)
    restart_explorer_button.pack(pady=10)

    quit_button = tk.Button(root, text="Exit", command=root.quit, width=30, height=2)
    quit_button.pack(pady=10)

    root.mainloop()

if __name__ == "__main__":
    create_gui()
