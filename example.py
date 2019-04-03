import tkinter as tk
import tkinter.ttk as ttk

root = tk.Tk()
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

tree = ttk.Treeview(root)
tree["show"] = "headings"
tree["columns"] = list(range(3))
for i in range(3):
    tree.column('#' + str(i), minwidth=300, stretch=0)
    tree.heading(i, text="Column {}".format(i))
tree.column('#0', stretch=0)

for i in range(5):
    tree.insert('', "end", i)

tree.grid(row=0, column=0, sticky=(tk.N, tk.S, tk.E, tk.W))
xs = ttk.Scrollbar(root, orient=tk.HORIZONTAL, command=tree.xview)
tree["xscrollcommand"] = xs.set
xs.grid(row=1, column=0, sticky=(tk.E, tk.W))

root.mainloop()

##
##from tkinter import *
##
##class Example(Frame):  
##
##    def printLabel(self):
##        self.hello.append('Hello\n')
##        self.hello.append('World!')  
##        return(self.hello) 
##
##    # Added 'updatePanel' method which updates the label in every button press.
##    def updatePanel(self):
##        self.panelA.config(text=str(self.printLabel()))
##
##    # Added 'hello' list and 'panelA' label in the constructor.
##    def __init__(self, root):
##        self.hello = []
##        self.panelA = None
##        Frame.__init__(self, root)
##        self.buttonA()
##        self.viewingPanel()
##
##    # Changed the method to be executed on button press to 'self.updatePanel()'.
##    def buttonA(self):
##        self.firstPage = Button(self, text="Print Text", bd=1, anchor=CENTER, height = 13, width = 13, command=lambda: self.updatePanel())
##        self.firstPage.place(x=0, y=0)        
##
##    # Changed text string to be empty.
##    def viewingPanel(self):  
##        self.panelA = Label(self, bg='white', width=65, height=13, padx=3, pady=3, anchor=CENTER, text="")
##        self.panelA.place(x=100, y=0)        
##
##
##def main():
##    root = Tk()
##    root.title("Tk")
##    root.geometry('565x205')
##    app = Example(root)
##    app.pack(expand=True, fill=BOTH)
##    root.mainloop()
##
##if __name__ == '__main__':
##    main()
##
