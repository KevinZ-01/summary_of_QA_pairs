import random
from nltk.translate.bleu_score import corpus_bleu
import stanfordnlp
from conllu import parse
import re
import codecs
from rule_based.utils_rule import *
import pattern3
import pattern

with codecs.open('rule_based/examples.conllu', 'r', encoding='utf-8') as f:
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
generate_summary = ''
for i in range(total):
    generate_summary += qa2d(i, examples) + ' '

print(generate_summary)

pattern3.conjugate