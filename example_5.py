from threading import Timer, Thread, Event
import datetime
import tkinter as tk

app = tk.Tk()
lab = tk.Label(app, text="Did you get take your meds?")
lab.pack()


class perpetualTimer():

    def __init__(self, t, hFunction):
        self.t = t
        self.hFunction = hFunction
        self.thread = Timer(self.t, self.handle_function)

    def handle_function(self):
        self.hFunction()
        self.thread = Timer(self.t, self.handle_function)
        self.thread.start()

    def start(self):
        self.thread.start()

    def cancel(self):
        self.thread.cancel()
        
##    def create_top(self):
##        top = tk.Toplevel()
##        label = tk.Label(' did you take your meds? ')


def printer():
##    x=datetime.datetime.now()
##    y=x.replace(day=x.day, hour=7, minute=25, second=5, microsecond=0)
##    delta_t=y-x    
##    secs=delta_t.seconds+1
##    clock = "{}:{}:{}".format(y.hour, y.minute, y.second)
##    print(clock)
##        a = perpetualTimer(
    print(' did you take your meds? ')
    
##    tempo = datetime.today()
##    clock = "{}:{}:{}".format(tempo.hour, tempo.minute, tempo.second)
##    try:
##        lab['text'] = clock
##    except RuntimeError:
##        exit()

t = perpetualTimer(25200, printer)
t.start()
app.mainloop()
