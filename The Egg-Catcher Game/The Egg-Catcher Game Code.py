#upload the packages
from tkinter import * 

import winsound #import module for click sound

#Create the class function 
class game(Frame):

    def __init__(self, master=None): #Fanction for creating the first screen
        Frame.__init__(self, master)        
        self.master = master

        #First screen after running the code
        fscreen = Label(root,text='*Play Me*', fg = "lime")
        fscreen.config(font=('Ink Free',50, 'bold'))
        fscreen.config(bg='pink')
        fscreen.pack()

        #widget can take all game
        self.pack(fill=BOTH, expand=1)

        #creating button
        exitButton = Button(self, text="EXIT", fg = 'white', bg='black', activebackground = "yellow", activeforeground='deep sky blue', font =('Comic Sans', 9, 'bold'), command=self.clickExitButton, borderwidth = 5)
        startButton = Button(self, text="START",fg = 'white', bg = "red", activebackground = "yellow", activeforeground='deep sky blue', font =('Comic Sans', 9, 'bold'), command=self.clickStartButton, borderwidth = 5)
        helpButton = Button(self, text="?", fg = 'white', bg = "blue", activebackground = "yellow", activeforeground='deep sky blue', font =('Comic Sans', 9, 'bold'), command=self.clickHelpButton, borderwidth = 5)

        #position of button
        exitButton.place(x=170, y=50)
        startButton.place(x=90, y=50)
        helpButton.place(x=290, y=2)

    #Faction for help button
    def clickHelpButton(self):
        print("""AN EGG-CELLENT BRAIN STIMULANT!

Egg Catcher is a game for toddlers to learn primary colours and can be used check your
child’s attention span while building your child’s perseverance to complete the goal of the
game by having them move the basket to catch the eggs either to the left or right. They can do
so by clicking the right arrow to the right or left arrow to the left. A player has 3 lives to catch 
a certain number of eggs. If you don’t catch an egg, you lose a life. 


RULES:
1.Catch the eggs on time.
2.If you don't catch an egg and it breaks, you loose a life.
3.Failure to catch three eggs results in 'Game Over' """)
        winsound.PlaySound("Sound for help.wav", winsound.SND_FILENAME) #play sound for help button

    #Fanction for start buttion
    def clickStartButton(self):
    
        #Changing the Current working Direction
        import os
        os.system("eggGame.py")

    #Fanction for exit button
    def clickExitButton(self): 
        winsound.PlaySound("Sound for exit.wav", winsound.SND_FILENAME) #play sound for the exiting the game
        exit()


#Creating the first screen
root = Tk()
app = game(root)
root.wm_title("Let Catcher the eggs 0")
root.configure(bg='lime')
root.geometry("320x200")
root.mainloop()
