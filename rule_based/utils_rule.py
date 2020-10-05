from copy import deepcopy
from sacremoses import MosesDetokenizer
from rule_based.rule_based import Question, AnswerSpan

detokenizer = MosesDetokenizer()

def qa2d(idx, examples):
    q = Question(deepcopy(examples[idx].tokens))
    if not q.isvalid:
        print("Question {} is not valid.".format(idx))
        return ''
    a = AnswerSpan(deepcopy(examples[str(idx)+'_answer'].tokens))
    if not a.isvalid:
        print("Answer span {} is not valid.".format(idx))
        return ''
    q.insert_answer_default(a)
    return detokenizer.detokenize(q.format_declr(), return_str=True)

def print_sentence(idx, examples):
    return detokenizer.detokenize([examples[idx].tokens[i]['form'] for i in range(len(examples[idx].tokens))], return_str=True)