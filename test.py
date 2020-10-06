import random
from nltk.translate.bleu_score import corpus_bleu
import stanfordnlp
from conllu import parse
import re
import codecs

with codecs.open('rule_based/examples.conllu', 'r', encoding='utf-8') as f:
    conllu_file = parse(f.read())
# Creating dict
print(len(conllu_file))
print(conllu_file)



