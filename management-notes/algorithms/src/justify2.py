#!/usr/bin/env python3
import sys

n_calls = 0

def badness(words, pagewidth):
    #print("badness: %s" % (words))
    global n_calls
    n_calls += 1
    width = 0
    for w in words:
        width += len(w) + 1 # Add a space between words
    width -= 1 # Remove space at end of line
    if width > pagewidth:
        badness = sys.maxsize
    else:
        badness = (pagewidth - width)**3
    return badness

"""
Where to split lines so as to minimise total badness
"""
def justify(text, pagewidth, use_memo, memo):
    #print("justify: %s" % (text)) 
    text_len=len(text)
    if text_len < 1: # error case
        return 0 
    elif text_len == 1: # base case
        return badness(text, pagewidth)
    else: # recursive step
        # Minimise total badness over all choices for where to start the second line
        if text_len not in memo: 
            min_badness = None
            for i in range(1, text_len + 1):
                total_badness = badness(text[0:i], pagewidth) + justify(text[i:], pagewidth, use_memo, memo)
                if min_badness is None:
                    min_badness = total_badness
                elif total_badness < min_badness:
                    min_badness = total_badness
            if use_memo:
                memo[text_len] = min_badness
        else:
            min_badness = memo[text_len]
        return min_badness

def justify_bottom_up(text, pagewidth, use_memo, memo):
    text_len = len(text)
    min_badness = None
    memo[text_len] = 0
    # Work backwards through the text
    # Pre-condition: memo is empty except for memo[text_len]
    # Post-condition: memo will be populated for all entries between 0 and text_len
    # Invariant:
    for i in range(text_len - 1, -1, -1):
        #print(i)
        min_badness = None
        # Calculate the min badness for suffix starting from i
        # Pre-condition: memo[i+1..text_len] is populated
        # Post-condition: min badness calculated for position i
        #print(memo)
        for j in range(text_len, i, -1):
            #print("i:%d, j:%d, text: %s" % (i, j, text[i:j]))
            this_badness = badness(text[i:j], pagewidth) + memo[j]
            if min_badness is None:
                min_badness = this_badness
            elif this_badness < min_badness:
                min_badness = this_badness
        # Store the min badness for reuse
        memo[i] = min_badness
        #print(memo)

    return min_badness


if __name__ == "__main__":
    with open("test.txt") as file:
        #text = ["a", "b", "c", "d", "e", "f"]
        text = file.read().split()
        print(text)
        for i in range(1, 26):
            for pagewidth in range(4, 9):
                print(text[0:i])
                n_calls = 0
                print("n_words: %d, pagewidth: %d, min_badness: %d" % (len(text[0:i]), pagewidth, justify(text[0:i], pagewidth, True, {})))
                print("%d, n_calls: %d" % (i, n_calls));

                n_calls = 0
                # Recursive, no memoisation
                print("n_words: %d, pagewidth: %d, min_badness: %d" % (len(text[0:i]), pagewidth, justify(text[0:i], pagewidth, False, {})))
                print("%d, n_calls: %d" % (i, n_calls));
                #print("%d: %d" % (pagewidth, badness(text, pagewidth)))

                n_calls = 0
                print("n_words: %d, pagewidth: %d, min_badness: %d" % (len(text[0:i]), pagewidth, justify_bottom_up(text[0:i], pagewidth, False, {})))
                print("%d, n_calls: %d" % (i, n_calls));
