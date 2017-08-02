"""module for sorting siblings chronologically"""
import operator
from datetime import datetime
import time

def sort_siblings(children, people):
    kidsToBeSorted={}
    if children != "NA":
        for child in children:
            kidsToBeSorted[child]= datetime.strptime(people[child]["BIRT"], '%d %b %Y')
            mytime = kidsToBeSorted[child].isoformat()
            dectime=mytime.split('-')
            kidsToBeSorted[child]=dectime[0]+dectime[1]+dectime[2]
    sortedKids = sorted(kidsToBeSorted.items(),key=operator.itemgetter(1))
    sortedIDs = [x[0] for x in sortedKids] 


    return sortedIDs


        
