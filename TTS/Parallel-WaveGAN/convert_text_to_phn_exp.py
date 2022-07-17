#!/usr/bin/env python3

from espnet2.text.phoneme_tokenizer import PhonemeTokenizer

def get_lex(line):
    g2p="espeak_ng_hindi"
    tokenizer = PhonemeTokenizer(g2p_type=g2p)
    tokens = tokenizer.text2tokens(line)
    print(" ".join(tokens) + "\n")
    return(" ".join(tokens) + "\n")


