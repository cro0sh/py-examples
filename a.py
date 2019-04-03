import tkinter as tk
import tkinter.ttk as ttk

class meals_app(tk.Tk):
    def __init__(a, zero=None):
        super().__init__(zero)
        a.zero = zero
        a.frame = tk.Frame(a, height=1080, width=1920)
        a.frame.pack()

##        a.canvas1 = tk.Canvas(a, bg="#476581",
##                                            width = 210, height = 1920)
##        a.canvas1.pack()
##        a.canvas1.place(x=0, y=0)

        a.test_list = ('rice', 'steak', 'oranges')

        a.create_widgets()

        entry = tk.Entry(a)
        entry.pack()
        entry.bind('<KeyRelease>', a.on_keyrelease)
        entry.place(x=25, y=40)

        a.listbox = tk.Listbox(a)
        a.listbox.pack()
        #listbox.bind('<Double-Button-1>', on_select)
        a.listbox.bind('<<ListboxSelect>>', a.on_select)
        a.listbox_update(a.test_list)
        a.listbox.place(x=25, y=60)

        button1 = tk.Button(a, text = 'Add Item', command=a.add_item)
        button1.configure(width = 10, activebackground = "#33B5E5",
                          bg='#476581', font=("Helvetica", 10))
    
##            button1_window = a.canvas1.create_window(35, 10 + increment, anchor=NW, window=button1)
##        button1_window = a.canvas1.create_window(100, 25,  window=button1)
        button1.place(x=225, y=40)
        button1.config(highlightthickness=0, fg='white')

        button3 = tk.Button(a, text = 'Remove Item', command=a.remove_itemz)
        button3.configure(width = 10, activebackground = "#33B5E5",
                          bg='#476581', font=("Helvetica", 10))
    
##            button1_window = a.canvas1.create_window(35, 10 + increment, anchor=NW, window=button1)
##        button1_window = a.canvas1.create_window(100, 25,  window=button1)
        button3.place(x=225, y=65)
        button3.config(highlightthickness=0, fg='white')

        a.items = []
        a.meal1_items = []
        a.meal2_items = []
        a.meal3_items = []
        a.meal4_items = []
        a.meal5_items = []
        a.meal6_items = []
        a.meal7_items = []
        a.meal8_items = []
        
        
        a.itemsd = {}
        
        a.incre_var = 0
        a.increment = 0

        from time import gmtime, strftime, localtime

        time = strftime("%Y-%m-%d %H:%M:%S", localtime())

        a.label_time = tk.Label(a, text='Today is ' + time, fg="#476581")
        a.label_time.pack()
        a.label_time.place(x=1150, y=10)

##        while True:
        a.add_item_label = tk.Label(a, text='', fg="#476581")
        a.add_item_label.pack()
        a.add_item_label_list = []
        a.update()
        a.add_item_label.update()


        a.columnconfigure(0, weight=1)
        a.rowconfigure(0, weight=1)

        tree = ttk.Treeview(a)
        tree["show"] = "headings"
        tree["columns"] = list(range(4))
        for i in range(3):
            tree.column('#' + str(i), minwidth=300, stretch=0)
            tree.heading(i, text="Column {}".format(i))
        tree.column('#0', stretch=0)

        for i in range(5):
            tree.insert('', "end", i)

        tree.pack()
        tree.place(x=500,y=35)
        xs = ttk.Scrollbar(a, orient=tk.HORIZONTAL, command=tree.xview)
        tree["xscrollcommand"] = xs.set
        xs.pack()
        xs.place(x=500, y=243)
        a.variable = 0

        a.var = [1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,]
        a.var2 = ["a","a","a","a","a","a","a","a","a","a",
                  ]

        for z, a in zip(a.var, a.var2):
        
            tree.insert('', 'end', text="Item_" + str(z), values=("mg", a, "z" ))
##        a.variable += 1

##        a.mainloop()
##        a.add_item_label.place(x=300 + a.increment,y=40)
        
##        print('add item event', event)

    def remove_itemz(a):

        a.add_item_label['text'] =  ''   # update label
        a.after(100, a.remove_itemz)
##        entry.delete(0, END)
    def remove_item(a):
        meal_list = [a.meal1_items,
        a.meal2_items, 
        a.meal3_items ,
        a.meal4_items ,
        a.meal5_items ,
        a.meal6_items ,
        a.meal7_items,
        a.meal8_items]

        for meal in meal_list:
            for z in meal:
                print('on list number ', meal)
                print('z is ', z)
##                if len(meal) > 0:
    ##                meal = ''
##                    print('a.items in remove_item before ', a.items)
##                meal.pop(0)
                a.add_item_label.update()
                meal.clear()
                print('meal is ', meal)
##                z = ''
                print('a.add_item_label', a.add_item_label)
##        for z in a.add_item_label_list:
##            z=''
##            a.add_item_label.configure(text=z)
##                a.add_item_label.configure(text=z)
##                z = ''
                
##                    print('a.items in remove_item before ', a.items)
    ##                a.label_time.update()
##                else:
##                    print('empty list')
        
        
    
    def relax(a):
        var = 1+1

    def create_widgets(a):
##        a.add_meals = tk.Button(a)
##        a.add_meals["text"] = "Add Meal"
##        a.add_meals["command"] = a.add_meal()
##        a.add_meals.pack(side="top")

        

        button2 = tk.Button(a, text = 'New Meal', command=a.new_meal)
        button2.configure(width = 10, activebackground = "#33B5E5",
                              bg='#476581', font=("Helvetica", 10))
        
##            button1_window = a.canvas1.create_window(35, 10 + increment, anchor=NW, window=button1)
##        button1_window = a.canvas1.create_window(100, 25,  window=button1)
        button2.place(x=225, y=15)
        button2.config(highlightthickness=0, fg='white')

        

##        a.quit = tk.Button(a, text="QUIT", fg="red",
##                              command=a.zero.destroy)
##        a.quit.pack(side="bottom")
##    def new_meal_helper(a):
##        print('new meal helper a.event is', a.event)

        
    def new_meal(a):
##        try:
##            a.event_new_meal = a.event
##        except Exception:
####            a.relax()
##
##            
####            a.event = ''
##            a.items = []
##    ##        a.event = event.widget.get(event.widget.curselection())
##            print('a.event is ', a.event)
####            print('a.event_new_meal is ', a.event_new_meal)
##    ##        lst = [1,2,3,4,5,6]
##    ##        a.incre_var = 1
##    ##        a.increment = 0
##    ##        for items in lst:
##            a.incre_var += 1
##            a.increment += 115
##            label = tk.Label(a, text="Meal " + str(a.incre_var), fg="#476581")
##            label.pack()
##            label.place(x=300 + a.increment,y=40)

            
##        a.event = ''
        a.items = []
##        a.event = event.widget.get(event.widget.curselection())
##        print('a.event in new meal is ', a.event)
##            print('a.event_new_meal is ', a.event_new_meal)
##        lst = [1,2,3,4,5,6]
##        a.incre_var = 1
##        a.increment = 0
##        for items in lst:
        a.incre_var += 1
        a.increment += 115
        if a.incre_var < 9: # and a.increment < 1000:
            label = tk.Label(a, text="Meal " + str(a.incre_var), fg="#476581")
            label.pack()
            
            label.place(x=300 + a.increment,y=40)
        else:
            print('no more than 8 meals')
    def add_item_update(a):
        pass
    def add_item(a):
##        print('add_meal()')
##        try:
##        a.event = a.on_select()        
##        a.event_bool = True
##        if boolean:
        if a.incre_var == 0:
            print('new meal first')
        else:
            print('a event in add item', a.event)
        ##        meal =
            a.items.append(a.event)
##            a.meal1_items.append(a.event)
            
##            a.itemsd = ([a.event], [a.incre_var])
##            print(a.itemsd)
##            a.itemsd = FrozenDict()
##            a.itemsd[a.event] = a.incre_var
##            a.itemsd([(a.event, a.incre_var)])
##            helper_list = []
##            meal_check = a.incre_var
##            mealz = [1,2,3,4,5,6,7,8]
##            for meal in mealz:
##                a.itemsd[a.incre_var] = a.mealmeal_items

            if a.incre_var == 1:
                a.itemsd[a.incre_var] = a.meal1_items
                a.meal1_items.append(a.event)
            elif a.incre_var == 2:
                a.itemsd[a.incre_var] = a.meal2_items
                a.meal2_items.append(a.event)
            elif a.incre_var == 3:
                a.itemsd[a.incre_var] = a.meal3_items
                a.meal3_items.append(a.event)
            elif a.incre_var == 4:
                a.itemsd[a.incre_var] = a.meal4_items
                a.meal4_items.append(a.event)
            elif a.incre_var == 5:
                a.itemsd[a.incre_var] = a.meal5_items
                a.meal5_items.append(a.event)
            elif a.incre_var == 6:
                a.itemsd[a.incre_var] = a.meal6_items
                a.meal6_items.append(a.event)
            elif a.incre_var == 7:
                a.itemsd[a.incre_var] = a.meal7_items
                a.meal7_items.append(a.event)
            else:
                a.itemsd[a.incre_var] = a.meal8_items
                a.meal8_items.append(a.event)
          
           
                

            print(a.itemsd)
##            a.new_meal_helper()
        ##        a.event = a.event.widget.get(a.event.widget.curselection())
        ##        label = tk.Label(a, text="Meal 1", fg="#476581")
        ##        label.pack()
        ##        label.place(x=790,y=40)
            
            increment = 0
            all_meal_items = [a.meal1_items,
        a.meal2_items, 
        a.meal3_items ,
        a.meal4_items ,
        a.meal5_items ,
        a.meal6_items ,
        a.meal7_items,
        a.meal8_items]
            for item in a.items:
                increment = increment + 35 
                
                a.add_item_label = tk.Label(a, text=item, fg="#476581")
                
                a.add_item_label.pack()
                a.add_item_label_list.append(a.add_item_label)
                if a.increment < 1000: # increment < 281: # and a.increment < 1000:
                    a.add_item_label.place(x=300 + a.increment,y=40 + increment)
                    
##                    label.place(x=300 + a.increment,y=40 + increment)
##                    v = tk.StringVar()
##                    z = tk.Label(a, textvariable=v).pack()
##                    v.set(item)
##                    print(v)
##                    z.place(x=300 + a.increment,y=40 + increment)
                else:
##                    print('off screen')
##                    label.place(x=300 + 920,y=40 + 280) #meal 8
                    label.place(x=300 + 920,y=40 + increment) #meal 8
        
##        if boolean == True:
##            print('add item', event)
##        print('add item', event)
        
##        button1 = tk.Button(a, text = 'Add Item', command=a.relax)
##        button1.configure(width = 10, activebackground = "#33B5E5",
##                          bg='#476581', font=("Helvetica", 10))
##    
####            button1_window = a.canvas1.create_window(35, 10 + increment, anchor=NW, window=button1)
####        button1_window = a.canvas1.create_window(100, 25,  window=button1)
##        button1.place(x=580, y=40)
##        button1.config(highlightthickness=0, fg='white')
        
##        return event
##        except:
##            pass
        
    
    def on_keyrelease(a, event):

        # get text from entry
        value = event.widget.get()
        value = value.strip().lower()

        # get data from test_list
        if value == '':
            data = a.test_list
        else:
            data = []
            for item in a.test_list:
                if value in item.lower():
                    data.append(item)                

        # update data in listbox
        a.listbox_update(data)


    def listbox_update(a, data):
        # delete previous data
        a.listbox.delete(0, 'end')

        # sorting data 
        data = sorted(data, key=str.lower)

        # put new data
        for item in data:
            a.listbox.insert('end', item)


    def on_select(a, event):
##        global event
        # display element selected on list
        print('(event) previous:', event.widget.get('active'))
        print('(event)  current:', event.widget.get(event.widget.curselection()))
##        while True:
        a.event = event.widget.get(event.widget.curselection())
##        a.event_bool = True
##        a.add_item(boolean=a.event_bool, event=a.event)
##        if a.event_bool:
            
##        print('a.event', a.event)
##        return event
##        print(current_selection)
##        a.add_item(event=a.event)
        
        
        
        print('---')

##root = tk.Tk()
app = meals_app()
app.mainloop()

##
##app = Application()
##app.zero.maxsize(1000, 400)
##app.mainloop()


##print(dir(tk.Frame.configure()))


