import tkinter as tk
from tkinter.messagebox import showinfo

def get_key(event):
    global code

    if event.char in '0123456789':
        code += event.char
        print('>', code)
        label['text'] = code

    elif event.keysym == 'Return':
        print('result:', code)
        showinfo('Code', code)

# --- main ---

def cheese(event):
    print("Cheese")
    
root = tk.Tk()
root.geometry('100x20')

# global variables
code = ''

label = tk.Label(root, text="?")
label.pack()

root.bind('<Key>', get_key)

root.mainloop()