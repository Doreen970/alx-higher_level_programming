#!/usr/bin/python3

def multiple_returns(sentence):
    length_str = len(sentence)
    if length_str == 0:
        first = None
    else:
        first = sentence[0]
    return length_str, first
