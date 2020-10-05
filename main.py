import codecs
from conllu import parse
from rule_based.utils_rule import *


def main():
    print('Parsing conllu file...')
    with codecs.open('examples.conllu', 'r', encoding='utf-8') as f:
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

    total = int(len(examples.keys()) / 2)
    print("Transforming {} examples.".format(total))
    for i in range(total):
        out = qa2d(i, examples)
        print(print_sentence(i, examples))
        if out != '':
            print(out)
        print('----------')

if __name__ == "__main__":
    main()