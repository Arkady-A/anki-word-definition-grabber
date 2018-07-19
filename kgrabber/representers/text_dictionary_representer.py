from yattag import Doc
import pandas as pd


class definition_html_template():
    html_header = '{word} | {transcript}'
    html_part_of_speech = ''

    def __init__(self):
        pass


class Data_Definition_html_representer():
    def __init__(self, data):
        self.data = data  # type: pd.DataFrame

    # to do: realize additional info field
    def to_html_by_part_of_speech(self, path, file_open_modif):
        doc, tag, text = Doc().tagtext()
        groups = self.data.groupby('part_of_speech')
        with tag('strong'):
            text(', '.join(self.data.loc[:,'word'].unique()))
        for name, group in groups:
            with tag('div', style='margin-bottom:20px;'):
                with tag('div'):
                    with tag('span', style='padding-left:10px;'):
                        with tag('strong'):
                            text(name)
                for index, row in group.iterrows():
                    with tag('div', style='padding-left:20px;padding-right:20px; margin-bottom: 8px'):
                        text(row['definition'])
                        with tag('div', style='padding-left:15px;color:#545454'):
                            for example in row['examples']:
                                text(example)
                                doc.stag('br')
                            # examples
        A_file=open(path, file_open_modif)
        A_file.write(doc.getvalue())
        A_file.write('\n\n'+'='*100+'\n\n')
        A_file.close()
