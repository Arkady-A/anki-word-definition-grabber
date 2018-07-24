from bs4 import BeautifulSoup
import requests
import pandas as pd
import time
import random
import urllib.request
# TODO add documentation


class Data():                   # TODO put this class higher in different
    def __init__(self, source, data_type):
        self.source = source      # type: str
        self.data_type = data_type   # type: str
        self.data = []

    def get_data_as_df(self):
        '''
        returns: Pandas DataFrame consisting data.
        '''
        return pd.DataFrame([entry.get_data() for entry in self.data])

    def __str__(self):
        return 'Data object. Source:{}, Type:{}'.format(self.source, self.data_type)


class Definition():  # TODO remove all variables initialization from __init__ - replace them by docstring
    def __init__(self):
        self.word = None        # type: str
        self.part_of_speech = None  # type: str
        self.definition = None  # type: str
        self.examples = []
        self.additional_info = 'No additional info'  # only for now
        self.transcript = None

    def get_data(self):
        ''' returns: Dictionary with all data '''
        data = {
            'word': self.word,
            'part_of_speech': self.part_of_speech,
            'definition': self.definition,
            'examples': self.examples,
            'additional_info': self.additional_info,
            'transcript': self.transcript
        }
        return data


class Definition_Collector():
    # self.words : list
    def __load_data(self, link):
        time.sleep(random.randrange(1, 2))  # for not to ddos
        raw_html = requests.get(link).text  #
        return raw_html

    def __prepare_data(self, link, word):
        raw_html = self.__load_data(link.format(word))
        parser = BeautifulSoup(raw_html, 'html.parser')
        return parser

    def worcc_oxford(self, word):
        #        raw_html = self.__load_data('https://en.oxforddictionaries.com/definition', word)
        link = 'https://en.oxforddictionaries.com'
        parsed_data = Data(link, 'words_def')
        parser = self.__prepare_data(link+'/definition/{}', word)
        sections = parser.find('div', 'entryWrapper').find_all(
            'section', 'gramb', recursive=False)
        for section in list(sections):
            definitions = section.find(
                'ul', 'semb').find_all('li', recursive=False)
            for definition in list(definitions):
                definition_var = Definition()
                definition_var.word = word
                definition_var.part_of_speech = section.find(
                    'span', 'pos').get_text()
                definition_var.definition = definition.find('p').get_text()
                try:
                    if definition_var.definition[0].isdigit():
                        definition_var.definition = definition_var.definition[1:]
                except IndexError:
                    definition_var.definition = 'No definition'
                definition_var.examples = [
                    example.get_text() for example in definition.find_all('div', 'ex', limit=3)]
                parsed_data.data.append(definition_var)
        return parsed_data

    def worcc_dictionarycom(self, word):  # TO-DO
        link = 'http://www.dictionary.com'
        parsed_data = Data(link, 'words_def')
        parser = self.__prepare_data(link+'/browse/{}', word)
        sections = parser.find_all('section', 'css-1sdcacc e10vl5dg0')
        for section in list(sections):
            definitions = section.find_all('li', 'css-2oywg7 e10vl5dg5')
            part_of_speech = section.find('header').find('span').get_text()
            for definition in list(definitions):
                examples = definition.find(
                    'span', 'luna-example italic')
                examples = examples.find_all(text=True) if examples != None else ['None']
                definition = definition.find('span')
                definition_var = Definition()
                definition_var.examples.append(examples)
                definition_var.word = word
                definition_var.part_of_speech = part_of_speech
                definition_var.definition = definition.get_text()
                definition_var.examples = examples
                parsed_data.data.append(definition_var)
                
            # extract examples from list then get text by getText
        return parsed_data

    def get_definitions(self, words):
        '''Gets definitions from all dictionaries 
        return: Data-type object'''
        for word in words:
            oxford_data = self.worcc_oxford(word)
            dictcom_data = self.worcc_dictionarycom(word)
            # here should be data from anothers dictionaries
        return (dictcom_data, oxford_data)

    def worcc_cambridge():      # TO-DO
        return 1


# class Oxford_Word_Collector(Dictionary_Collector):
#     def __init__(self):
#         super().__init__()
#         self.link =

#     def __process_data__(self, word, raw_html, full_link):
#         super().__process_data__(word,raw_html,full_link)# -------------------------


#         return processed_data

#     def load_words(self, words):
#         data_array = []
#         words_that_havenot_found = [] # this sould be fixed by finding appropriate word and asking
#         # user is a suggestion right
#         for word in words:
#             raw_html, full_link = self.__load_data__(self.link, word)
#             temporary_parser = BeautifulSoup(raw_html, 'html.parser') # should be checked in more appropriate way
#             if 'No exact matches found' in temporary_parser.get_text():
#                 print('word {} is not found'.format(word))
#                 words_that_havenot_found.append(word)
#             else:
#                 print('word {} found'.format(word))
#                 data_array.append(self.__process_data__(
#                     word, raw_html, full_link))
#         print(words_that_havenot_found) # add it to return and process it
#         return data_array


# class Cambridge_Word_Collector(Dictionary_Collector): # did not figured that out for now
#     # Cambridge site dosen't want to be scrabbed by requests, but by urllib all is ok.
#     def __init__(self):
#         return 0


# class Dicionary_com_Word_Collector(Dictionary_Collector):
#     def __init__(self):
#         return 0
