'''
Created on Sep 9, 2017

@author: egikmnq
'''
import logging

class JadenCase(object):
    '''
    Converts the phrase to CapWords as Jaden smith uses in his blog
    '''


    def __init__(self):
        '''
        Constructor
        '''
        self.log = logging.getLogger(__name__)
    
    def convert_to_jaden_case(self, phrase):
        '''
        This function converts the phrase to CapWords.
        First letter of all words will be converted to JadenCase (CapWords)
        :param phrase: Phrase to use for conversion
        '''
        self.log.info("Phrase to convert, \'%s\'" %phrase)
        str_list = phrase.split(' ')
        jaden_list = [x.capitalize() for x in str_list]
        self.log.info("Converted phrase, \'%s\'" %(' ' .join(jaden_list)))
        return ' ' .join(jaden_list)
        