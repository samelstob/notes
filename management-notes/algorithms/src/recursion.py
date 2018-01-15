#!/bin/env python3

"""
Base case - instance of the problem which can be solved trivially

There may be more than one base case.

Often it will be the identity value for a function e.g. 1 is the identity value for product, 0 is identity for sum

f(a,x) = a

Recursive step - reduce to a smaller instance of the same problem - heading towards the base case

Don't try to think
"""
def count(a):
    # base case
    if a == []:
        return 0
    else:
        # recursive step
        return 1 + count(a[1:])

def sum(a):
    # base case
    if a == []:
        return None 
    elif len(a) == 1:
        return a[0]
    else:
        # recursive step
        return a[0] + sum(a[1:])

def product(a):
    if a == []: # error case
        return None
    elif len(a) == 1: # base case
        return a[0]
    else:
        # recursive step
        return a[0] * product(a[1:])

"""
What did I learn?
1. It's easy to get confused between returning a list, and an element of the list
2. I forgot to return the value in the recursive step
"""
def reverse(a):
    #print(a)
    if a == []: # base case
        return []
    elif len(a) == 1: # base case
        return a
    else: # recursive step
        return reverse(a[1:]) + a[0:1]

if __name__ == "__main__":
    print(count([]))
    print(count(['a']))
    print(count(['a', 'b']))

    print(sum([]))
    print(sum([1]))
    print(sum([1, 2]))
    print(sum([1, 2, 3]))
    print(sum([1, 2, 3, 4, 5]))

    print(product([]))
    print(product([1]))
    print(product([1, 2]))
    print(product([1, 2, 3]))
    print(product([1, 2, 3, 4, 5]))

    print(reverse([]))
    print(reverse(['a']))
    print(reverse(['a', 'b']))
    print(reverse(['a', 'b', 'c']))
    print(reverse(['a', 'b', 'c', 'd', 'e']))
    print(reverse("Hello"))

