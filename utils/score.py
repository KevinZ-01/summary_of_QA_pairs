#from bert_score import score
from nltk.translate.bleu_score import corpus_bleu
import nltk

def get_score(cand, gt, method = 'bleu'):
    if method == 'bleu':
        gt_list = nltk.tokenize.sent_tokenize(gt)
        for i in range(len(gt_list)):
            gt_list[i] = [nltk.tokenize.word_tokenize(gt_list[i])]
        cand_list = nltk.tokenize.sent_tokenize(cand)
        for i in range(len(cand_list)):
            cand_list[i] = [nltk.tokenize.word_tokenize(cand_list[i])]
        print(corpus_bleu(gt_list, cand_list))
        return corpus_bleu(gt_list, cand_list)
    """
    elif method == 'bert score':
        gt_list = nltk.tokenize.sent_tokenize(gt)
        for i in range(len(gt_list)):
            gt_list[i] = [gt_list[i]]
        cand_list = nltk.tokenize.sent_tokenize(cand)
        for i in range(len(cand_list)):
            cand_list[i] = [cand_list[i]]
        P, R, F1 = score(cand_list, gt_list, lang='en', verbose=True)
        return F1.mean() 
    """



