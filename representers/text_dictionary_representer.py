basic_html_template = '''
{word} | {transcript}\n
{additional_info}
<div style="margin-bottom: 20px;">
<div>
<p style="padding-left: 10px;"><strong>{part_of_speech}</strong></p>
</div>
<div style="padding-left: 20px; padding-right: 20px;">
<p>{definition}</p>
<div style="padding-left:15px;color: #545454">
{formatted_examples}
</div>
</div>
</div>
'''


class Data_Definition_html_representer():
    def __init__(self, data):
       self.data=data
    def to_text(self,path):
        a_file = open(path, 'a')
        for definition in self.data.data:
            def_dict_data = definition.get_data()['examples']
            a_file.write(basic_html_template.format(formatted_examples='<br>'.join(def_dict_data),**definition.get_data()))
        a_file.close()
