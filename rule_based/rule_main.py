import codecs
from conllu import parse
from rule_based.utils_rule import *
from utils.score import get_score


def rule_main(args, data):
    file_name = 'rule_based/example.conllu'
    if args.dataset == 'CoQA':
        score = 0
        data = data[:5]
        length = len(data)
        with codecs.open(file_name, 'r', encoding='utf-8') as f:
            conllu_file = parse(f.read())

        # Creating dict
        ids = range(int(len(conllu_file) / 2))
        examples = {}
        count = 0
        for i, s in enumerate(conllu_file):
            if i % 2 == 0:
                examples[ids[count]] = s
            else:
                examples[str(ids[count]) + '_answer'] = s
                count += 1
        current_pos = 0
        for data_ in data:
            summary = data_['summary']
            generate_summary = ''
            for i in range(len(data_['questions'])):
                generate_summary += qa2d(current_pos, examples) + ' '
                current_pos += 1
            score += get_score(generate_summary, summary, args.score)

    elif args.dataset == 'QuAC':
        score = 0
        length = len(data)

    else:
        score = 0
        length = len(data)

    score = score/length
    print('summary score: ', score)
