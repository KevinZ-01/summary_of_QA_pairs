from load import *
import nltk
# output as html
def printTohtml_SQUAD(data):
    html = "<html>\n<head></head>\n<style>p { margin: 0 !important; }</style>\n<body>\n"

    title = "SQuAD"
    html += '\n<p>' + title + '</p>\n' + '<br>\n'

    for data_ in data:
        for paragraph in data_['paragraphs']:
            # context
            context = '<p>' + paragraph['context'] + '</p>\n'
            html +=context
            html += '<br>\n'
            # qas
            for qa in paragraph['qas']:
                q = '<p style="color:red;">' + 'Q:  ' + qa['question'] + '</p>\n'
                html += q
                for answer in qa['answers']:
                    a = '<p style="color:red;">' + 'A:  ' + answer['text'] + '</p>\n'
                    html += a
            html += '<br>\n'
            # summary
            summary = '<p style="color:green;">' + 'Summary:  ' + paragraph['summary'] + '</p>\n'
            html += summary
            html += '<br>\n' + '<p>' + '-------------------------------------------------------------------------------------' + '</p>\n' + '<br>\n'

    with open('SQuAD.html', 'w', encoding='utf8') as f:
        f.write(html + "\n</body>\n</html>")

def printTohtml_COQA(data):
    html = "<html>\n<head></head>\n<style>p { margin: 0 !important; }</style>\n<body>\n"

    title = "CoQA"
    html += '\n<p>' + title + '</p>\n'  + '<br>\n'

    for data_ in data:
        # source
        source = '<p>' + 'source: ' + data_['source'] + '</p>\n'
        html += source
        # context
        context = '<p>' + data_['story'] + '</p>\n'
        html += context
        html += '<br>\n'
        # qas
        for i in range(len(data_['questions'])):
            q = '<p style="color:red;">' + 'Q:  ' + data_['questions'][i]['input_text'] + '</p>\n'
            html += q
            a = '<p style="color:red;">' + 'A:  ' + data_['answers'][i]['input_text'] +'||' + data_['answers'][i]['span_text'] + '</p>\n'
            html += a
        html += '<br>\n'
        # summary
        summary = '<p style="color:green;">' + 'Summary:  ' + data_['summary'] + '</p>\n'
        html += summary
        html += '<br>\n' + '<p>' + '-------------------------------------------------------------------------------------' + '</p>\n' + '<br>\n'

    with open('CoQA.html', 'w', encoding='utf8') as f:
        f.write(html + "\n</body>\n</html>")

def printTohtml_SMCalFlow(data):
    html = "<html>\n<head></head>\n<style>p { margin: 0 !important; }</style>\n<body>\n"

    title = "SMCalFlow"
    html += '\n<p>' + title + '</p>\n' + '<br>\n'

    for dialog in data:
        for turn in dialog:
            user = '<p>' + turn['user'] + '</p>\n'
            agent = '<p>' + turn['agent'] + '</p>\n'
            html += user
            html += agent
        html += '<p>' + '--------------------------------------------------------------------' + '</p>\n'
        # context
    with open('SMCalFlow.html', 'w', encoding='utf8') as f:
        f.write(html + "\n</body>\n</html>")

def is_match_squad(qa, sentence_end):
     if qa['answers'][0]['answer_start'] < sentence_end:
         return True
     else:
         return False

def if_match_coqa(a, sentence_end):
    if a['span_start'] < sentence_end:
        return True
    else:
        return False

