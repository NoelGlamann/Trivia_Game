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
                      5:["Which is the coldest sea on Earth?", "The White Sea"], 
                      6:["Which is the oldest active volcano on Earth?", "Mount Etna"], 
                      7:["What Hawaiian island is known as 'Bird Island'?", "Nihoa"], 
                      8:["What is the oldest city in Texas?", "Nacogdoches"], 
                      9:["What is the flattest U.S. state?", "Florida"], 
                      10:["Which is the least populated US state?", "Wyoming"]}, 
                   2:{1:["What three colors appear on the Italian flag?", "Red/White/Green"], 
                      2:["Who was president during the US Civil War?", "Abraham Lincoln"], 
                      3:["The Ptolemy dynasty ruled which ancient empire?", "Egyptian"], 
                      4:["Which war took place between 1950 and 1953?", "The Korean War"], 
                      5:["How long did the shortest war in human civilization last?", "<1"], 
                      6:["How many US presidents have been assassinated?", "4"], 
                      7:["Which president served the shortest term?", "William Harrison"], 
                      8:["Who is the Greek God of the Underworld?", "Hades"], 
                      9:["Van Gogh sold how many paintings in his life time?", "1"], 
                      10:["The Olympic Games originated in which country?", "Greece"]}, 
                   3:{1:["What is the oldest surviving musical instrument?", "Flute"], 
                      2:["What was the first rock-n-roll song to hit #1 on the charts?", "Rock Around the Clock"], 
                      3:["Who was rocketed to super-stardom in 1998 by the hit single 'Baby One More Time'?", "Britney Spears"], 
                      4:["Which Beatle had dyslexia?", "John Lennon"], 
                      5:["Who is NOT  a founding member of the UK Music Hall of Fame?", "David Bowie"], 
                      6:["'If you wanna be my lover, you gotta get with my _______' -Finish the Lyrics", "friends"], 
                      7:["What was Elvis Presley's first number one hit single on the Billboard Hot 100 charts?", "Heartbreak Hotel"], 
                      8:["How many strings from a violin have?", "four"], 
                      9:["'I tll her only partly, I only love my _____ and my ______, I'm sorry.' - Finish the Lyrics", "Bed/Mama"], 
                      10:["'IM A GOOFY GOOBER ______'-Finish the Lyrics", "ROCK"]}, 
                   4:{1:["What was Mario's origianl name?", "Jumpman"], 
                      2:["What was the title of the very first video game?", "Tennis for Two"],
                      3:["Which type of Pokemon is strong against Charmander?", "Water"], 
                      4:["Who is the main character in the Splinter Cell series?", "Sam Fisher"], 
                      5:["Which of the following is NOT a playable character in Super Smash Bros?", "Ms. Pac-Man"], 
                      6:["Which of the following isn't a real game?", "Spyro Bandicoot: Spinnin'"], 
                      7:["Which console came first?", "Dreamcast"], 
                      8:["What is Master Chief's first name?", "John"], 
                      9:["Yoshi first appeared in which game?", "Super Mario World"], 
                      10:["What is the most played online game in the world?", "League of Legends"]}}


datafile = open('questions.pickle', 'wb')
p.dump(question_answer, datafile)
datafile.close()

