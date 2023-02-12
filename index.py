from tkinter import *

root = Tk()
root.geometry("620x485")
root.title("Calculator")
root.minsize(620, 485)
root.maxsize(620, 485)
root.wm_iconbitmap("calculator-icon_34473.ico")

def click(event):
    global scvalue
    text = event.widget.cget("text")
    if text == "=":
        if scvalue.get().isdigit():
            value = int(scvalue.get())
        else:
            try:
                value = eval(screen.get())
            except Exception as e:
                value = "Error"

        scvalue.set(value)
        screen.update()

    elif text == "C":
        scvalue.set("")
        screen.update()
    else:
        scvalue.set(scvalue.get() + text)
        screen.update()


scvalue = StringVar()
scvalue.set("")
screen = Entry(root, textvar=scvalue, font="lucida 40 bold")
screen.pack(fill=X, padx=8, pady=10, ipadx=8)

f1 = Frame(root, bg="grey")
b = Button(f1, text="9",padx=15, pady=15, font="lucida 35 bold")
b.pack(side=LEFT, padx=5, pady=5)
b.bind("<Button-1>",click)

b = Button(f1, text="8",padx=15, pady=15, font="lucida 35 bold")
b.pack(side=LEFT, padx=5, pady=5)
b.bind("<Button-1>",click)

b = Button(f1, text="7",padx=15, pady=15, font="lucida 35 bold")
b.pack(side=LEFT, padx=5, pady=5)
b.bind("<Button-1>",click)

b = Button(f1, text="0",padx=15, pady=15, font="lucida 35 bold")
b.pack(side=LEFT, padx=5, pady=5,anchor="e")
b.bind("<Button-1>",click)

b = Button(f1, text=".",padx=15, pady=15, font="lucida 35 bold")
b.pack(side=LEFT, padx=5, pady=5,anchor="e")
b.bind("<Button-1>",click)

b = Button(f1, text="/",padx=15, pady=15, font="lucida 35 bold")
b.pack(side=LEFT, padx=5, pady=5,anchor="e")
b.bind("<Button-1>",click)

f1.pack(anchor="w")

f2 = Frame(root, bg="grey")
b = Button(f2, text="6",padx=15, pady=15, font="lucida 35 bold")
b.pack(side=LEFT, padx=5, pady=5)
b.bind("<Button-1>",click)

b = Button(f2, text="5",padx=15, pady=15, font="lucida 35 bold")
b.pack(side=LEFT, padx=5, pady=5)
b.bind("<Button-1>",click)

b = Button(f2, text="4",padx=15, pady=15, font="lucida 35 bold")
b.pack(side=LEFT, padx=5, pady=5)
b.bind("<Button-1>",click)

b = Button(f2, text="*",padx=15, pady=15, font="lucida 35 bold")
b.pack(side=LEFT, padx=5, pady=5)
b.bind("<Button-1>",click)

b = Button(f2, text="-",padx=15, pady=15, font="lucida 35 bold")
b.pack(side=LEFT, padx=5, pady=5)
b.bind("<Button-1>",click)

b = Button(f2, text="%",padx=10, pady=15, font="lucida 35 bold")
b.pack(side=LEFT, padx=5, pady=5)
b.bind("<Button-1>",click)

f2.pack(anchor="w")

f3 = Frame(root, bg="grey")
b = Button(f3, text="3",padx=15, pady=15, font="lucida 35 bold")
b.pack(side=LEFT, padx=5, pady=5)
b.bind("<Button-1>",click)

b = Button(f3, text="2",padx=15, pady=15, font="lucida 35 bold")
b.pack(side=LEFT, padx=5, pady=5)
b.bind("<Button-1>",click)

b = Button(f3, text="1",padx=15, pady=15, font="lucida 35 bold")
b.pack(side=LEFT, padx=5, pady=5)
b.bind("<Button-1>",click)

b = Button(f3, text="+",padx=9, pady=15, font="lucida 35 bold")
b.pack(side=LEFT, padx=5, pady=5)
b.bind("<Button-1>",click)

b = Button(f3, text="=",padx=9, pady=15, font="lucida 35 bold")
b.pack(side=LEFT, padx=5, pady=5)
b.bind("<Button-1>",click)

b = Button(f3, text="C",padx=9, pady=15, font="lucida 35 bold")
b.pack(side=LEFT, padx=5, pady=5)
b.bind("<Button-1>",click)

f3.pack(anchor="w")



root.mainloop()