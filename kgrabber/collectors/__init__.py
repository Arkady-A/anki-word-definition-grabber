# import Definition
# import Data

# dict_converters = {}


# def converter(f): return dict_converters.setdefault(f.__name__, f)


# @converter
# def oxford(word, raw_html):
#     parsed_data = Data()
#     for section in list(sections):
#         definitions = section.find(
#             'ul', 'semb').find_all('li', recursive=False)
#         for definition in list(definitions):
#             definition_var = Definition()
#             definition_var.word = word
#             definition_var.part_of_speech = section.find(
#                 'span', 'pos').get_text()
#             definition_var.definition = definition.find('p').get_text()
#             try:
#                 if definition_var.definition[0].isdigit():
#                     definition_var.definition = definition_var.definition[1:]
#             except IndexError:
#                 definition_var.definition = 'No definition'
#             definition_var.examples = [
#                 x.get_text() for x in definition.find_all('div', 'ex', limit=3)]
#             parsed_data.data.append(definition_var)
#     return parsed_data
