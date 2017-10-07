'''
Created on Sep 9, 2017

@author: egikmnq
'''
import sys
import logging


class MissingSequence(object):
    '''
    Converts the phrase to CapWords as Jaden smith uses in his blog
    '''

    def __init__(self):
        '''
        Constructor
        '''
        logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)
        self.log = logging.getLogger(__name__)

    def find_missing_sequence(self, sequence):
        '''
        This function finds the missing sequence number in the list
        :param sequence: sequence to process
        '''
        self.log.info("Sequence to work on %s" % sequence)
        diff = min(
            [(sequence[1] - sequence[0]),
                (sequence[-1] - sequence[-2])])
        self.log.info("Diff: %s" % diff)
        missingNos = [sequence[i] - diff for i in range(1, len(sequence))
                      if not abs(sequence[i] - sequence[i - 1]) is diff]
        self.log.info("missing no: %s" % missingNos[0])