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
                   4:{1:["Wario", "Jumpman", "Hammer Bro", "Luigi"], 
                      2:["Pong", "Pitfall", "Pac-Man", "Tennis for Two"],
                      3:["Ice", "Steel", "Grass", "Water"], 
                      4:["Sam Fisher", "Jason Bourne", "Solid Snake", "Agent 47"], 
                      5:["Cloud", "Ms.Pac-Man", "Captain Falcon", "Solid Snake"], 
                      6:["Hotel Mario", "Jimmie Johnson's Anything with an Engine", "Banjo-Kazooie: Grunty's Revenge", "Spyro Bandicoot: Spinnin'"], 
                      7:["Play Station 2", "Gamecube", "Xbox", "Dreamcast"], 
                      8:["Nathan", "Ryan", "John", "Dylan"], 
                      9:["Yoshi's Island", "Super Mario World", "Mario is Missing", "Yoshi's Cookie"], 
                      10:["League of Legends", "World of Warcraft", "Call of Duty", "Fortnite"]}}


datafile = open('choices.pickle', 'wb')
p.dump(multiple_choice, datafile)
datafile.close()

