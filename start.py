import data_collectors.dictionarycollector as dicts_col
import representers
from bs4 import BeautifulSoup
import pprint

if __name__ == '__main__':
    print('Hello console!')
    test = dicts_col.Oxford_Word_Collector()
    thing = test.get_data('home')
    pprint.pprint('The thing is {}'.format(thing))
    for defin in thing.data:
        print(defin.get_data())
 #   print(test.get_data('home'))
#    print(test.raw_html)
