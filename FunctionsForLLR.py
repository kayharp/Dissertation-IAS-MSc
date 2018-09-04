'''
	Functions for implementation of LLR - Log likelihood ratio 
	Author: Kristina Harper
	Date: 29/08/2018
'''
import numpy as np

'''
	Function to return the list of shared markers between two tweets
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
	Find number of markers in messages. Functions when a count dict is passed as argument. Checking for simple presence or absence. 
'''
def countMarkers(marker, message_set):
    tally = 0
    for countItem in message_set:
        if marker in countItem:
            tally+=1
    return tally
	
'''
	Implementation of LLR. Takes as arguments two lists of counter items of POS tags per tweet and reply, 
	a list of lists of shared markers, and the set of POS markers we're testing. 
	ex. countdictB[0] = Counter({'V': 8, 'O': 4, 'N': 3, 'L': 1, 'P': 4, ',': 2, '^': 2, '&': 1})
	sharedMarkers[0:2] = [['V', 'O', 'N', 'P', ',', '^'], ['V', 'O', 'N', 'P', ',']]
	markerset[0] = 'V'
	'''	
def getLLR(countdictA,countdictB,sharedMarkers,markerset):
	LLRStore = {}
	for marker in markerset: 
		allMarkerInstancesB = countMarkers(marker,countdictB)
		k1 = countMarkers(marker,sharedMarkers)
		k2 = allMarkerInstancesB - k1
		n1 = countMarkers(marker,countdictA)
		n2 = len(countdictA) - n1
		#print('AMarker - N1: ',n1,' ANoMarker - N2: ',n2)
		p1 = k1/n1
		p2 = k2/n2
		p = (k1+k2)/(n1+n2)
		logl1 = k1*np.log(p1) + (n1-k1)*np.log(1-p1)
		logl2 = k2*np.log(p2) + (n2-k2)*np.log(1-p2)
		logl3 = k1*np.log(p) + (n1-k1)*np.log(1-p)
		logl4 = k2*np.log(p) + (n2-k2)*np.log(1-p)
		LLR = 2*(logl1 + logl2 - logl3 - logl4)
		LLRStore[marker] = LLR
	return LLRStore
	
