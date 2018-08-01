import kgrabber
from bs4 import BeautifulSoup
import pandas as pd

# TODO
# * Idiom support
# * --check if word was not found--
# * --load words from file--
# * ability to choose  definition
# * graphical interface
# * place functional of function below to a module
# * much more ^_^

if __name__ == '__main__':
    test = kgrabber.Definition_Collector()
    words = pd.DataFrame()
    words = pd.read_csv('input.csv')
    words = [el[0] for el in words.values]
    print(words)
    not_found = []
    data = test.get_definitions(words)
    for dat in data:
        print(dat.get_data_as_df().word.values)
        print(dat.get_data_as_df().definition.values)
        if 'Defenition have not been found' in dat.get_data_as_df().definition.values:
            print('word {} have not been found'.format(dat.get_data_as_df().word.values))
            not_found.append(dat.data[0].word)
        else:
            repr = kgrabber.Data_Definition_html_representer(dat.get_data_as_df())
            repr.to_html_by_part_of_speech('output.txt','a')
    print('Words that have not found:{}'.format(not_found))
