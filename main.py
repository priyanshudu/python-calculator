from tkinter import *

root = Tk()
root.title("My first GUI")
root.title("calculator")
root.geometry('280x380')
root.resizable(0, 0)
root.configure(background="black")

first_num = second_num = operator = None


#logic
def getnumber(num):
              current = result["text"]
              new = current + str(num)
              result.config(text=new)


#clear
def clear():
              result.config(text="")


#operation
def operation(op):
              global first_num, operator
              first_num = int(result["text"])
              operator = op
              result.config(text="")


#equal
def equal():
              global first_num, second_num, operator
              second_num = int(result["text"])
              if operator == "+":
                            result.config(text=str(first_num +
                                                   int(second_num)))
              elif operator == "-":
                            result.config(text=str(first_num -
                                                   int(second_num)))
              elif operator == "*":
                            result.config(text=str(first_num *
                                                   int(second_num)))
              else:
                            if second_num == 0:
                                          result.config(text="Error")
                            else:
                                          result.config(
                                              text=str(first_num /
                                                       int(second_num, 2)))


#result
result = Label(root, text='', bg='black', fg='white')
result.grid(row=0, column=0, columnspan=24, pady=(50, 25))
result.configure(font=('verdana', 30, 'bold'))

btn7 = Button(root,
              text='7',
              background="green",
              fg="white",
              width=5,
              height=2,
              command=lambda: getnumber(7))
btn7.grid(row=1, column=0)

btn8 = Button(root,
              text='8',
              background="green",
              fg="white",
              width=5,
              height=2,
              command=lambda: getnumber(8))
btn8.grid(row=1, column=1)

btn_add = Button(root,
                 text='+',
                 background="green",
                 fg="white",
                 width=5,
                 height=2,
                 command=lambda: operation('+'))
btn_add.grid(row=1, column=2)

btn9 = Button(root,
              text='9',
              background="green",
              fg="white",
              width=5,
              height=2,
              command=lambda: getnumber(9))
btn9.grid(row=1, column=3)

btn4 = Button(root,
              text='4',
              background="green",
              fg="white",
              width=5,
              height=2,
              command=lambda: getnumber(4))
btn4.grid(row=2, column=0)

btn5 = Button(root,
              text='5',
              background="green",
              fg="white",
              width=5,
              height=2,
              command=lambda: getnumber(5))
btn5.grid(row=2, column=1)

btn_sub = Button(root,
                 text='-',
                 background="green",
                 fg="white",
                 width=5,
                 height=2,
                 command=lambda: operation('-'))
btn_sub.grid(row=2, column=2)

btn6 = Button(root,
              text='6',
              background="green",
              fg="white",
              width=5,
              height=2,
              command=lambda: getnumber(6))
btn6.grid(row=2, column=3)

btn1 = Button(root,
              text='1',
              background="green",
              fg="white",
              width=5,
              height=2,
              command=lambda: getnumber(1))
btn1.grid(row=3, column=0)

btn2 = Button(root,
              text='2',
              background="green",
              fg="white",
              width=5,
              height=2,
              command=lambda: getnumber(2))
btn2.grid(row=3, column=1)

btn_mul = Button(root,
                 text='*',
                 background="green",
                 fg="white",
                 width=5,
                 height=2,
                 command=lambda: operation('*'))
btn_mul.grid(row=3, column=2)

btn3 = Button(root,
              text='3',
              background="green",
              fg="white",
              width=5,
              height=2,
              command=lambda: getnumber(3))
btn3.grid(row=3, column=3)

btn0 = Button(root,
              text='0',
              background="green",
              fg="white",
              width=5,
              height=2,
              command=lambda: getnumber(0))
btn0.grid(row=4, column=0)

btn_clear = Button(root,
                   text='C',
                   background="green",
                   fg="white",
                   width=5,
                   height=2,
                   command=lambda: clear())
btn_clear.grid(row=4, column=1)

btn_div = Button(root,
                 text='/',
                 background="green",
                 fg="white",
                 width=5,
                 height=2,
                 command=lambda: operation('/'))
btn_div.grid(row=4, column=2)

btn_equal = Button(root,
                   text='=',
                   background="green",
                   fg="white",
                   width=5,
                   height=2,
                   command=lambda: equal())
btn_equal.grid(row=4, column=3)

root.mainloop()
