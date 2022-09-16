#!/usr/bin/env python
import re                                                   
import sys                                                  
import numpy as np      
from operator import itemgetter
import os
import string

# TODO track all the reauired totals
cur_word = None
class0Count = 0
class1Count = 0
class0Total = 0
class1Total = 0
class0WordTot = 0
class1WordTot = 0
corpusTotal = 0
count = 0

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
            
            # current_count += count
            # get word total count
            class0Count += class0_partialCount
            class1Count += class1_partialCount
            
        else:
            
            if cur_word:
                
                # calculate all the marginals before we use them in the denominator to calculate the conditional probabilities of our training set.
                class0prob = (class0Count + 1) / float(class0WordTot)
                class1prob = (class1Count + 1) / float(class1WordTot)

                # write result to STDOUT
                # print(f'{cur_word}\t{class0Count},{class1Count},{class0prob},{class1prob}')
                
                count += 1
                
            cur_word = word

count += 1 

print(f'{"totalWordCount"}\t{count}')
    