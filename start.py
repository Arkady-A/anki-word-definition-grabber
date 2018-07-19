import kgrabber
from bs4 import BeautifulSoup
import pandas as pd

# TODO
# * Idiom support
# * check if word was not found
# * load words from file
# * ability to choose  definition
# * graphical interface
# * much more ^_^

if __name__ == '__main__':
    test = dicts_col.Oxford_Word_Collector()
    words = pd.read_csv('input.csv',',')
    print(words)
    things = test.load_words(words.loc[:,'word'].tolist())
    all_data = []
    for thing in things:
       # with pd.option_context('display.max_rows', None, 'display.max_columns', 10):
        #    print(thing.get_data_as_df())
        repr = representers.text_dictionary_representer.Data_Definition_html_representer(
            thing.get_data_as_df())
        repr.to_html_by_part_of_speech('output.txt', 'a')
