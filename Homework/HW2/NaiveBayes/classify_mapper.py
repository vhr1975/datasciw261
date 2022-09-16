#!/usr/bin/env python
"""
Mapper for Naive Bayes Inference.
INPUT:
    ID \t true_class \t subject \t body \n
OUTPUT:
    ID \t true_class \t logP(ham|doc) \t logP(spam|doc) \t predicted_class
SUPPLEMENTAL FILE: 
    This script requires a trained Naive Bayes model stored 
    as NBmodel.txt in the current directory. The model should 
    be a tab separated file whose records look like:
        WORD \t ham_count,spam_count,P(word|ham),P(word|spam)
        
Instructions:
    We have loaded the supplemental file and taken the log of 
    each conditional probability in the model. We also provide
    the code to tokenize the input lines for you. Keep in mind 
    that each 'line' of this file represents a unique document 
    that we wish to classify. Fill in the missing code to get
    the probability of each class given the words in the document.
    Remember that you will need to handle the case where you
    encounter a word that is not represented in the model.
"""
import os
import re
import sys
import numpy as np

# confirm that we have access to the model file
assert 'NBmodel.txt' in os.listdir('.'), "ERROR: can't find NBmodel.txt"

# load the model into a dictionary for easy access
MODEL = {}
for record in open('NBmodel.txt', 'r').readlines():
    word, payload = record.split('\t')
    # extract conditional probabilities
    ham_cProb, spam_cProb = payload.split(',')[2:]
    # save their logs as a tuple in our model dictionary
    take_log = lambda x: np.log(x) if x != 0 else float("-inf")
    MODEL[word] = (take_log(float(ham_cProb)),
                   take_log(float(spam_cProb)))

# read from standard input
for line in sys.stdin:
    # parse input and tokenize
    docID, _class, subject, body = line.lower().split('\t')
    words = re.findall(r'[a-z]+', subject + ' ' + body)
    
    # initialize variables that student code should overwrite
    logpHam, logpSpam, pred_class = None, None, None
    
    ################# YOUR CODE HERE ################
    # TIP: try using MODEL.get(word, (0,0)) to access the tuple 
    # of log probabilities without throwing a KeyError!
    
    # notes
    # – P(A)  : prior probability, probability of A (reason) that is determined before the outcome is produced.
    # – P(B|A): likelihood probability, probability for an outcome B to occur given that reason A has occurred.
    # – P(A|B): posterior probability, probability for reason A to occur given that outcome B has occurred.
    # or
    # P(c|x) is the posterior probability of class (target) given predictor (attribute). 
    # P(c) is the prior probability of class. 
    # P(x|c) is the likelihood which is the probability of predictor given class. 
    # P(x) is the prior probability of predictor.
        
    # example MODEL data
    # {'beijing':  (-2.197224577337219,  -1.9459101490563133),  
    # 'chinese':  (-1.504077396777274,  -0.8472978603882036),  
    # 'tokyo':  (-1.504077396777274,  -2.6390573296148587),  
    # 'shanghai':  (-2.197224577337219,  -1.9459101490563133),  
    # 'ClassPriors':  (-1.3862943611198906,  -0.2876820724517809),      
    
    # using MODEL.get(word, (0,0)) to access the tuple of ClassPriors probabilities without throwing a KeyError!
    classPriorHam, classPriorSpam = MODEL.get("ClassPriors", (0,0))    
    
    # Fill in the missing code to get the probability of each class given the words in the document.
    # set the following: logpHam, logpSpam, pred_class
    logpHam = classPriorHam
    logpSpam = classPriorSpam    
    
    # loop all the word in the current class
    for word in words:
        
        conditionalProbHam, conditionalProbSpam = MODEL.get(word, (0,0))    
        logpHam = logpHam + conditionalProbHam
        logpSpam = logpSpam + conditionalProbSpam
        
        # add logic to confirm or not confirm Spam
        # set pred_class
        if logpHam >= logpSpam:
            
            # not Spam
            pred_class = 0
        
        else:
            
            #Spam
            pred_class = 1
                

    # ID \t true_class \t logP(ham|doc) \t logP(spam|doc) \t predicted_class

    ################# (END) YOUR CODE ##############
    
    print(f"{docID}\t{_class}\t{logpHam}\t{logpSpam}\t{pred_class}")
    