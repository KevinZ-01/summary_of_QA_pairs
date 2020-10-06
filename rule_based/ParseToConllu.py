import stanfordnlp

def parseToconllu(paragraph):
    nlp = stanfordnlp.Pipeline(models_dir='E:/anaconda/setup/Lib/site-packages/stanfordnlp')  # This sets up a default neural pipeline in English
    doc = nlp(paragraph)
    doc.write_conll_to_file('example.conllu')

    """
    f = open('example.conllu', 'wt')

    for i in range(len(doc.sentences)):
        tokens = doc.sentences[i].tokens
        for token in tokens:
            to_write = token.index + '\t' + token.words.text + '\t_\t' + token.words.upos + '\t' + token.words.xpos\
                       + '\t_\t' + token.words.governor + '\t' + token.words.dependency_relation + '\t_\t_\n'
            f.write(to_write)
        f.write('\n')
    f.close()
    """
