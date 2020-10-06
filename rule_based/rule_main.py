import codecs
from conllu import parse
from rule_based.utils_rule import *
from rule_based.ParseToConllu import parseToconllu
from utils.score import get_score


def rule_main(args, data):
    file_name = 'example.conllu'
    if args.dataset == 'CoQA':
        score = 0
        length = len(data)
        for data_ in data:
            summary = data_['summary']
            QA = ""
            for i in range(len(data_['questions'])):
                QA += data_['questions'][i]['input_text'] + ' '
                if not data_['answers'][i]['input_text'][-1] == '.':
                    data_['answers'][i]['input_text'] += '.'
                QA += data_['answers'][i]['input_text'] + ' '
            parseToconllu(QA)

            with codecs.open(file_name, 'r', encoding='utf-8') as f:
                conllu_file = parse(f.read())
            # Creating dict
            print(len(conllu_file))
            print(conllu_file)
            ids = range(int(len(conllu_file) / 2))
            examples = {}
            count = 0
            for i, s in enumerate(conllu_file):
                if i % 2 == 0:
                    examples[ids[count]] = s
                else:
                    examples[str(ids[count]) + '_answer'] = s
                    count += 1

            total = int(len(examples.keys()) / 2)
            generate_summary = ''
            for i in range(total):
                generate_summary += qa2d(i, examples)
            score += get_score(generate_summary, summary, args.score)

    elif args.dataset == 'QuAC':
        score = 0
        length = len(data)
    else:
        score = 0
        length = len(data)

    score = score/length
    print('summary score: ', score)
