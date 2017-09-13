'''
Created on Sep 12, 2017

@author: egikmnq
'''
import logging

class SubstringArray(object):
    '''
    Compares Array a1 and Array a2
    Finds a sorted array result from a1 which are substrings of a2
    
    a1 = ["arp", "live", "strong"]
    a2 = ["lively", "alive", "harp", "sharp", "armstrong"]
    Returns Array ["arp", "live", "strong"]
    '''


    def __init__(self):
        '''
        Constructor
        '''
        self.log = logging.getLogger(__name__)
        
    def findSortedSubstringArray(self, a1, a2):
        '''
        Finds the substrings of a2 from a1 and returns a sorted array of a1
        :param a1: Array to be compared with a2
        :param a2: Array to make substring comparison
        '''
        self.log.info("Comparing %s and %s" %(a1, a2))
        r = []
        for i in a1:
            for j in a2:
                if not i in j:
                    continue
                if i in r:
                    continue
                r.append(i)
        self.log.info("Sorted array %s" %sorted(r))
        return sorted(r)