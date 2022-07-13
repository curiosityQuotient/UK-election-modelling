# -*- coding: utf-8 -*-
"""
Script to analyse the results of the 2017 election to check sensitivity to randomness

@author: CuriosityQuotient
"""
# use file available at  https://researchbriefings.files.parliament.uk/documents/CBP-7979/HoC-GE2017-constituency-results.csv

import numpy as np
import pandas as pd
 
fp = '../Downloads/HoC-GE2017-constituency-results.csv'

resultFrame = pd.read_csv(fp)

# function to determine winner 
# looks are results columns and finds the one with the most votes
# assumes no draws
# returns: column with most votes
def findWinner(series):
    if series.iloc[15:].dtype != 'int':
        votes = series.iloc[15:].astype(int)
    else:
        votes = series.iloc[15:]
    winner = votes.idxmax()
    return winner
    
# check that function works on small subset
# output of function should match 'first_party' column
subset = resultFrame.head()
#print(subset['first_party'], subset.apply(findWinner, axis=1))

# function to add some randomness to vote count
# add or subtracts a random number of votes
def randVotes(series, factor):
    votes = series.iloc[15:].astype(int)
    newVotes = []
    for val in votes:
        newVote = round(val + val*factor*np.random.normal())
        if newVote < 0:
            newVote = 0
        newVotes.append(newVote)
    return newVotes

# generate n election results
n = 30
# set how common a vote 'error' occurs
errRate = [0.01]
# create final seats dataframe
seats = pd.DataFrame(index=range(n), columns = resultFrame.columns[15:])
for i in range(n):
    # add some noise to election results
    newResults = resultFrame.apply(randVotes, axis=1, 
                                   args=[0.1], result_type='expand')
    resultFrameCpy = resultFrame.copy()
    resultFrameCpy.iloc[:, 15:] = newResults
    # calculate seats for each party
    seatCnt = resultFrameCpy.apply(findWinner, axis=1).value_counts()
    seats.loc[i, seatCnt.index] = seatCnt
seats = seats.fillna(0)
seats = seats.astype(int)
# show results of Conservative and Labour
seats.hist(column=seatCnt.index[0])
seats.hist(column=seatCnt.index[1])
