#!/usr/bin/env python3

import sys

fh = open("test.txt", "r")
file = fh.read()
words = file.split()
#print(words)

"""
DP aims to turn an exponential algorithm into a polynomial one by recursion + memoisation

Reusing solutions to sub-problems in the recursion tree

"""

def count_chars(words):
    chars = 0
    for word in words:
        chars += len(word)
    return chars

"""
    Assign a value to how well the given words fit within the page_width

    @return Degree of "Badness" of fit - zero is a perfect fit
    @return sys.maxsize there is no fit
"""
def badness(words, page_width):
    # sum length of words between start and end
    print("Calculating badness for: %s" % (words))
    chars = count_chars(words)
    if chars > page_width:
        badness = sys.maxsize # Words do not fit on the line - infinite badness
    else:
        # We favour lines with minimal whitespace.  The formula is from latex according to the OCW course notes
        badness = (page_width-chars)**3
    print(badness)
    return badness


#print count_chars(words)

"""
        prefix : suffix
          ^         ^ 
    first line :  subsequent lines

We want to minimise the badness over all lines.

We have n choices for the length of the prefix: 1..n
We have n choices for the length of suffix: 0..n-1
We have n choices for where to start the suffix: 2..n+1 (i.e. no suffix)

DP is often about minimising or maximising

We define the total_badness for a choice as the sum of the badness of the prefix and the min badness of the suffix.

We need to minimise total_badness by trying each choice above - i.e. we want to calaculate the min total_badd

The min total_badness is the min of the sum of the badness of the prefix and the min_badness of the suffix

The total badness is the sum of the badness of the prefix plus the min_badness of the suffix
"""
def total_badness(words, suffix_pos, page_width):
    prefix = words[0:suffix_pos]
    suffix = words[suffix_pos:]
    print("prefix: %s, suffix: %s" % (prefix, suffix))
    prefix_badness = badness(prefix, page_width)
    suffix_badness = min_total_badness(suffix, page_width)
    sum_badness = prefix_badness + suffix_badness
    return sum_badness

"""
    We calculate the min over all the available choices for suffix_pos
"""
def min_total_badness(words, page_width):
    print("min_total_badness: words: %s, page_width: %d" % (words, page_width))
    word_len = len(words)
    if word_len == 0:
        return badness(words, page_width)

    min_badness = sys.maxsize
    # Try each of the available choices for
    # We include the case where the suffix is empty hence word_len+1
    for j in range(1, word_len+1):
        print("Trying pos: %d" % (j))
        b = total_badness(words, j, page_width)
        if b < min_badness:
            min_badness = b
    return min_badness

"""
The minimum badness of the give suffix

How do we deal with the base case?

What is the min_badness of an empty suffix?
1   [] -> sys.maxsize
2   [] -> (page_width - 0)**3
3   [] -> 0

Option 2 is the most natrual - it makes the base case not that special which seems elegant.  However won't it mean that when we are checking the case that the prefix best fits on one line that it favours putting the suffix on the next line?

page_width: 10
prefix: ['a', 'b', 'c', 'd', 'e'], suffix: []
badness: (10-5)**3 + min_badness([])
prefix: ['a', 'b', 'c', 'd'], suffix: ['e']
badness: (10-4)**3 + min_badness([])

If we use option 1 or 2 then the algorithm will never favour positions than end in an empty list, because the empty list will always add a large value to total badness

We must therefore make an empty suffix a special case with zero additional badness.

Option 3
"""
def min_badness(suffix, page_width):
    return 0
    

def justify_recursive_naive(words, width, memo):
    # minimise badness over all partitions of words 
    min_badness = sys.maxsize
    total_badness = 0
    j = len(words)
    print(j)
    for i in range(1, j):
        print("justify_naive: start prefix (0, %d), suffix (%d, %d)" % (i, i, j))
        total_badness = badness(words[0:i], width) + justify_recursive_naive(words[i:], width, memo)
        print("justify_naive: end prefix (0, %d), suffix (%d, %d)" % (i, i, j))
        #print total_badness
        #if total_badness >= sys.maxint:
        #    break
    return total_badness
    
# min_badness = justify_recursive_naive(words, 12, {})

print("min_total_badness: %d" %(min_total_badness(['a', 'b'], 2)))

"""
Ask questions
Brute force
Solve by hand, DIY
BUD
DS + Alg brainstorm
Divide and conquer
Walkthrough
Test
Implement

"""
