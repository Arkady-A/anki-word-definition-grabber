from bs4 import BeautifulSoup
import requests
import pandas as pd
import time
import random
# TODO add documentation


class Data():                   # TODO put this class higher in different
    def __init__(self):
        self.source = None      # type: str
        self.data_type = None   # type: str
        self.data = []

    def get_data_as_df(self):
        '''
        returns: Pandas DataFrame consisting data.
        '''
        return pd.DataFrame([entry.get_data() for entry in self.data])


class Definition():
    def __init__(self):
        self.word = None        # type: str
        self.part_of_speech = None  # type: str
        self.definition = None  # type: str
        self.examples = []
        self.additional_info = 'No additional info'  # only for now

    def get_data(self):
        data = {
            'word': self.word,
            'part_of_speech': self.part_of_speech,
            'definition': self.definition,
            'examples': self.examples,
            'additional_info': self.additional_info,
            'transcript': None
        }
        return data


class Dictionary_Collector():

    def __load_data__(self, link, word):
        time.sleep(random.randrange(1, 2))  # for not to ddos
        raw_html = requests.get('{}/{}'.format(link, word)).text
        self.full_link = '{}/{}'.format(link, word)  # full link to page
        return (raw_html, self.full_link)

    def get_data(self):
        '''Returns dictionary with data'''
        return self.__data__


class Oxford_Word_Collector(Dictionary_Collector):
    def __init__(self):
        super().__init__()

        self.link = 'https://en.oxforddictionaries.com/definition'

    def __process_data__(self, word, raw_html, full_link):
        processed_data = Data()  # this all should be in super method
        parser = BeautifulSoup(raw_html, 'html.parser')
        sections = parser.find('div', 'entryWrapper').find_all(
            'section', 'gramb', recursive=False)
        processed_data.source = full_link
        processed_data.data_type = 'word'  # -------------------------
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
                    x.get_text() for x in definition.find_all('div', 'ex', limit=3)]
                processed_data.data.append(definition_var)

        return processed_data

    def load_words(self, words):
        data_array = []
        words_that_havenot_found = [] # this sould be fixed by finding appropriate word and asking
        # user is a suggestion right
        for word in words:
            raw_html, full_link = self.__load_data__(self.link, word)
            temporary_parser = BeautifulSoup(raw_html, 'html.parser')
            if 'No exact matches found' in temporary_parser.get_text():
                print('word {} is not found'.format(word))
                words_that_havenot_found.append(word)
            else:
                print('word {} found'.format(word))
                data_array.append(self.__process_data__(
                    word, raw_html, full_link))
        print(words_that_havenot_found) # add it to return and process it 
        return data_array


class Cambridge_Word_Collector(Dictionary_Collector):
    def __init__(self):
        return 0


class Dicionary_com_Word_Collector(Dictionary_Collector):
    def __init__(self):
        return 0
