import tkinter as tk

def press(v):
    entry.insert(tk.END, v)

def clear():
    entry.delete(0, tk.END)

def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

root = tk.Tk()
root.title("Simple Calculator") 
root.configure(bg="lightblue")
root.resizable(False, False)
entry = tk.Entry(root, font=("segoe UI",20)
                 bg="#2d2d2d",fg="white",bd=0,justify="right")
entry.grid(row=0,column=0,columnspan=4,pady=10,padx=10,ipady=10)

buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', 'C', '+',
]

r=1
c=0
for b in buttons:
    cmd = cal if b == "=" else lambda x=b: press(x) 
    tk.Button(root, text=b, command=cmd,
              font=("segoe UI",14),
              width=5, height=2,
              bg="#ff5900" if b in "+-*/=" else "#3a3a3a",
                fg="white", bd=0).grid(row=r, column=c, padx=5, pady=5)
    c+=1
    if c == 4:
        c=0
        r+=1

tk.Button(root, text="C", command=clear,
          font=("segoe UI",14),
          bg="#ff3b3b", fg="white", 
          bd=0, width=22, height=2)\
.grid(row=r, column=0, columnspan=4, pady=8)
root.mainloop()                  