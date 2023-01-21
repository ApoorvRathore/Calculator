from tkinter import *


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
                value = str(e)
                scvalue.set(value)
                screen.update()

        scvalue.set(value)
        screen.update()
    elif text == "c":
        scvalue.set("")
        screen.update()
    else:
        scvalue.set(scvalue.get() + text)
        screen.update()


root = Tk()
root.title("GUI-Calculator")
root.geometry('344x536')
root.resizable(width=False, height=False)
root.wm_iconbitmap("calculator.ico")
scvalue = StringVar()

screen = Entry(root,
               textvariable=scvalue,
               font="lucida 20 bold", )
screen.pack(fill=X,
            ipadx=20,
            ipady=10,
            padx=10)
f = Frame(root,
          bg='brown')
b = Button(f,
           text='9',
           padx=25,
           pady=10,
           font="lucida 15 bold",
           bg="yellow")
b.pack(side=LEFT,
       pady=10,
       padx=10)
b.bind('<Button-1>', click)
b = Button(f,
           text='8',
           padx=25,
           pady=10,
           font="lucida 15 bold",
           bg="yellow")
b.pack(side=LEFT,
       pady=10,
       padx=10)
b.bind('<Button-1>', click)

b = Button(f, text='7',
           padx=25,
           pady=10,
           font="lucida 15 bold",
           bg="yellow")
b.pack(side=LEFT,
       pady=10,
       padx=10)
b.bind('<Button-1>', click)

f.pack()

f = Frame(root,
          bg='brown')
b = Button(f, text='6',
           padx=25,
           pady=10,
           font="lucida 15 bold",
           bg="yellow")
b.pack(side=LEFT,
       pady=10,
       padx=10)
b.bind('<Button-1>', click)

b = Button(f,
           text='5',
           padx=25,
           pady=10,
           font="lucida 15 bold",
           bg="yellow")
b.pack(side=LEFT,
       pady=10,
       padx=10)
b.bind('<Button-1>', click)

b = Button(f,
           text='4',
           padx=25,
           pady=10,
           font="lucida 15 bold",
           bg="yellow")
b.pack(side=LEFT,
       pady=10,
       padx=10)
b.bind('<Button-1>', click)

f.pack()

f = Frame(root,
          bg='brown')
b = Button(f,
           text='3',
           padx=25,
           pady=10,
           font="lucida 15 bold",
           bg="yellow")
b.pack(side=LEFT,
       pady=10,
       padx=10)
b.bind('<Button-1>', click)

b = Button(f,
           text='2',
           padx=25,
           pady=10,
           font="lucida 15 bold",
           bg="yellow")
b.pack(side=LEFT,
       pady=10,
       padx=10)
b.bind('<Button-1>', click)

b = Button(f,
           text='1',
           padx=25,
           pady=10,
           font="lucida 15 bold",
           bg="yellow")
b.pack(side=LEFT,
       pady=10,
       padx=10)
b.bind('<Button-1>', click)

f.pack()

f = Frame(root,
          bg='brown')
b = Button(f,
           text='0',
           padx=25.5,
           pady=10,
           font="lucida 15 bold",
           bg="yellow")
b.pack(side=LEFT,
       pady=10,
       padx=11, )
b.bind('<Button-1>', click)

b = Button(f,
           text='c',
           padx=25,
           pady=10,
           font="lucida 15 bold",
           bg="yellow")
b.pack(side=LEFT,
       pady=10,
       padx=10)
b.bind('<Button-1>', click)

b = Button(f,
           text='=',
           padx=23,
           pady=10,
           font="lucida 15 bold",
           bg="yellow")
b.pack(side=LEFT,
       pady=10,
       padx=9)
b.bind('<Button-1>', click)

f.pack()

f = Frame(root,
          bg='brown')
b = Button(f,
           text='-',
           padx=25,
           pady=10,
           font="lucida 15 bold",
           bg="yellow")
b.pack(side=LEFT,
       pady=10,
       padx=10)
b.bind('<Button-1>', click)

b = Button(f,
           text='+',
           padx=25,
           pady=10,
           font="lucida 15 bold",
           bg="yellow")
b.pack(side=LEFT,
       pady=10,
       padx=10)
b.bind('<Button-1>', click)

b = Button(f,
           text='*',
           padx=28,
           pady=10,
           font="lucida 15 bold",
           bg="yellow")
b.pack(side=LEFT,
       pady=10,
       padx=10)
b.bind('<Button-1>', click)

f.pack()
f = Frame(root,
          bg='brown')
b = Button(f,
           text='/',
           padx=25,
           pady=10,
           font="lucida 15 bold",
           bg="yellow")
b.pack(side=LEFT,
       pady=10,
       padx=10)
b.bind('<Button-1>', click)
b = Button(f,
           text='%',
           padx=25,
           pady=10,
           font="lucida 15 bold",
           bg="yellow")
b.pack(side=LEFT,
       pady=10,
       padx=10)
b.bind('<Button-1>', click)

b = Button(f, text='**',
           padx=22,
           pady=10,
           font="lucida 15 bold",
           bg="yellow")
b.pack(side=LEFT,
       pady=10,
       padx=10)
b.bind('<Button-1>', click)

f.pack()
root.mainloop()
