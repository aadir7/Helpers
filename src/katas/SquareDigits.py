'''
Created on Sep 9, 2017

@author: egikmnq
'''
import logging

class SquareDigits(object):
    '''
    Converts the number to square of its digits
    For example: Converts 9119 to 811181
    '''


    def __init__(self, log=None):
        '''
        Constructor
        '''
        self.log = logging.getLogger(__name__)
    
    def square_digits(self, num):
        self.log.info('Number input to square process: %s' %num)
        square = list()
        digits = [str(int(x)* int(x)) for x in str(num)]
        square_str = ''.join(digits)
        self.log.info('Squared result for %s - %s' %(num, int(square_str)))
        return int(square_str)