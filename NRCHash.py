#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep  2 17:27:33 2018

@author: kh414

Functions relevent to the calculation of Stylistic Accommodation under SCP - but can only be used for NRC at the moment because the column names of dataframes
are not yet standardized. 

To Do: Standardize dataframe titles so code is less redundant. 

"""

import numpy as np
import SCP_Code as scp


'''
    Iterate through the dataframe to compile a list of tweet-reply pairs corresponding to a single user and return that list of tweets, replies, and that T-R's shared markers
    to calculate the accommodation score of a specific user. 
'''
def UNIterateforSCPPairScore(dataframe,userPair,shared):
    tempA = []
    tempB = []
    tempsh = []
    for num in range(len(dataframe)):
        if dataframe['Pairs'][num] == userPair: # check to see if the row matches UN pairs to be calc.
            tempA.append(dataframe['ASent'][num])
            tempB.append(dataframe['BSent'][num])
            tempsh.append(shared[num])
    return([tempA,tempB,tempsh])


'''
    Get accommodation score; this is the score called upon by FullForm
'''
def calculateAccom(markerset,UNTweetTagsA,UNTweetTagsB,SharedABTags):
    minDict= {}
    for marker in markerset:
        minDict[marker] = getMin(marker,UNTweetTagsB)
        marker2 = str(marker)+'2' # Easy way to record both minuend and subtrahend scores in one dictionary
        minDict[marker2] = getSub(marker,UNTweetTagsA,SharedABTags)
    return minDict


'''
    Get Minuend 
'''
def getMin(marker,listB):
    numerator = scp.countMarkers(marker,listB)#b's replies to A in which marker is present
    denom = len(listB) # number of b's replies to A
    if denom == 0:
        return np.nan
    else:
        return (numerator/denom)


'''
    Get Subtrahend 
'''
def getSub(marker,listA,shared):
    numerator = scp.countMarkers(marker,shared) #b and a show marker
    denom = scp.countMarkers(marker,listA) # a shows marker
    if denom == 0:
        return np.nan
    else:
        return(numerator/denom)

'''
    Get accommodation
'''
def getAcc(marker,listA,listB,shared):
    minuend = getMin(marker,listB)
    subtrahend = getSub(marker,listA,shared)
    if subtrahend == 0:
        return np.nan
    else:
        return([minuend,subtrahend])

'''
    This function calls upon the others above to determine a dictionary of username accommodation scores. 
'''
def fullForm(usernameList,dataframe,markers,shared):
    minDict = {}
    for userPair in usernameList:
        temp = UNIterateforSCPPairScore(dataframe,userPair,shared)  # temp consists of [A_lst,B_lst,Shared]
        minDict[userPair] = calculateAccom(markers,temp[0],temp[1],temp[2])
    return minDict

'''
    Input is a dataframe of tags which are split. 
'''
def getSharedMarkers(ATweet,BTweet):
	sharedMarkers = []
	for i in range(len(ATweet)):
		tempmarker = []
		for tag in ATweet[i].split():
			if tag in BTweet[i].split() and (tag not in tempmarker):
				tempmarker.append(tag)
		sharedMarkers.append(tempmarker)
	return sharedMarkers