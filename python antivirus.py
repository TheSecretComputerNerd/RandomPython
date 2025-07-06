import os
import tkinter as tk
from tkinter import ttk
from concurrent.futures import ThreadPoolExecutor

def list_files(directory):
    files = []
    with ThreadPoolExecutor() as executor:
        for filename in os.listdir(directory):
            file_path = os.path.join(directory, filename)
            if os.path.isfile(file_path):
                files.append(file_path)
    return files






def start_scan():
    start_directory = "/"  # Directory to start the search from (root directory)
    all_files = list_files(start_directory)  # Get list of all files in the computer starting from the root directory
    
    progress_bar['maximum'] = len(all_files)  # Set the maximum value of the progress bar
    
    with open("file_list.txt", "w", encoding="utf-8") as f:  # Save the list of files to a text file with utf-8 encoding
        for idx, file_path in enumerate(all_files, start=1):
            f.write(file_path + "\n")
            progress_bar['value'] = idx  # Update the value of the progress bar
            root.update_idletasks()  # Update the GUI
    print("Done!")

root = tk.Tk()
root.title("Start scan of document files")

progress_bar = ttk.Progressbar(root, orient="horizontal", length=200, mode="determinate")
progress_bar.pack(pady=10)

button = tk.Button(root, text="Start Scan", command=start_scan)
button.pack(pady=5)

root.mainloop()
