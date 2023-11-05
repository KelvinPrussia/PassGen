import tkinter as tk

window = tk.Tk()
window.geometry('500x300')
header = tk.Frame()
body = tk.Frame()

header_text = tk.Label(text="Password Generator", master=header)
header_text.pack()

num_slider_text = tk.Label(text="Number of Passwords", master=body)
num_slider_text.pack()
num_entry = tk.Entry(master=body)
num_entry.pack()
num_slider = tk.Scale(from_=0, to_=10, orient="horizontal", showvalue=0, master=body)
num_slider.pack()

len_slider_text = tk.Label(text="Length of Passwords", master=body)
len_slider_text.pack()
len_entry = tk.Entry(master=body)
len_entry.pack()
len_slider = tk.Scale(from_=0, to_=16, orient="horizontal", showvalue=0, master=body)
len_slider.pack()

header.pack()
body.pack()
window.mainloop()