from bs4 import BeautifulSoup
import requests


class Data():                   # TODO put this class higher in different module
    def __init__(self):
        self.source = None      # type: String
        self.data_type = None   # type: String
        self.data = []        # type: List of Definition's


class Definition():
    def __init__(self):
        self.word = None        # type: String
        self.part_of_speech = None  # type: String
        self.definitions = None  # type: String
        self.examples = []  # type: List of strings

    def get_data(self):
        data = {
            'word': self.word,
            'part_of_speech': self.part_of_speech,
            'definition': self.definitions,
            'examples': self.examples,
        }
        return data


class Dictionary_Collector():

    def __load_data__(self, link, word):
        self.raw_html = requests.get('{}/{}'.format(link, word)).text
        self.full_link = '{}/{}'.format(link, word)  # full link to page

    def get_data(self):
        '''Returns dictionary with data'''
        return self.__data__


class Oxford_Word_Collector(Dictionary_Collector):
    def __init__(self):
        super().__init__()

        self.link = 'https://en.oxforddictionaries.com/definition'
        self.data = Data()

    def __process_data__(self, word):
        parser = BeautifulSoup(self.raw_html, 'html.parser')
        sections = parser.find('div', 'entryWrapper').find_all(
            'section', 'gramb', recursive=False)

        for counter, section in enumerate(list(sections)):
            print("section!{}".format(counter))
            definitions = section.find(
                'ul', 'semb').find_all('li', recursive=False)
            for definition in list(definitions):
               # print(definition)
                definition_var = Definition()
                definition_var.word = word
                definition_var.part_of_speech = section.find(
                    'span', 'pos').get_text()
                definition_var.definition = definition.find('p').get_text(),
                definition_var.examples = [
                    x.get_text() for x in definition.find_all('div', 'ex', limit=3)]
                self.data.data.append(definition_var)

    def get_data(self, word):
        self.__load_data__(self.link, word)
        self.data.source = self.full_link
        self.data.data_type = 'word'
        self.__process_data__(word)
        return self.data


class Cambridge_Word_Collector(Dictionary_Collector):
    def __init__(self):
        return 0


class Dicionary_com_Word_Collector(Dictionary_Collector):
    def __init__(self):
        return 0
