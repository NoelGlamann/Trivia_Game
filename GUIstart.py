#!usr/bin/python3
#Noel Glamann
#Dylan Eastman
#10 March 2020

'''
This program will develop the Graphical User 
Interface (GUI) for a Trivia Game
          
'''

#IMPORTS-------------------------------------------------------------------
import pickle as p
import tkinter as tk
from tkinter import scrolledtext

#FUNCTIONS-----------------------------------------------------------------

#CLASSES-------------------------------------------------------------------

class Screen(tk.Frame):
    current = 0
    
    def __init__(self):
        tk.Frame.__init__(self)
        
    def switch_frame():
        screens[Screen.current].tkraise()
        
    def main():
        Screen.current = 0
        Screen.switch_frame()  
        
class MainMenu(Screen):
    def __init__(self):
        
        tk.Frame.__init__(self)    

        self.lbl_title1 = tk.Label(self, text = "Trivia",
                                   font = ("Courier", "50"))
        self.lbl_title1.grid(row =1, column = 1,
                             sticky = "e")
        self.lbl_title2 = tk.Label(self, text = "Games",
                                   font = ("Courier", "50"))
        self.lbl_title2.grid(row = 2, column = 2,
                             sticky = "w")
        
        self.btn_geography = tk.Button(self, text = "Geography",
                                   font = ("Courier", "25"))
        self.btn_geography.grid(row = 3, column = 1,
                              columnspan = 2, sticky = "news")
        
        self.btn_history = tk.Button(self, text = "History",
                                   font = ("Courier", "25"))
        self.btn_history.grid(row = 4, column = 1,
                              columnspan = 2, sticky = "news")
        
        self.btn_music = tk.Button(self, text = "Music",
                                   font = ("Courier", "25"))
        self.btn_music.grid(row = 5, column = 1,
                              columnspan = 2, sticky = "news")
        
        self.btn_vidgame = tk.Button(self, text = "Video Games",
                                   font = ("Courier", "25"))
        self.btn_vidgame.grid(row = 6, column = 1,
                              columnspan = 2, sticky = "news")
        
        self.btn_random = tk.Button(self, text = "Random Mix",
                                   font = ("Courier", "25"))
        self.btn_random.grid(row = 7, column = 1,
                              columnspan = 2, sticky = "news")        
        
        self.btn_scorecheck = tk.Button(self, text = "Check Scores",
                                   font = ("Courier", "25"))
        self.btn_scorecheck.grid(row = 8, column = 1,
                              columnspan = 2, sticky = "news")
        
          
        
        self.grid_columnconfigure(0, weight = 1)
        self.grid_columnconfigure(3, weight = 1)
        self.grid_rowconfigure(0, weight = 1)
        self.grid_rowconfigure(9, weight = 2)
        
class Question(tk.Frame):
    def __init__(self):
        
        tk.Frame.__init__(self)  
        
        self.btn_return = tk.Button(self, text = "Main Menu",
                                   font = ("Courier", "10"))
        self.btn_return.grid(row = 0, column = 0, sticky = "news")
        
        self.lbl_question = tk.Label(self, text = "???",
                                   font = ("Courier", "35"))
        self.lbl_question.grid(row = 1, column = 1,
                               columnspan = 2)
        
        self.rad_multiplechoice = MultipleChoices(self)
        self.rad_multiplechoice.grid(row = 2, column = 1,
                                     rowspan = 4,
                                     columnspan = 2,
                                     sticky = "news")
        self.btn_submit = tk.Button(self, text = "Submit",
                                   font = ("Courier", "10"))
        self.btn_submit.grid(row = 6, column = 3, sticky = "news")
        
        self.grid_columnconfigure(0, weight = 1)
        self.grid_columnconfigure(1, weight = 2)
        self.grid_columnconfigure(2, weight = 2)
        self.grid_columnconfigure(3, weight = 1)
        
        self.grid_rowconfigure(0, weight = 1)
        self.grid_rowconfigure(1, weight = 2)
        self.grid_rowconfigure(2, weight = 2)
        self.grid_rowconfigure(3, weight = 2)
        self.grid_rowconfigure(4, weight = 2)
        self.grid_rowconfigure(5, weight = 2)
        self.grid_rowconfigure(6, weight = 1)
        
        
        
class MultipleChoices(tk.Frame):
    def __init__(self, parent): 
        tk.Frame.__init__(self, master = parent)
        
        self.choice1 = tk.Radiobutton(self, text = "hello",
                                      selectcolor = "black",
                                      font = ("Courier", "20"))
        self.choice1.grid(row = 0, column = 0, sticky = "news")
        self.choice2 = tk.Radiobutton(self, text = "hi",
                                      selectcolor = "black",
                                      font = ("Courier", "20"))
        self.choice2.grid(row = 1, column = 0, sticky = "news")
        self.choice3 = tk.Radiobutton(self, text = "hallo",
                                      selectcolor = "black",
                                      font = ("Courier", "20"))
        self.choice3.grid(row = 2, column = 0, sticky = "news")       
        self.choice4 = tk.Radiobutton(self, text = "hola",
                                      selectcolor = "black",
                                      font = ("Courier", "20"))
        self.choice4.grid(row = 3, column = 0, sticky = "news")              
        
        

#MAIN----------------------------------------------------------------------
if __name__ == "__main__":
    
    
    pickle_file = open("geography.pickle", "rb")
    geography_s = p.load(pickle_file)  
    pickle_file.close()
    
    pickle_file = open("history.pickle", "rb")
    history_s = p.load(pickle_file)  
    pickle_file.close()
    
    pickle_file = open("music.pickle", "rb")
    music_s = p.load(pickle_file)  
    pickle_file.close()
    
    pickle_file = open("vidgame.pickle", "rb")
    vidgame_s = p.load(pickle_file)  
    pickle_file.close()
    
    pickle_file = open("random.pickle", "rb")
    random_s = p.load(pickle_file)  
    pickle_file.close()    
    
    pickle_file = open("questions.pickle", "rb")
    questions = p.load(pickle_file)  
    pickle_file.close()       
    
    
    root = tk.Tk()
    root.geometry("500x500")
    root.title("Trivia Game")
    root.grid_columnconfigure(0, weight = 1)
    root.grid_rowconfigure(0, weight = 1)    
    
    main_menu = Question()
    main_menu.grid(row = 0, column = 0, sticky = "news")
    
    screens = []
    
    screens.append(MainMenu())    
    screens.append(Question())     
  
    screens[0].grid(row = 0, column = 0, sticky = "news")  
    screens[1].grid(row = 0, column = 0, sticky = "news")
    
    Screen.current = 0
    Screen.switch_frame()    

    root.mainloop()
    
    