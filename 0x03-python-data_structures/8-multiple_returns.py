#!/usr/bin/python3
def multiple_returns(sentence):
    tot = len(sentence)
    char = sentence[0] if tot > 0 else "None"
    new_tup = tot, char
    return(new_tup)
