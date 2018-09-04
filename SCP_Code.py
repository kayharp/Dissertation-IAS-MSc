# -*- coding: utf-8 -*-
"""
Created on Thu Jul 26 11:58:45 2018
File holds functions relevent to creating subtractive conditional probability - cohesion estimates. 

@author: Kristina Harper
"""

# Import Libraries
import pandas as pd
import sys
import csv
import matplotlib.pyplot as plt
from scipy import stats
from collections import Counter

'''Find number of markers in reply messages. Start with 'E'  - twitter specific marker. For [p(B)] portion '''
def countMarkers(marker, message_set):
    tally = 0
    for countItem in message_set:
        if marker in countItem:
            tally+=1
    return tally

'''Count all items in the count dictionaries'''
def countAll(countdict):
    tally = 0
    for oneline in countdict:
        for item in oneline:
            tally+=1
    return tally
	
'''
Minuend in subtractive conditional probability measure: Validation of stylistic cohesion on certain markers
The fraction of all turns in which both tweets exhibit dimension C where tc denotes condition that a tweet t exhibits c. 
'''' 
def getMinuendCohesion(marker,allsharedmarkers):
	numTweetsWMarker = countMarkers(marker,allsharedmarkers)
	allTurns = len(allsharedmarkers)
	return (numTweetsWMarker/allTurns)

'''
Subtrahend gets a baseline usage of using a marker across the dataset. Calculates the probability of a marker being shared between a tweet and a randomized reply
'''
def getSubtrahendCohesion(marker,shuffledshared):
	numTweetsWMarker = countMarkers(marker,shuffledshared)
	allTurns = len(shuffledshared)
	return (numTweetsWMarker/allTurns)



'''
	This function was used to generate a csv file of shared markers between the a_tweets and randomized control tweets, and is much
    faster than the above function. 
    Inputs are list items. 
	
'''
def getSharedMarkers(ATweet,BTweet):
	sharedMarkers = []
	for i in range(len(ATweet)):
		tempmarker = []
		for tag in ATweet[i]:
			if tag in BTweet[i]:
				tempmarker.append(tag)
		sharedMarkers.append(tempmarker)
	return sharedMarkers


'''
	Code calculates the cohesions scores for two lists of markers: One list of shared markers between a_tweets and b_tweets,
	and the other between a_tweets and the shuffled b_tweets (acts as a control). 
'''
def CalculateAllCohesion(marks,markerdict,shuffledSharedMarkers):
    allcohesion = {}
    for mark in marks: 
        firstTerm = getMinuendCohesion(mark,markerdict)
        secondTerm = getSubtrahendCohesion(mark,shuffledSharedMarkers)
        CohesionScore = firstTerm-secondTerm
        allcohesion[mark] = [firstTerm,secondTerm,CohesionScore]
    return allcohesion
	
'''
Get the statistical significance as 'p-value' of the twitter data
'''
def getFishersPVal(countdictA,countdictB,sharedMarkers,markerset):
	PValScore = {}
	for marker in markerset:
		allMarkersB = countMarkers(marker,countdictB) # get all marker in BTweet
		k1 = countMarkers(marker,sharedMarkers)	# get all markers in a and B 
		k2 = allMarkersB - k1	# get number of B markers without A 
		n1 = countMarkers(marker,countdictA) # get number of A markers 
		n2 = len(countdictA) - n1	# get number of tweets in A without marker
		odds,pval = stats.fisher_exact([[n1,k1],[n2,k2]])
		PValScore[marker] = pval
	return PValScore



