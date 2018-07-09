import data_collectors.dictionarycollector as dicts_col
import representers.text_dictionary_representer
from bs4 import BeautifulSoup
import pprint

if __name__ == '__main__':
    print('Hello console!')
    test = dicts_col.Oxford_Word_Collector()
    thing = test.get_data('home')
    pprint.pprint('The thing is {}'.format(thing))
    for defin in thing.data:
        print(defin.get_data())
    representer = representers.text_dictionary_representer.Data_Definition_html_representer(thing)
    representer.to_text('test.txt')
 #   print(test.get_data('home'))
#    print(test.raw_html)
