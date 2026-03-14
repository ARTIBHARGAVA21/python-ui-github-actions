import tkinter as tk

def show_message():
    name = entry.get()
    message = f"Hello {name}, Welcome!"
    label_result.config(text=message)

root = tk.Tk()
root.title("Simple UI Program")
root.geometry("300x200")

label = tk.Label(root, text="Enter your name:")
label.pack(pady=10)

entry = tk.Entry(root)
entry.pack(pady=5)

button = tk.Button(root, text="Submit", command=show_message)
button.pack(pady=10)

label_result = tk.Label(root, text="")
label_result.pack(pady=10)

root.mainloop()