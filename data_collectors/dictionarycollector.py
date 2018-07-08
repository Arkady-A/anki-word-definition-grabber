from bs4 import BeautifulSoup
import requests


class Dictionary_Collector():

    def __init__(self):
        self.__data__= { # setting structure for data # TODO place that structure higher
            'source':None,
            'type':None,
            'data':[
                
                ]
        }
        self.__process_structure__={
            'word':None,
            'part_of_speech':None,
            'Definition':[],
        }
    
    def __load_data__(self,link, word):
        self.raw_html = requests.get('{}/{}'.format(link,word)).text
        self.full_link = '{}/{}'.format(link,word) # full link to page
        
    def get_data(self):
        '''Returns dictionary with data'''
        return self.__data__


class Oxford_Word_Collector(Dictionary_Collector):
    def __init__(self):
        super().__init__()
        
        self.link = 'https://en.oxforddictionaries.com/definition'
        self.__data__['type'] = 'word'
        
    def __process_data__(self, word):
        parser = BeautifulSoup(self.raw_html,'html.parser')
        sections = parser.find_all('section', 'gramb')

        for section in list(sections):
            self.__process_structure__['word'] = word
            self.__data__['data'].append(self.__process_structure__)

    def get_data(self, word):
        self.__load_data__(self.link,word)
        self.__data__['source']= self.full_link
        self.__process_data__(word)
        return self.__data__

class Cambridge_Word_Collector(Dictionary_Collector):
    def __init__(self):
        return 0


class Dicionary_com_Word_Collector(Dictionary_Collector):
    def __init__(self):
        return 0
