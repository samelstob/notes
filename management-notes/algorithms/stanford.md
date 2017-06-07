# Programming Abstractions

# Lecture 26

* Heapsort - is a great sort for nlogn, doesn't use extra space the way merge
  sort does, doesn't have any degenerate cases, for an unknown set of inputs works
pretty well

* Even insertion sort or bubble sort might make sense if the input is nearly
  sorted

* Sorted vs. not: Do you want to sort it?  Many operations are more efficiently implement if
  the data is sorted
  - Min, max, median, mode, percentile
  - Finding duplicates
  - Merge or intersect arrays
  - Sorting is not free but may be an investment

* Set vs. sorted vector

* Assume set implemented as a balanced binary tree
* Sorted vector tends to be underutilised or underappreciated.  If you don't
  need to add/remove elements often then a sorted vector may be a good choice.
The overhead of a pointer based structure (e.g. balanced binary tree) may add
8 bytes on every element to get that "editability" 

* PQueue - Priority Queue or Heap
  - Weakly sorted structure - gives access to the maximum value
  - PQueue doesn't give you the other benefits of sorting like finding
    duplicates or the mode
  - PQueue isn't really a place you store things and plan on using them again
    and again.   It's really a place you stick things to get them out in an
order.  Its value is in the dequeue - pulling them out - e.g. finding the
highest priority.

* Pointer based versus contiguous memory
  - Have a good idea of what going to a pointer based data structure buys you
    and what it costs you relative to contiguous memory

## MVPs

* Abstraction
  - Leverage existing, Keep complexity down, solve more interesting problems
* Recursion
  - Solve problems that have a self-similar structure.
* Algorithm
  - Big O - sloppy math that computer scientists are fond of
  - Intuition about how to gauge things and their growth
* Implementation
* Appreciation for Design
  - Beautifully, elegant, unified, clean, readable code 
  - Other people you work with would appreciate being involved with
* Not so much
  - Pointers, C++

## Pointers

* Flexible wiring of data structures
* Sharing instead of copying
* Many pitfalls

## To Remember Years From now

* Algorithmic thinking
* Ballparking
  - Back of the envelope calculations
  - "In the era of computers it's easy to get distanced from numbers; punch
    numbers into formulas and not have intuition of whether what comes out is
the right number, whether that number makes sense, whether that number is
grounded, whether that number is an order of magnitude off."
  - "Do some predictions, do some time trials, do some more sketching on your
    numbers, see that things are working out - feel comfortable that the math
and theory are reinforcing each other."
  - "Don't get too distanced from the fact those numbers play out in the real
    world in ways that are interesting and not just let the numbers themselves
tell the story; there really is more to connect it up with."
* Tradeoffs
  - The answer to most questions is "it depends".
  - Space/time and many other factors

* Tradeoffs

