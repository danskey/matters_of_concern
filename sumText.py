### Lex Rank ###
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lex_rank import LexRankSummarizer
from sumy.summarizers.kl import KLSummarizer

##############   Text summary tools   ##############


def lex_rank_sum(path, L):
    filename = path
    L = L
    output = []
    parser = PlaintextParser.from_file(filename, Tokenizer("english"))
    summarizer = LexRankSummarizer()
    summary = summarizer(parser.document, L) #number of sentences in parenthecies
    for sentence in summary: # option for writing to a summary output file.
        item = str(sentence)
        output.append(item)
    return output

    #for sentence in summary: # option for writing to a summary output file.
    #     item = str(sentence)+"\n"

def kl_rank_sum(path, K):
    filename = path
    K = K
    parser = PlaintextParser.from_file(filename, Tokenizer("english"))
    summarizer = LexRankSummarizer()
    summary = summarizer(parser.document, K) #number of sentences in parenthecies
    return summary

    # for sentence in summary: #writing to a summary output file.
    #     FRANK = str(sentence)+"\n"
    #     return FRANK
    #     print FRANK
