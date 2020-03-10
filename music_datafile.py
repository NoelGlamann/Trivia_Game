#!/usr/bin/python3
#Noel Glamann
#28 January 2020

''' data file for movie library file '''

import pickle as p


'''just so i do not forget:
          the list following the # key in the dictionary is-
          
          0. name
          1. score
        
'''

music_scores = {1:['name', 'score'], 2:['name', 'score'], 3:['name', 'score']}

datafile = open('music.pickle', 'wb')
p.dump(music_scores, datafile)
datafile.close()

