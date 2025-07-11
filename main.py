from tkinter import *
import re

root = Tk()
#button_9 = Button(label_key,text='9',height=3,width=5,font=('Helvetica','12'))
#button_9.grid(row=0,column=0)
class Calculator:
    def click_button(self, char):
        # Contribution: If the user pressed “.”, check the current number
        if char == '.':
            # split the expression on any operator to get the last (current) number
            last_number = re.split(r'[\+\-\*/]', self.operator)[-1]
             # if it already contains a “.”, ignore press
            if '.' in last_number:
                return

        # Otherwise append the character as before
        self.operator += str(char)
        self.var.set(self.operator)

    def clear(self):
        self.entry.delete(0,END)
        self.operator =""

    # Contribution: Delete key for most recent input
    def delete(self):
        self.operator = self.operator[:-1]
        self.var.set(self.operator)


    # Contribution: Catches input errors and displays an "Error" message
    def evaluate(self):
        # if x is used for multiplication 
        expr = self.operator.replace('x','*')

        try:
            result = eval(expr)
        except Exception:
            # clear the broken expression
            self.operator = ""
            # show “Error” in the display
            self.var.set("Error")
        else:
            # on success, update both internal state and display
            self.operator = str(result)
            self.var.set(self.operator)




    def __init__(self,master):

        self.operator = ""
        self.var = StringVar()
        frame_s = Frame(master, height=400, width=45 )
        frame_s.pack(side=TOP, fill=BOTH, expand=True)
        self.entry = Entry(frame_s,textvariable=self.var,bg='grey',width=45,bd=20,insertwidth=4,justify='right',font=('arial',10,'bold'))
        self.entry.pack()
        self.t = Text(self.entry,height=40)



        label_key = Label(root, height=15, width=30,bd=10,bg='gray50')
        label_key.pack(side=LEFT, fill=BOTH, expand=True)

        label_fkey = Label(root, height=15, width=15, bg='gray25')
        label_fkey.pack(fill=BOTH, expand=True)

        label_7 = Label(label_key, bg='black')
        label_7.grid(row=0, column=0)
        button_7 = Button(label_7, text='7', font=('Helvetica', '16'),command= lambda : self.click_button(7),bg='black',fg='cyan')
        button_7.pack()

        label_8 = Label(label_key, bg='black')
        label_8.grid(row=0, column=1, padx=20)
        button_8 = Button(label_8, text='8', font=('Helvetica', '16'),command= lambda: self.click_button(8),bg='black',fg='cyan')
        button_8.pack()

        label_9 = Label(label_key, bg='black')
        label_9.grid(row=0, column=2, padx=10)
        button_9 = Button(label_9, text='9', font=('Helvetica', '16'),command= lambda: self.click_button(9),bg='black',fg='cyan')
        button_9.pack()

        label_4 = Label(label_key, bg='black')
        label_4.grid(row=1, column=0, padx=10, pady=10)
        button_4 = Button(label_4, text='4', font=('Helvetica', '16'),command= lambda: self.click_button(4),bg='black',fg='cyan')
        button_4.pack()

        label_5 = Label(label_key, bg='black')
        label_5.grid(row=1, column=1, padx=10, pady=10)
        button_5 = Button(label_5, text='5', font=('Helvetica', '16'),command= lambda: self.click_button(5),bg='black',fg='cyan')
        button_5.pack()

        label_6 = Label(label_key, bg='black')
        label_6.grid(row=1, column=2, padx=10, pady=10)
        button_6 = Button(label_6, text='6', font=('Helvetica', '16'),command= lambda: self.click_button(6),bg='black',fg='cyan')
        button_6.pack()

        label_1 = Label(label_key, bg='black')
        label_1.grid(row=2, column=0, padx=10)
        button_1 = Button(label_1, text='1', font=('Helvetica', '16'),command= lambda: self.click_button(1),bg='black',fg='cyan')
        button_1.pack()

        label_2 = Label(label_key, bg='black')
        label_2.grid(row=2, column=1, padx=10)
        button_2 = Button(label_2, text='2', font=('Helvetica', '16'),command= lambda: self.click_button(2),bg='black',fg='cyan')
        button_2.pack()

        label_3 = Label(label_key, bg='black')
        label_3.grid(row=2, column=2, padx=10)
        button_3 = Button(label_3, text='3', font=('Helvetica', '16'),command= lambda: self.click_button(3),bg='black',fg='cyan')
        button_3.pack()

        label_0 = Label(label_key, bg='black')
        label_0.grid(row=3, column=0, padx=10, pady=10)
        button_0 = Button(label_0, text='0', font=('Helvetica', '16'),command= lambda: self.click_button(0),bg='black',fg='cyan')
        button_0.pack()

        label_deci = Label(label_key, bg='black')
        label_deci.grid(row=3, column=1, padx=10, pady=10)
        button_deci = Button(label_deci, text='.', font=('Helvetica', '16'),command= lambda: self.click_button('.'),bg='black',fg='cyan')
        button_deci.pack()

        label_equal = Label(label_key, bg='black')
        label_equal.grid(row=3, column=2, padx=10, pady=10)
        button_equal = Button(label_equal, text='=', font=('Helvetica', '16'),command= self.evaluate,bg='black',fg='cyan')
        button_equal.pack()

        #Contribution: Adjusting spacing for new Del key, adding Del key with functionality.
        label_C = Label(label_fkey, bg='black')
        label_C.grid(row=0, column=0, sticky=W, padx=10, pady=10)
        button_C = Button(label_C, text='C', font=('Helvetica', '16'), height=1, width=3,command=  self.clear,bg='black',fg='cyan')
        button_C.pack(side=LEFT)

        label_del = Label(label_fkey, bg ='black')
        label_del.grid(row=0,column=1,sticky=E)
        button_del = Button(label_del, text='Del', font=('Helvetica', '16'), height=1, width=3,command=self.delete, bg='black', fg='cyan')
        button_del.pack(side=LEFT)

        label_sub = Label(label_fkey, bg='black')
        label_sub.grid(row=1, column=0, sticky=W, padx=10, pady=10)
        button_sub = Button(label_sub, text='-', font=('Helvetica', '16'), height=1, width=3,command= lambda: self.click_button('-'),bg='black',fg='cyan')
        button_sub.pack(side=LEFT)

        label_mul = Label(label_fkey, bg='black')
        label_mul.grid(row=1, column=1, sticky=E)
        button_mul = Button(label_mul, text='x', font=('Helvetica', '16'), height=1, width=3,command= lambda: self.click_button('*'),bg='black',fg='cyan')
        button_mul.pack()

        label_div = Label(label_fkey, bg='black')
        label_div.grid(row=2, column=0, sticky=W, padx=10)
        button_div = Button(label_div, text='/', font=('Helvetica', '16'), height=1, width=3,command= lambda: self.click_button('/'),bg='black',fg='cyan')
        button_div.pack()

        label_add = Label(label_fkey, bg='black')
        label_add.grid(row=2, column=1, sticky=E)
        button_add = Button(label_add, text='+', font=('Helvetica', '16'), height=1, width=3,command= lambda: self.click_button('+'),bg='black',fg='cyan')
        button_add.pack()

        label_lbrace = Label(label_fkey, bg='black')
        label_lbrace.grid(row=3,column=0,sticky=W, padx=10, pady=10)
        button_lbrace = Button(label_lbrace,text='(', font=('Helvetica', '16'), height=1, width=3,command= lambda: self.click_button('('),bg='black',fg='cyan')
        button_lbrace.pack()

        label_rbrace = Label(label_fkey, bg='black')
        label_rbrace.grid(row=3, column=1, sticky=E, pady=10)
        button_rbrace = Button(label_rbrace, text=')', font=('Helvetica', '16'), height=1, width=3,
                               command=lambda: self.click_button(')'),bg='black',fg='cyan')
        button_rbrace.pack()

c = Calculator(root)
root.title("Sushant\'s Calculator")
root.mainloop()