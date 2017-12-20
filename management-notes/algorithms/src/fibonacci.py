#!/usr/bin/env python3

"""
Base case - smallest instance - can be solved trivially - often the identity value

Recursive step - Work on a smaller instance of the problem towards the base case
"""

"""
Return the nth Fibonacci number

Naive implementation - follows the recursive mathematical definition
"""
def fib_naive(n):
    if n < 1: # error case
        return 0
    elif n == 1: # base case
        return 1
    elif n == 2: # base case
        return 1
    elif n > 2: # recursive step
        return fib_naive(n-1) + fib_naive(n-2)

"""
Recursion + Memoization version of Fibonacci

Demonstrating the key elements of DP
"""
def fib_memo(n, memo={}, calls=[0]):
    if n < 1: # error case
        return 0
    elif n == 1: # base case
        return 1
    elif n == 2: # base case
        return 1
    elif n > 2: # memoized recursive step
        if n in memo:
            calls[0] = calls[0] + 1
            return memo[n]
        else:
            calls[1] = calls[1] + 1
            val = fib_memo(n-1, memo, calls) + fib_memo(n-2, memo, calls)
            memo[n] = val
            return val

"""
Bottom up Fibonacci

Demonstrating DP can be bottom up

Fib has a simple sub-problem DAG
"""
def fib_dp(n):
    fib = 0
    memo = [1, 1]
    if n < 1:
        return 0
    if n < 3:
        return 1
    else:
        n = n - 2

    for i in range(n):
        fib = memo[0] + memo[1]  
        memo[0] = memo[1]
        memo[1] = fib
    return fib

if __name__ == "__main__":
    calls = [0, 0]
    for n in range(35):
        print("%d: %d" % (n, fib_naive(n)))
        print("%d: %d %d %d" % (n, fib_memo(n, {}, calls), calls[0], calls[1]))
        print("%d: %d" % (n, fib_dp(n)))
