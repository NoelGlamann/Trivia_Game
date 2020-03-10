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
    
    
    
    '''creating a main screen'''
    root = tk.Tk()
    root.geometry("500x500")
    root.title("Movie Library NG")
    root.mainloop()
    
    