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
                      5:["Caspian Sea", "Persian Gulf", "The White Sea", "Baltic Sea"], 
                      6:["Mount Fuji", "Mount Yasur", "Mount Olympus", "Mount Etna"], 
                      7:["Nihoa", "Hulu", "Oahu", "Lanai"], 
                      8:["El Paso", "Austin", "Nacogdoches", "San Antonio"], 
                      9:["Texas", "Missouri", "Alabama", "Florida"], 
                      10:["Montana", "Wyoming", "Rhode Island", "Nevada"]}, 
                   2:{1:["Red/Blue/White", "Red/White/Green", "Black/Red/Yellow", "Orange/Green/White"], 
                      2:["Abraham Lincoln", "George Washington", "Donald Trump", "James Madison"], 
                      3:["Assyrian", "Egyptian", "Babylonian", "Kushite"], 
                      4:["Civil War", "World War II", "The Vietnam War", "The Korean War"], 
                      5:["<1", "2.5", "7", "21"], 
                      6:["2", "4", "9", "1"], 
                      7:["Millard Fillmore", "Andrew Jackson", "William Harrison", "Zachary Taylor"], 
                      8:["Hades", "Demeter", "Poseidon", "Artemis"], 
                      9:["0", "1", "7", "1000"], 
                      10:["China", "USA", "Spain", "Greece"]}, 
                   3:{1:["Piano", "Flute", "Guitar", "Violin"], 
                      2:["Heartbreak Hotel", "Tutti-Frutti", "That's All Right", "Rock Around the Clock"], 
                      3:["Christina Aguliera", "Madonna", "Britney Spears", "Beyonce"], 
                      4:["Ringo Starr", "George Harrison", "Paul McCartney", "John Lennon"], 
                      5:["David Bowie", "Elivs Presley", "Bob Marley", "Madonna"], 
                      6:["dad", "friends", "dog", "vibe"], 
                      7:["Love Me Tender", "Hound Dog", "Heartbreak Hotel", "Are You Lonesome Tonight"], 
                      8:["four", "seven", "three", "five"], 
                      9:["Dog/Dad", "Friends/Food", "Bed/Mama", "Python/Java"], 
                      10:["cool", "neat", "ROCK", "swag"]}, 
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

