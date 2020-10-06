import argparse
from rule_based.rule_main import rule_main
from summary import *

def get_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('--dataset', type=str, default='CoQA',help='CoQA, QuAC')

    parser.add_argument('--no-cuda', action='store_true', default=True,
                        help='Disables CUDA training.')
    parser.add_argument('--method', type=str, default='rule',help='rule, rule-neural parser')
    parser.add_argument('--score', type=str, default='bert score', help='bert score, bleu, ')

    return parser.parse_args()


def main():
    args = get_arguments()
    if args.dataset == 'CoQA':
        data = summary_CoQA()
    if args.method == 'rule':
        rule_main(args, data)

if __name__ == "__main__":
    main()