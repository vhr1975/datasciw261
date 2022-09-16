#!/usr/bin/env python
"""
Reducer to calculate precision and recall as part
of the inference phase of Naive Bayes.
INPUT:
    ID \t true_class \t P(ham|doc) \t P(spam|doc) \t predicted_class
OUTPUT:
    precision \t ##
    recall \t ##
    accuracy \t ##
    F-score \t ##
         
Instructions:
    Complete the missing code to compute these^ four
    evaluation measures for our classification task.
    
    Note: if you have no True Positives you will not 
    be able to compute the F1 score (and maybe not 
    precision/recall). Your code should handle this 
    case appropriately feel free to interpret the 
    "output format" above as a rough suggestion. It
    may be helpful to also print the counts for true
    positives, false positives, etc.
"""
import sys

# initialize counters
FP = 0.0 # false positives
FN = 0.0 # false negatives
TP = 0.0 # true positives
TN = 0.0 # true negatives

# read from STDIN
for line in sys.stdin:
    # parse input
    docID, class_, pHam, pSpam, pred = line.split()
    # emit classification results first
    print(line[:-2], class_ == pred)
    
    # then compute evaluation stats
#################### YOUR CODE HERE ###################

# sample data
# d5	1	-8.90668134500626	-8.10769031284611	1
# d6	1	-5.780743515794329	-4.179502370564408	1
# d7	0	-6.591673732011658	-7.511706880737812	0
# d8	0	-4.394449154674438	-5.565796731681498	0
# d5	1	-8.90668134500626	-8.10769031284611	 True
# d6	1	-5.780743515794329	-4.179502370564408	 True
# d7	0	-6.591673732011658	-7.511706880737812	 True
# d8	0	-4.394449154674438	-5.565796731681498	 True























#################### (END) YOUR CODE ###################
    