#!usr/bin/python3
#Noel Glamann
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

class MainMenu(tk.Frame):
    def __init__(self):
        '''This function creates a main menu for the database,
        inlcuding positioning and jobs of widgets'''
        
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
    
    
    root = tk.Tk()
    root.geometry("500x500")
    root.title("Trivia Game")
    root.grid_columnconfigure(0, weight = 1)
    root.grid_rowconfigure(0, weight = 1)    
    
    main_menu = MainMenu()
    main_menu.grid(row = 0, column = 0, sticky = "news")
    

    root.mainloop()
    
    