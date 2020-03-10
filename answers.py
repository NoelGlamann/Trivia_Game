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

multiple_choice = {1:{1:["Europe", "Asia", "North America", "Africa"], 
                      2:["22%", "100%", "52%", "84%"], 
                      3:["Ethiopia", "Nigeria", "Egypt", "Tunisia"],
                      4:["London", "Istanbul", "New Delhi", "Rome"], 
                      5:["", "", "", ""], 
                      6:["", "", "", ""], 
                      7:["", "", "", ""], 
                      8:["", "", "", ""], 
                      9:["", "", "", ""], 
                      10:["", "", "", ""]}, 
                   2:{1:["Red/Blue/White", "Red/White/Green", "Black/Red/Yellow", "Orange/Green/White"], 
                      2:["", "", "", ""], 
                      3:["", "", "", ""], 
                      4:["", "", "", ""], 
                      5:["", "", "", ""], 
                      6:["2", "4", "9", "1"], 
                      7:["", "", "", ""], 
                      8:["", "", "", ""], 
                      9:["", "", "", ""], 
                      10:["", "", "", ""]}, 
                   3:{1:["", "", "", ""], 
                      2:["", "", "", ""], 
                      3:["", "", "", ""], 
                      4:["", "", "", ""], 
                      5:["", "", "", ""], 
                      6:["", "", "", ""], 
                      7:["", "", "", ""], 
                      8:["", "", "", ""], 
                      9:["", "", "", ""], 
                      10:["", "", "", ""]}, 
                   4:{1:["", "", "", ""], 
                      2:["", "", "", ""],
                      3:["", "", "", ""], 
                      4:["", "", "", ""], 
                      5:["", "", "", ""], 
                      6:["", "", "", ""], 
                      7:["", "", "", ""], 
                      8:["", "", "", ""], 
                      9:["", "", "", ""], 
                      10:["", "", "", ""]}}


datafile = open('choices.pickle', 'wb')
p.dump(multiple_choice, datafile)
datafile.close()

