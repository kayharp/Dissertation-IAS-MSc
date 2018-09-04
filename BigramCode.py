# -*- coding: utf-8 -*-
"""
Created on Thu Jul 26 11:58:45 2018
File holds bigram-relevent functions - generating them from tagged tweets in dataframe.

@author: Kristina Harper
"""

# Import Libraries


from collections import Counter

'''
Function to take a dataframe of tweet tags and put them as a list. 
'''
def dfToTagLists(tagLists):
    functionalList = []
    for taglist in tagLists:
        functionalList.append(list(taglist))
    return functionalList

'''
 Function to take a list of tags as strings with spaces in between 
 and remove the space items, returning a list of list of tags corresponding to tweet pos syntax. 
'''
def cleanuplist(tweets):
    cleaned = []
    #print('CleanListfunction')
    for item in tweets:
        #print('Item: ',item)
        temp = []
        for tag in item:
            #temp = []
            temp.append(tag)
            if ' ' in temp: 
                temp.remove(' ')
        #print('Temp: ',temp)
        cleaned.append(temp)
    return cleaned

'''
Create bigrams from an input of tags in list form, with empty space removed. returns a list of lists (2 tags
paired)
'''
def createBigrams(tagList):
    #bigramList = []
    return list(map(list,zip(tagList,tagList[1:])))

'''
Function to remove duplicate bigrams from list 
'''
def cleanBigrams(bigramlist):
    newlist = []
    for item in bigramlist:
        if item not in newlist:
            newlist.append(item)
    return newlist

'''
Put together lots of functions to take raw tweet tags and output a list of all bigrams in tagged tweets
'''
def AllBigramsinTweetset(tweets):
    val = dfToTagLists(tweets) # Output list of lists of tweet-tags
    #print(val)
    val2 = cleanuplist(val) # Output list of list of tweet-tags with spaces removed
    #print(val2)
    bigramsforAllTweets = []
    for listitem in val2: 
        z = cleanBigrams(createBigrams(listitem)) # Creates bigrams and removes duplicates
        bigramsforAllTweets.append(z)
    return bigramsforAllTweets 

''' 
Function takes as input pairset1 - a list of bigrams organized into lists corresponding to tweets, and
pairset2 - the same. The output is a list of shared bigrams between indexed tweets (ex the first item in the 
list will be the shsared bigram parts of speech tags in the first tweet-reply pair in the dataset. )
'''
def checksharedbigrams(pairset1,pairset2):
    sharedset = []
    for i in range(len(pairset1)):
        temp = []
        #print('I: ',i)
        for item in pairset1[i] :
            #print('A: ',item)
            if item in pairset2[i]:
                #print('Corresponding tagset in b: ',pairset2[i])
                temp.append(item)
                #print('Temp: ',temp)
        sharedset.append(temp)
    return sharedset

'''
Convert list of bigram lists to list of bigram tuples
'''
def convertToTuples(bigramList):
    tempBigrams = []
    for item in bigramList:
        templist = []
        for pair in item:
            t = tuple(pair)
            templist.append(t)
        tempBigrams.append(templist)
    return tempBigrams


# Function to generate count list of bigrams appearing in each tweet. 
def countFreqBigrams(bigramlist):
    bigramCtList = []
    count = Counter(bigramlist)
    bigramCtList.append(count)

