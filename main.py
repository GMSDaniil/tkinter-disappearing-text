from tkinter import *
import threading
import time

YELLOW = "#f7f5dd"


class MainWindow():
    def __init__(self, main: Tk) -> None:
        self.main = main

        self.label = Label(self.main, text='The text will disappear in 5 seconds if you don\'t write', background=YELLOW)
        self.label.grid(row=0, column=1)

        self.area = Text(self.main, height=25, width=50)
        self.area.grid(row=1, column=1)
        self.area.bind('<Key>', self.reset_timer)
        
        self.timer_thread = None
        self.stop_timer = False


    def reset_timer(self, event):
        if self.timer_thread and self.timer_thread.is_alive():
            self.stop_timer = True
            self.timer_thread.join()
            self.stop_timer = False

        self.timer_thread = threading.Thread(target=self.start_timer)
        self.timer_thread.start()

    def start_timer(self):
        start_time = time.time()
        while time.time() - start_time < 5:
            time.sleep(0.1)
            if self.stop_timer:
                return
        self.area.delete('1.0', 'end-1c')

    




window = Tk()
window.title('Typing Speed')
window.config(background=YELLOW)
window.eval('tk::PlaceWindow . center')
MainWindow(window)


window.mainloop()