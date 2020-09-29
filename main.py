from html_writing_utils import *


def main():
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
    printTohtml_COQA(COQA)

    # print dialog data in HTML
    SMCalFlow = load_data_SMCalFlow()
    printTohtml_SMCalFlow(SMCalFlow)


if __name__ == "__main__":
    main()