#!/usr/bin/python3
def multiple_returns(sentence):
    if len(sentence) == 0 or sentence == 0:
        print(f"Length: {len(sentence)} - First character: None")
    else:
        print(f"Length: {len(sentence)} - First character: {sentence[0]}")
