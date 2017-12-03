import tkinter as tk
from time import time


class Stopwatch:
    def __init__(self):
        root = tk.Tk()
        root.title('Balance Board Game')

        self.display = tk.Label(root, text='00:00', width=20)
        self.display.pack()

        self.button = tk.Button(root, text='Start', command=self.toggle)
        self.button.pack()

        self.paused = True
        root.mainloop()

    def toggle(self):
        if self.paused:
            self.paused = False
            self.button.config(text='Stop')
            self.oldtime = time()
            self.run_timer()

        else:
            self.paused = True
            self.oldtime = time()
            self.button.config(text='Start')

    def run_timer(self):
        if self.paused:
            return
        delta = int(time() - self.oldtime)
        global timestr
        timestr = '{:02}:{:02}'.format(*divmod(delta, 60))
        self.display.config(text=timestr)
        self.display.after(1000, self.run_timer)


def makeymakey():
    name = input("whats your name? \n\n") #asks for the users name
    f = open("makeymakey", "a")
    f.write(timestr) #records each users time into a seperate text file
    f.write("\n")
    f.write(name)
    f.write("\n\n")
    f.close()

def playagain(): #allows the user to play again
    while True:
        play = str(input("\n\nDo you want to play again? \n\n Yes? or No?\n\n"))
        playy = str.lower(play) #makes it lower case so the user can type yes or no in any way
        if playy == "yes":
            print("\nHave fun trying to beat your high score!\n\n")
            Stopwatch()
            makeymakey()
        elif playy =="no":
            print("\nThanks for Playing!\n")
            break
        else:
            print("Only yes or no please")


Stopwatch()
makeymakey()
playagain()
