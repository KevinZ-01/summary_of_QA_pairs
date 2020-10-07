#from bert_score import score
from nltk.translate.bleu_score import sentence_bleu
import nltk


def get_score(cand, gt, method = 'bleu'):
    if method == 'bleu':
        gt_list = nltk.tokenize.sent_tokenize(gt)
        gt_l = []
        for i in range(len(gt_list)):
            gt_l += nltk.tokenize.word_tokenize(gt_list[i])

        cand_list = nltk.tokenize.sent_tokenize(cand)
        cand_l = []
        for i in range(len(cand_list)):
            cand_l += nltk.tokenize.word_tokenize(cand_list[i])
        score = sentence_bleu([gt_list], cand_list, weights=(0.25,0.25,0.25,0.25))
        print(score)
        return score
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
    return 0



