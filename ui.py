import tkinter as tk

window = tk.Tk()
window.geometry('300x400')
window.title('My appication')

button = tk.Button(window, text='submit')
button.pack()

window.mainloop()