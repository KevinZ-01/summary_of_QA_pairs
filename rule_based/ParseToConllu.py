import stanfordnlp
from utils.load import *


def parseToconllu(data):
    data = data[:5]
    nlp = stanfordnlp.Pipeline(models_dir='E:/anaconda/setup/Lib/site-packages/stanfordnlp')  # This sets up a default neural pipeline in English
    doc_text = ''
    for data_ in data:
        for i in range(len(data_['questions'])):
            if not data_['questions'][i]['input_text'][-1] == '?':
                data_['questions'][i]['input_text'] += '?'
            if not data_['questions'][i]['input_text'][0].isupper():
                data_['questions'][i]['input_text'] = list(data_['questions'][i]['input_text'])
                data_['questions'][i]['input_text'][0] = data_['questions'][i]['input_text'][0].upper()
                data_['questions'][i]['input_text'] = ''.join(data_['questions'][i]['input_text'])
            doc_text += data_['questions'][i]['input_text'] + ' '
            if not data_['answers'][i]['input_text'][-1] == '.':
                data_['answers'][i]['input_text'] += '.'
            if not data_['answers'][i]['input_text'][0].isupper():
                data_['answers'][i]['input_text'] = list(data_['questions'][i]['input_text'])
                data_['answers'][i]['input_text'][0] = data_['questions'][i]['input_text'][0].upper()
                data_['answers'][i]['input_text'] = ''.join(data_['questions'][i]['input_text'])
            doc_text += data_['answers'][i]['input_text'] + ' '
#        doc_text += '\n'
    print('start parsing...')
    doc = nlp(doc_text)
    doc.write_conll_to_file('example.conllu')


data = load_data_COQA()
parseToconllu(data)
