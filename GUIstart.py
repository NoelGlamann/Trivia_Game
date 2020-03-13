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
import random as rnd

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
        
        Screen.__init__(self)    

        self.lbl_title1 = tk.Label(self, text = "Trivia",
                                   font = ("Courier", "50"))
        self.lbl_title1.grid(row =1, column = 1,
                             sticky = "e")
        self.lbl_title2 = tk.Label(self, text = "Games",
                                   font = ("Courier", "50"))
        self.lbl_title2.grid(row = 2, column = 2,
                             sticky = "w")
        
        self.btn_geography = tk.Button(self, text = "Geography",
                                       command = self.geography_update,
                                       font = ("Courier", "25"))
        self.btn_geography.grid(row = 3, column = 1,
                                columnspan = 2, sticky = "news")
        
        self.btn_history = tk.Button(self, text = "History",
                                    command = self.history_update,
                                    font = ("Courier", "25"))
        self.btn_history.grid(row = 4, column = 1,
                              columnspan = 2, sticky = "news")
        
        self.btn_music = tk.Button(self, text = "Music",
                                   command = self.music_update,
                                   font = ("Courier", "25"))
        self.btn_music.grid(row = 5, column = 1,
                              columnspan = 2, sticky = "news")
        
        self.btn_vidgame = tk.Button(self, text = "Video Games",
                                    command = self.vidgame_update,
                                    font = ("Courier", "25"))
        self.btn_vidgame.grid(row = 6, column = 1,
                              columnspan = 2, sticky = "news")
        
        self.btn_random = tk.Button(self, text = "Random Mix",
                                    command = self.rnd_update,
                                    font = ("Courier", "25"))
        self.btn_random.grid(row = 7, column = 1,
                              columnspan = 2, sticky = "news")        
        
        self.btn_scorecheck = tk.Button(self, text = "Check Scores",
                                        font =("Courier", "25"))
        self.btn_scorecheck.grid(row = 8, column = 1,
                                 columnspan = 2, sticky = "news")
        
          
        
        self.grid_columnconfigure(0, weight = 1)
        self.grid_columnconfigure(3, weight = 1)
        self.grid_rowconfigure(0, weight = 1)
        self.grid_rowconfigure(9, weight = 2)
        
        
    def geography_update(self):
        Question.section = 1
        self.change_frame()
    def history_update(self):
        Question.section = 2
        self.change_frame()
    def music_update(self):
        Question.section = 3
        self.change_frame()
    def vidgame_update(self):
        Question.section = 4
        self.change_frame()
    def rnd_update(self):
        Question.section = 5
        self.change_frame()
    def change_frame(self):
        Screen.current = 1
        Question.question = 1
        Screen.switch_frame()
        screens[1].reset_score()         
        
class Question(Screen):
    
    section = 0
    question = 0
    button_tries = 0
    streak = 0
    
    def __init__(self):
        
        Screen.__init__(self)        
        
        self.btn_return = tk.Button(self, text = "Main Menu",
                                    bg = "black", fg = "white",
                                   font = ("Courier", "10"),
                                   command = Screen.main)
        self.btn_return.grid(row = 0, column = 0, sticky = "news")
        
        
        self.text = tk.StringVar(self)
        self.text.set("help")
        
        self.lbl_question = tk.Label(self, textvariable = self.text,
                                   font = ("Courier", "22"))
        self.lbl_question.grid(row = 1, column = 1,
                               columnspan = 2)
        
        self.first = tk.StringVar()
        self.second = tk.StringVar()
        self.third = tk.StringVar()
        self.fourth = tk.StringVar()
        
        self.first.set('a')
        self.second.set('b')
        self.third.set('c')
        self.fourth.set('d')
        
        self.btn_option1 = tk.Button(self, textvariable = self.first,
                                     command = self.selected_first,
                                     fg = "black", bg = "white",
                                     font = ("Courier", "15"))
        self.btn_option1.grid(row = 2, column = 1, sticky = "news",
                              columnspan = 2) 
        
        self.btn_option2 = tk.Button(self, textvariable = self.second,
                                     command = self.selected_second,
                                     fg = "black", bg = "white",
                                      font = ("Courier", "15"))
        self.btn_option2.grid(row = 3, column = 1, sticky = "news",
                              columnspan = 2)
        
        self.btn_option3 = tk.Button(self, textvariable = self.third,
                                     command = self.selected_third,
                                     fg = "black", bg = "white",
                                      font = ("Courier", "15"))
        self.btn_option3.grid(row = 4, column = 1, sticky = "news",
                              columnspan = 2)
        
        self.btn_option4 = tk.Button(self, textvariable = self.fourth,
                                     command = self.selected_fourth,
                                     fg = "black", bg = "white",
                                      font = ("Courier", "15"))
        self.btn_option4.grid(row = 5, column = 1, sticky = "news",
                              columnspan = 2)  
        
        self.lbl_scorelbl = tk.Label(self, text = "Score:",
                                    fg = "blue",
                                    font = ("Courier", "15"))
        self.lbl_scorelbl.grid(row = 5, column = 0, sticky = "news")
        
        self.score = tk.IntVar()
        self.score.set(0)
        
        self.lbl_scores = tk.Label(self, textvariable =self.score,
                                  bg = "blue", fg = "white",
                                font = ("Courier", "15"))
        self.lbl_scores.grid(row = 6, column = 0,
                             sticky  ="news")
        
        
        
        self.btn_submit = tk.Button(self, text = "Next Question",
                                    bg = "black", fg = "white",
                                    state = "disabled",
                                    command = self.reset_question,
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
    
    def reset_score(self):
        self.score.set(0)
        self.update()
        
    def update(self):
        
        if Question.section == 5:
            r_questions = []
            for i in range(1, 11):
                Question.section = rnd.randint(1,4)
                Question.question = rnd.randint(1, 10)
                r_questions.append(questions[Question.section][Question.question][0])
            
        self.text.set(questions[Question.section][Question.question][0])
        
        self.first.set(answers[Question.section][Question.question][0])
        self.second.set(answers[Question.section][Question.question][1])
        self.third.set(answers[Question.section][Question.question][2])
        self.fourth.set(answers[Question.section][Question.question][3])  
        
        self.btn_option1.configure(bg = "white", state = "normal")
        self.btn_option2.configure(bg = "white", state = "normal")
        self.btn_option3.configure(bg = "white", state = "normal")
        self.btn_option4.configure(bg = "white", state = "normal")
        self.btn_submit.configure(bg = "black", fg = "white", state = "disabled")   
             
        
        
        
    def selected_first(self):        
        correct_answer = (questions[Question.section][Question.question][1])
        
        if self.first.get() == correct_answer:
            self.btn_option1.configure(bg = "green")
            self.score.set(self.score.get() + 1000) 
            Question.streak +=1
            self.score.set(self.score.get() * (1 + (Question.streak*.1))) 
            self.score.set(round(self.score.get(), 1))
            
        else:
            self.btn_option1.configure(bg = "red")
            Question.streak = 0
            
            if self.second.get() == correct_answer:
                self.btn_option2.configure(bg = "green")
                
            elif self.third.get() == correct_answer:
                self.btn_option3.configure(bg = "green") 
            
            elif self.fourth.get() == correct_answer:
                self.btn_option4.configure(bg = "green")
                
        self.continue_to_next()
                
    def selected_second(self):
        correct_answer = (questions[Question.section][Question.question][1])
        
        if self.second.get() == correct_answer:
            self.btn_option2.configure(bg = "green")
            self.score.set(self.score.get() + 1000) 
            Question.streak +=1
            self.score.set(self.score.get() * (1 + (Question.streak*.1))) 
            self.score.set(round(self.score.get(), 1))
            
        else:
            self.btn_option2.configure(bg = "red")
            Question.streak = 0
            
            if self.first.get() == correct_answer:
                self.btn_option1.configure(bg = "green")
                
            elif self.third.get() == correct_answer:
                self.btn_option3.configure(bg = "green") 
            
            elif self.fourth.get() == correct_answer:
                self.btn_option4.configure(bg = "green")     
                  
        self.continue_to_next()
        
    def selected_third(self):        
        correct_answer = (questions[Question.section][Question.question][1])
        
        if self.third.get() == correct_answer:
            self.btn_option3.configure(bg = "green")
            self.score.set(self.score.get() + 1000) 
            Question.streak +=1
            self.score.set(self.score.get() * (1 + (Question.streak*.1)))
            self.score.set(round(self.score.get(), 1))
            
        else:
            self.btn_option3.configure(bg = "red")
            Question.streak = 0
            
            if self.second.get() == correct_answer:
                self.btn_option2.configure(bg = "green")
                
            elif self.first.get() == correct_answer:
                self.btn_option1.configure(bg = "green") 
            
            elif self.fourth.get() == correct_answer:
                self.btn_option4.configure(bg = "green") 
                
        self.continue_to_next()
                
    def selected_fourth(self):
     
        
        correct_answer = (questions[Question.section][Question.question][1])
        
        if self.fourth.get() == correct_answer:
            self.btn_option4.configure(bg = "green")
            self.score.set(self.score.get() + 1000) 
            Question.streak +=1
            self.score.set(self.score.get() * (1 + (Question.streak*.1)))    
            
            
        else:
            self.btn_option4.configure(bg = "red")
            Question.streak = 0
            
            if self.second.get() == correct_answer:
                self.btn_option2.configure(bg = "green")
                
            elif self.third.get() == correct_answer:
                self.btn_option3.configure(bg = "green") 
            
            elif self.first.get() == correct_answer:
                self.btn_option1.configure(bg = "green")  
                
        self.continue_to_next() 
        
                
    def continue_to_next(self):
        self.btn_option1.configure(state = "disabled")
        self.btn_option2.configure(state = "disabled")
        self.btn_option3.configure(state = "disabled")
        self.btn_option4.configure(state = "disabled")
        self.btn_submit.configure(bg = "yellow", fg = "black", state = "normal")
        
        
    def reset_question(self):
        Question.question += 1
        if Question.question > 10:
            print("NEXT SCREEN")        
        else:            
            self.update()
            
class FinalScreen(Screen):
    def __init__(self):
        
        Screen.__init__(self)     

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
    
    pickle_file = open("choices.pickle", "rb")
    answers = p.load(pickle_file)  
    pickle_file.close()       
    
    root = tk.Tk()
    #root.geometry("500x500")
    root.title("Trivia Game")
    root.grid_columnconfigure(0, weight = 1)
    root.grid_rowconfigure(0, weight = 1)    
    
    
    screens = []
    
    screens.append(MainMenu())    #screens[0]  
    screens.append(Question())    #screens[1]  
    screens.append(FinalScreen()) #screens[2]
  
    screens[0].grid(row = 0, column = 0, sticky = "news")  
    screens[1].grid(row = 0, column = 0, sticky = "news")
    
    Screen.current = 0
    Screen.switch_frame()    

    root.mainloop()
    
    