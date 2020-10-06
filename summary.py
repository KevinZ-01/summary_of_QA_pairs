from html_writing_utils import *
from utils.load import *
import nltk

def summary_SQuAD():
    # generate summary of SQUAD
    SQuAD = load_data_SQuAD()
    for data in SQuAD:
        for paragraph in data['paragraphs']:
            context = paragraph['context']
            sentence_list = nltk.tokenize.sent_tokenize(context)
            summary = {}
            length = 0
            for i in range(len(sentence_list)):
                length += len(sentence_list[i])
                sentence_list[i] = [sentence_list[i], length]
            for qa in paragraph['qas']:
                for j in range(len(sentence_list)):
                    if is_match_squad(qa, sentence_list[j][1]):
                        if j not in summary:
                            summary[j] = sentence_list[j][0]
                        break
            sum = ''
            for key in sorted(summary):
                sum += summary[key]
            paragraph['summary'] = sum
    # print SQuAD with GT summary in HTML
    printTohtml_SQUAD(SQuAD)

def summary_CoQA():
    # generate summary of COQA
    COQA = load_data_COQA()
    for data in COQA:
        summary = {}
        context = data['story']
        sentence_list = nltk.tokenize.sent_tokenize(context)
        length = 0
        for i in range(len(sentence_list)):
            length += len(sentence_list[i])
            sentence_list[i] = [sentence_list[i], length]
        for i in range(len(data['questions'])):
            if data['answers'][i]['input_text'] == 'No' or data['answers'][i]['input_text'] == 'no':
                data['answers'][i]['input_text'] += ', ' + data['answers'][i]['span_text']
            for j in range(len(sentence_list)):
                if if_match_coqa(data['answers'][i], sentence_list[j][1]):
                    if j not in summary:
                        summary[j] = sentence_list[j][0]
                    break
        sum = ''
        for key in sorted(summary):
            sum += summary[key]
        data['summary'] = sum
    # print COQA with GT summary in HTML
    return COQA

def SMCalFlow():
    # print dialog data in HTML
    SMCalFlow = load_data_SMCalFlow()
    printTohtml_SMCalFlow(SMCalFlow)

def summary_QuAC():
    QuAC = load_data_QuAC()
    for data in QuAC:
        for paragraph in data['paragraphs']:
            summary = {}
            context = paragraph['context']
            sentence_list = nltk.tokenize.sent_tokenize(context)
            length = 0
            for i in range(len(sentence_list)):
                length += len(sentence_list[i])
                sentence_list[i] = [sentence_list[i], length]
            for qa in paragraph['qas']:
                for j in range(len(sentence_list)):
                    if if_match_quac(qa, sentence_list[j][1]):
                        if j not in summary:
                            summary[j] = sentence_list[j][0]
                        break
            sum = ''
            for key in sorted(summary):
                sum += summary[key]
            paragraph['summary'] = sum

    printTohtml_QuAC(QuAC)
