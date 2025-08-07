import tkinter as tk
def click(event):
    text = event.widget.cget("text")
    if text == "=":
        try:
            result = str(eval(str(screen.get())))
            screen.set(result)
        except Exception:
            screen.set("Error")
    elif text == "C":
        screen.set("")
    else:
        screen.set(screen.get() + text)

root = tk.Tk()
root.geometry("300x400")
root.title("Calculator")

screen = tk.StringVar()
entry = tk.Entry(root, textvar=screen, font="Arial 20", bd=10, relief=tk.RIDGE, justify=tk.RIGHT)
entry.pack(fill=tk.BOTH, ipadx=8, pady=10, padx=10)

buttons = [
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    ["C", "0", "=", "+"]
]

for row in buttons:
    frame = tk.Frame(root)
    for btn_text in row:
        btn = tk.Button(frame, text=btn_text, font="Arial 18", padx=10, pady=10)
        btn.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)
        btn.bind("<Button-1>", click)
    frame.pack(expand=True, fill=tk.BOTH)

root.mainloop()
