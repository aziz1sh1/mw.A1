import tkinter as tk
import subprocess
import os

# Function to open a specific Python file
def open_python_file(file_name):
    # Ensure the file exists before trying to open it
    if os.path.exists(file_name):
        subprocess.Popen(['python', file_name])
    else:
        print(f"File {file_name} does not exist.")

# Create the main window
root = tk.Tk()
root.title("mw.A1")
root.iconbitmap('icon.ico')
root.configure(bg='white')
label1 = tk.Label(root, bg ='white',text=" Choose an desire option.")
label1.pack()

# Create buttons and labels for each Python file
button1 = tk.Button(root, text="Open Script 1",bg ='lightyellow', command=lambda: open_python_file('mol1.py'))
button1.pack(pady=15)
label1 = tk.Label(root,bg ='white', text="1. Calculate the molecular weight and molecular formula from \n a sequence of standard amino acids.")
label1.pack()

button2 = tk.Button(root, text="Open Script 2",bg ='yellow', command=lambda: open_python_file('mol2.py'))
button2.pack(pady=15)
label2 = tk.Label(root,bg ='white', text="2. Calculate the molecular mass from the molecular formula \n of non-protien components.")
label2.pack()

button3 = tk.Button(root, text="Open Script 3",bg ='lightblue', command=lambda: open_python_file('mol3.py'))
button3.pack(pady=15)
label3 = tk.Label(root,bg ='white', text="3. Estimate the number of amino acids in proteins.")
label3.pack()

button4 = tk.Button(root, text="Open Script 4",bg ='lightgreen', command=lambda: open_python_file('mol4.py'))
button4.pack(pady=15)
label4 = tk.Label(root,bg ='white', text="4. Sum the molecular weight of proteins and the non-protein components.")
label4.pack()

button5 = tk.Button(root, text="Open Script 5",bg ='green', command=lambda: open_python_file('openimage.py'))
button5.pack(pady=15)
label5 = tk.Label(root,bg ='white', text="5. Single code Amino acid image.")
label5.pack()


# Run the application
root.mainloop()
