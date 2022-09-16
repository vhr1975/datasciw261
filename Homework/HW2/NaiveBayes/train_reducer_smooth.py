#!/usr/bin/env python
"""
Reducer aggregates word counts by class and emits frequencies.

INPUT:
    partitionKey \t word \t class0_partialCount,class1_partialCount
OUTPUT:
    word \t class0_count,class1_count,class0_condProb,class1_condProb
    
Instructions:
    Again, you are free to design a solution however you see 
    fit as long as your final model meets our required format
    for the inference job we designed in Question 8. Please
    comment your code clearly and concisely.
    
    A few reminders: 
    1) Don't forget to emit Class Priors (with the right key).
    2) In python2: 3/4 = 0 and 3/float(4) = 0.75
"""
##################### YOUR CODE HERE ####################
# reducer requirements
# the reducer will need access to the total number of terms in each class.
# the priors, the reducer will need access to the total number of documents in each class 
# as well as the total number of documents in the corpus.

# calculate all the marginals before we use them in the denominator to calculate the conditional probabilities of our training set.
# we have access to all of the totals before any other data. We can tally these up. 
# add up all the terms for the classes. And now that we have these marginals available, we can calculate the conditional probabilities of each word. 
# And this constitutes our model file. Our reducer is going to emit the model file.
# Q8 b with no smoothing.

# sample test file
# A	**doc_total	2,2
# A	**word_total	6,8
# A	beijing	0,1
# A	chinese	0,1
# A	chinese	0,1
# A	chinese	0,1
# A	japan	0,1
# A	japan	1,0
# A	japan	1,0
# A	macao	1,0
# A	shanghai	0,1
# A	tokyo	0,1
# A	tokyo	1,0
# A	tokyo	1,0
# A	trade	0,1
# A	trade	1,0

import re                                                   
import sys                                                  
import numpy as np      
from operator import itemgetter
import os

# TODO track all the reauired totals
cur_word = None
class0Count = 0
class1Count = 0
class0Total = 0
class1Total = 0
class0WordTot = 0
class1WordTot = 0
corpusTotal = 0
# size = 6

# note: the partitions are the key-value pairs of intermediate Map-outputs. 
# It partitions the data using a user-defined condition, which works like a hash function. 
# The total number of partitions is same as the number of Reducer tasks for the job.
# the total word count has been written to a file. the smooth mapper must now read in the total word count from the file on disk

# print(os.listdir('.'))

# assert 'NB_total_word_count.txt' in os.listdir('.'), "ERROR: can't find NB_total_word_count.txt"

# Local Disk/media/notebooks/Assignments/HW2/NaiveBayes/NB_total_word_count.txt
# f = open('./NaiveBayes/NB_total_word_count.txt', 'r')
f = open('NB_total_word_count.txt', 'r')

# TODO write a function
for x in f:
    # print(x)
    # parse input
    word, size = x.strip().split('\t')
    # print(word)
    # print(size)

# cast string to float
size = float(size)
    
# read from standard input
for line in sys.stdin:
    
    # parse input
    partitionKey, word, partialCounts = line.strip().split('\t')
    
    # split the keys, words and counts into individual parts
    class0_partialCount, class1_partialCount = partialCounts.split(',')
        
    # hint includes: In python2: 3/4 = 0 and 3/float(4) = 0.75
    # cast values to float
    class0_partialCount = float(class0_partialCount)
    class1_partialCount = float(class1_partialCount)
    
    # the reducer will need access to the total number of terms in each class. get totals below    
    # if word is **doc_total
    if word == "**doc_total":
    
        # get doc total count
        class0Total += class0_partialCount
        class1Total += class1_partialCount
        
    # else if word is **word_total
    elif word == "**word_total":
        
        # get word total count
        class0WordTot += class0_partialCount
        class1WordTot += class1_partialCount
    
    # else process the words
    else:
        
        # TODO update the following logic
        if word == cur_word: 
            
            # get word total count
            class0Count += class0_partialCount
            class1Count += class1_partialCount
            
        else:
            
            if cur_word:
                
                # calculate all the marginals before we use them in the denominator to calculate the conditional probabilities of our training set.
                class0prob = (class0Count + 1) / float(class0WordTot + size)
                class1prob = (class1Count + 1) / float(class1WordTot + size)

                # write result to STDOUT
                print(f'{cur_word}\t{class0Count},{class1Count},{class0prob},{class1prob}')
                
            
            cur_word = word
            class0Count = class0_partialCount
            class1Count = class1_partialCount
            

class0prob = (class0Count + 1) / (float(class0WordTot + size))
class1prob = (class1Count + 1) / (float(class1WordTot + size))

print(f'{cur_word}\t{class0Count},{class1Count},{class0prob},{class1prob}')
            
            
#print ClassPriors
if partitionKey == 'A':
    
    corpusTotal = class0Total + class1Total
    class0prob = class0Total/float(corpusTotal)
    class1prob = class1Total/float(corpusTotal)
    print(f'{"ClassPriors"}\t{class0Total},{class1Total},{class0prob},{class1prob}')
            
##################### (END) CODE HERE ####################
