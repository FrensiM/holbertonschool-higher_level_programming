#!/usr/bin/python3
def multiple_returns(sentence):
    if len(sentence) == 0 or sentence == 0:
        print("Length: {:d} - First character: None".format(len(sentence)))
    else:
        print("Length: {:d} - First character: {}".format(len(sentence), sentence[0]))
