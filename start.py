import data_collectors.dictionarycollector as dicts_col
import representers
from bs4 import BeautifulSoup

if __name__ == '__main__':
    print('Hello console!')
    test = dicts_col.Oxford_Word_Collector()
    print(test.get_data('home'))
#    print(test.raw_html)
