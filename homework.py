import tkinter as tk
root = tk.Tk()
root.geometry("600x600")
frame = tk.Frame()
frame.master.title("Hello World")
canvas = tk.Canvas(frame)

canvas.create_oval(120,50,230,100, fill="#ffffff")
canvas.create_oval(370,50,480,100, fill="#ffffff")
canvas.create_oval(150,50,200,100, fill="blue")
canvas.create_oval(400,50,450,100, fill="blue")
canvas.create_oval(275,220,325,270, fill="red")
canvas.create_rectangle(130,380,150,440, fill="red", outline="red")
canvas.create_rectangle(150,420,470,440, fill="red", outline="red")
canvas.create_rectangle(470,400,490,440, fill="red", outline="red")

canvas.pack(expand=True, fill="both")
frame.pack(expand=True, fill="both")

root.mainloop()