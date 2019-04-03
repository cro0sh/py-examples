import tkinter as tk
from tkinter import ttk

root = tk.Tk()

combostyle = ttk.Style()

combostyle.theme_create('combostyle', 
                         settings = {'TCombobox':
                                     {'configure':
                                      {'selectbackground': '#476581',
                                       'fieldbackground': '#476581',
                                       'background': 'white'
                                       }}}
                         )
## ATTENTION: this applies the new style 'combostyle' to all ttk.Combobox
combostyle.theme_use('combostyle')
##combostyle.configure("TMenubutton", background="#476581")

# show the current styles
# print(combostyle.theme_names())

##combo = ttk.Combobox(root, values=['1', '2', '3'], width=10)
##combo['state'] = 'readonly'
##combo.pack()

def chk_cb():
    print(combo.get())
    
##button5 = tk.Button(root, text = 'chk', command=chk_cb)
##button5.configure(width = 10, activebackground = "#33B5E5",
##                          bg='#476581', font=("Helvetica", 10))    
##button5.place(x=5, y=5)
##button5.config(highlightthickness=0, fg='white')


    
##entry = tk.Entry(root)
##entry.pack()

num_one_ten = ['', 'not answering', 'dont know', ]
for number in range(0,11):
    num_one_ten.append(number)
    
##        num_one_ten.append('not answering')

yes_no = ['', 'not answering', 'yes', 'dont know', 'no']

parents_q_a = ['', 'not answering', 'great', 'good', 'so so',
               'not good', 'terrible', 'dont know']

new_lst = [num_one_ten, yes_no, parents_q_a]
new_list = {}
new_list['num_one_ten'] = num_one_ten
new_list['yes_no'] = yes_no
new_list['parents_q_a'] = parents_q_a

alst_num_one_ten = ['doice', 'poice', 'doice2', 'doice3']
alst_yes_no = ['a', 'b', 'c', 'a', 'b']
alst_parents = ['m','d','m']

frame = tk.Frame(root, height=1920, width=1080)
frame.pack()
increment = 0
increment2 = 0
increment3 = 0
for z in  alst_num_one_ten:
    increment = increment + 100
    combo = ttk.Combobox(frame, values=z, width=10)
    combo['state'] = 'readonly'
    combo.pack()
    combo.place(x=5 + increment, y=5)
increment = 0
for z in  alst_yes_no:
    increment = increment + 100
    comb2 = ttk.Combobox(frame, values=z, width=10)
    comb2['state'] = 'readonly'
    combo.pack()
    combo.place(x=205 + increment, y=5)
increment = 0
for z in alst_parents:
    increment = increment + 100
    combo = ttk.Combobox(frame, values=z, width=10)
    combo['state'] = 'readonly'
    combo.pack()
    combo.place(x=205 + increment, y=50)
##print(new_list)
##count = 0
##for z in new_list.values():
##    for z1 in z:
##        print(z1)
####    print(z)
##    
##        count +=1
##print(count)


root.mainloop()



##from Tkinter import*
##import PIL
##from PIL import ImageTk, Image
##
##class MyOptionMenu(OptionMenu):
##    def __init__(self, master, status, *options):
##        self.var = StringVar(master)
##        self.img = ImageTk.PhotoImage(Image.open("...")) #replace with your own indicator image
##        self.var.set(status)
##        OptionMenu.__init__(self, master, self.var, *options)
##        self.config(indicatoron=0, image = self.img, font=('calibri',(10)),bg='white',width=12)
##        self['menu'].config(font=('calibri',(10)),bg='white')
##
##root = Tk()
##mymenu = MyOptionMenu(root, 'Select status', 'a','b','c')
##mymenu.pack()
##root.mainloop()
