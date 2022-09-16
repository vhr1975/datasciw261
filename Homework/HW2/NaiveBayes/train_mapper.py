#!/usr/bin/env python
"""
Mapper reads in text documents and emits word counts by class.
INPUT:                                                    
    DocID \t true_class \t subject \t body                
OUTPUT:                                                   
    partitionKey \t word \t class0_partialCount,class1_partialCount       
    

Instructions:
    You know what this script should do, go for it!
    (As a favor to the graders, please comment your code clearly!)
    
    A few reminders:
    1) To make sure your results match ours please be sure
       to use the same tokenizing that we have provided in
       all the other jobs:
         words = re.findall(r'[a-z]+', text-to-tokenize.lower())
         
    2) Don't forget to handle the various "totals" that you need
       for your conditional probabilities and class priors.
       
Partitioning:
    In order to send the totals to each reducer, we need to implement
    a custom partitioning strategy.
    
    We will generate a list of keys based on the number of reduce tasks 
    that we read in from the environment configuration of our job.
    
    We'll prepend the partition key by hashing the word and selecting the
    appropriate key from our list. This will end up partitioning our data
    as if we'd used the word as the partition key - that's how it worked
    for the single reducer implementation. This is not necessarily "good",
    as our data could be very skewed. However, in practice, for this
    exercise it works well. The next step would be to generate a file of
    partition split points based on the distribution as we've seen in 
    previous exercises.
    
    Now that we have a list of partition keys, we can send the totals to 
    each reducer by prepending each of the keys to each total.
       
"""

# notes
# reducer requirements
# the reducer will need access to the total number of terms in each class.
# the priors, the reducer will need access to the total number of documents in each class 
# as well as the total number of documents in the corpus.

import re                                                   
import sys                                                  
import numpy as np      

from operator import itemgetter
import os

#################### YOUR CODE HERE ####################

GLOBAL_TOTAL_HAM_DOCS = 0
GLOBAL_TOTAL_SPAM_DOCS = 0
GLOBAL_TOTAL_HAM_WORDS = 0
GLOBAL_TOTAL_SPAM_WORDS = 0


if os.getenv('mapreduce_job_reduces') == None:
    N = 1
else:
    N = int(os.getenv('mapreduce_job_reduces'))
    
def makeKeyHash(key, num_reducers = N):
    """
    Mimic the Hadoop string-hash function.
    
    key             the key that will be used for partitioning
    num_reducers    the number of reducers that will be configured
    """
    byteof = lambda char: int(format(ord(char), 'b'), 2)
    current_hash = 0
    for c in key:
        current_hash = (current_hash * 31 + byteof(c))
    return current_hash % num_reducers

# helper function
def makeKeyFile(num_reducers = N):
    KEYS = list(map(chr, range(ord('A'), ord('Z')+1)))[:num_reducers]
    partition_keys = sorted(KEYS, key=lambda k: makeKeyHash(k,num_reducers))
    return partition_keys

# call your helper function to get partition keys
pKeys = makeKeyFile() 

# read from standard input
for line in sys.stdin:
    
    # parse input and tokenize
    docID, _class, subject, body = line.lower().split('\t')    
    words = re.findall(r'[a-z]+', subject + ' ' + body)
        
    # print (docID) 
    # print (_class) 
    # print (subject) 
    # print (body) 
    # data:
    # 0
    # 1
    # 1
    # 1
    # d1
    # d2
    # d3
    # d4
    # chinese  beijing  chinese
    # chinese  chinese  shanghai
    # tokyo    japan    chinese
    # chinese  macao
    
    # loop all the words
    for word in words:
        
        class0_partialCount = 0
        class1_partialCount = 0
        
        # logic to check for in or out of class
        if int(_class) == 0:
            
            # NOT in Spam class
            class0_partialCount = 1
            GLOBAL_TOTAL_HAM_WORDS += 1
            
        else:
            
            # in Spam class
            class1_partialCount = 1
            GLOBAL_TOTAL_SPAM_WORDS += 1
            
        # partition indices for keys: A,B,C..Z; with up to 26 partitions
        partition_index = makeKeyHash(word)
        # call your helper function to get partition keys A - Z
        partitionKey = pKeys[partition_index]
        
        # print out the current class count
        # OUTPUT:
        # partitionKey \t word \t class0_partialCount,class1_partialCount
        print(f'{partitionKey}\t{word}\t{class0_partialCount},{class1_partialCount}')
        
        # end of for word loop
    
    # if else logic to track if doc is in class
    if int(_class) == 0:
        
        # increment global doc ham counter
        GLOBAL_TOTAL_HAM_DOCS += 1
    
    else:
        
        # increment global doc Spam counter
        GLOBAL_TOTAL_SPAM_DOCS += 1
    
# loop all the keys and print
for key in pKeys:
    # -> partitionKey \t word \t class0_partialCount,class1_partialCount   
    print(f'{key}\t{"**doc_total"}\t{GLOBAL_TOTAL_HAM_DOCS},{GLOBAL_TOTAL_SPAM_DOCS}')
    print(f'{key}\t{"**word_total"}\t{GLOBAL_TOTAL_HAM_WORDS},{GLOBAL_TOTAL_SPAM_WORDS}')
    
#################### (END) YOUR CODE ###################
