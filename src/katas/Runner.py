'''
Created on Sep 9, 2017

@author: egikmnq
'''
from SquareDigits import SquareDigits
from JadenCase import JadenCase
from SubstringArray import SubstringArray
import logging


class Runner(object):
    '''
    Runner for all the Katas tried in codewars
    '''

    def __init__(self):

        '''
        Constructor
        '''
        logging.basicConfig(level=logging.INFO)
        self.log = logging.getLogger(__name__)

    def run_square_digits(self, num):
        '''
        Runs the square digits kata
        :param num: Number to convert to digit squares
        '''
        self.log.info('square digits runner started')
        sd = SquareDigits()
        self.log.info('Running square digits with %s' % num)
        sd.square_digits(num)

    def run_jaden_case(self, phrase):
        '''
        Converts the phrase to CapWords
        :param phrase: Sequence of words to be converted
        '''
        self.log.info('jaden case conversion staretd')
        jdc = JadenCase()
        self.log.info("Running JadenCase conversion with \'%s\'" % phrase)
        jdc.convert_to_jaden_case(phrase)

    def compare_for_substring_arrays(self, a1, a2):
        '''
        a1 and a2 arrays are to be compared to get the result sorted
        substring array
        :param a1:
        :param a2:
        '''
        self.log.info('Substring array comparision started')
        sba = SubstringArray()
        sba.findSortedSubstringArray(a1, a2)


if __name__ == '__main__':
    run = Runner()
    run.run_square_digits(991)
    run.run_jaden_case("jaden's gonna convert me to capcase")
    run.compare_for_substring_arrays(
        ["livelytest", "strong", "arp"],
        ["lively", "alive", "harp", "sharp", "armstrong"])