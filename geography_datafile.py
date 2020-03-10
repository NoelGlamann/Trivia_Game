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

geography_scores = {1:['name', 'score'], 2:['name', 'score'], 3:['name', 'score']}

datafile = open('geography.pickle', 'wb')
p.dump(geography_scores, datafile)
datafile.close()

