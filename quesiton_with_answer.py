#!/usr/bin/python3
#Noel Glamann
#28 January 2020

''' data file for movie library file '''

import pickle as p


'''just so i do not forget:
          the list following the # key in the dictionary is-
          
         1 - geography questions
         2 - history quesitons
         3 - music quesions
         4 - video game questions
         
'''

question_answer = {1:{1:["What is the Earth's largest continent?", "Asia"], 
                      2:["What percent of the River Nile runs through Egypt?", "22%"], 
                      3:["What African country sreved as the setting for Tatooine in Star Wars?", "Tunisia"], 
                      4:["What is the only major city located on two continents?", "Istanbul"], 
                      5:["question", "answer"], 
                      6:["question", "answer"], 
                      7:["question", "answer"], 
                      8:["question", "answer"], 
                      9:["question", "answer"], 
                      10:["question", "answer"]}, 
                   2:{1:["What three colors appear on the Italian flag?", "Red/White/Green"], 
                      2:["question", "answer"], 
                      3:["question", "answer"], 
                      4:["question", "answer"], 
                      5:["question", "answer"], 
                      6:["How many US presidents have been assassinated?", "4"], 
                      7:["question", "answer"], 
                      8:["question", "answer"], 
                      9:["question", "answer"], 
                      10:["question", "answer"]}, 
                   3:{1:["question", "answer"], 
                      2:["question", "answer"], 
                      3:["question", "answer"], 
                      4:["question", "answer"], 
                      5:["question", "answer"], 
                      6:["question", "answer"], 
                      7:["question", "answer"], 
                      8:["question", "answer"], 
                      9:["question", "answer"], 
                      10:["question", "answer"]}, 
                   4:{1:["question", "answer"], 
                      2:["question", "answer"],
                      3:["question", "answer"], 
                      4:["question", "answer"], 
                      5:["question", "answer"], 
                      6:["question", "answer"], 
                      7:["question", "answer"], 
                      8:["question", "answer"], 
                      9:["question", "answer"], 
                      10:["question", "answer"]}}


datafile = open('questions.pickle', 'wb')
p.dump(question_answer, datafile)
datafile.close()

