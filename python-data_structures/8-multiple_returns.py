#!/usr/bin/python3

def multiple_returns(sentence):
    # Check if the sentence is empty
    if len(sentence) == 0:
        return (0, None)  # Return (0, None) if the sentence is empty
    else:
        return (len(sentence), sentence[0])  # Return tuple with length and first character
