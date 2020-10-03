# for the file
import json
import json_lines

def load_data_SQuAD():
    with open('./data/SQuAD2.0/dev-v2.0.json') as f:
        source = json.load(f)

    for data in source['data']:
        for paragraph in data['paragraphs']:
            remove_list = []
            for i in range(len(paragraph['qas'])):
                paragraph['qas'][i].pop('id')
                if paragraph['qas'][i]['is_impossible']: # not answerable data
                    remove_list.append(i)
            paragraph['qas'] = [paragraph['qas'][i] for i in range(len(paragraph['qas'])) if i not in remove_list]
    return source['data']

def load_data_COQA():
    with open('./data/COQA/coqa-dev-v1.0.json') as f:
        source = json.load(f)

    for data in source['data']:
        data.pop('id')
        data.pop('filename')
    return source['data']

def load_data_SMCalFlow():
    source = []
    with open('./data/SMCalFlow/valid.dataflow_dialogues.jsonl') as f:
        for dialog in json_lines.reader(f):
            source.append([
                {'agent': turn['agent_utterance']['original_text'], 'user': turn['user_utterance']['original_text']}
                for turn in dialog['turns']])
    return source

def load_data_QuAC():
    with open('./data/QuAC/val_v0.2.json') as f:
        source = json.load(f)

    for data in source['data']:
        for paragraph in data['paragraphs']:
            for qa in paragraph['qas']:
                if qa['yesno'] == 'y':
                    for answer in qa['answers']:
                        answer['text'] = 'yes, ' + answer['text']
                elif qa['yesno'] == 'n':
                    for answer in qa['answers']:
                        answer['text'] = 'no, ' + answer['text']
    return source['data']