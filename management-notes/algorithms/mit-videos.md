# Peak Finding

* O - upper bound (worst case)
* Theta - upper and lower bound
* Omega - lower bound (best case)

* Local peak - surrounding by numbers which are smaller or equal
* 1d peak finding - binary search

## 2d peak finding

* Pick middle column
* Find 1d peak
* Check neighbour
* Move in direction of larger neighbour
* Recurse (pick middle column of smaller matrix)

# 2. Document distance, models of computation

* Algorithm
  - Comes from Al Khwarizmi
  - Computation procedure for solving a problem
* An algorithm is the mathematical analogue of a computer program

## Random access machine

* RAM modeled by big array
* Word is w bits
* On words, can load, compute, store in constant time

## Pointer machine

* Dynamically allocated objects
* Object has O(1) fields
* Field = word | pointer to another object or null/nil/none
* Following a pointer costs constant time

## Python model

1. RAM
  - "list" (implemented as an array, they are not linked-lists)
  - l[i] = l[j] + 5     constant time
2. Pointer machine
  - x = x.next    constant time

## Document distance

* document = sequence of words
* word = string of alphanumeric characters
* D[w] = #occurences of w in D
  
* Vector calculus - inner product (dot product)

1. Split document into words
2. Compute word frequencies
3. Compute dot product

The fox is in the hat.
The fox is outside.

the 2       the 1
fox 1       fox 1
is 1        is 1
in 1        outside 1
hat 1

Inner product (dot product):

    2 * 1
+   1 * 1
+   1 * 1
+   1 * 0
+   1 * 0
+   0 * 1

vector angle (something more complicated)

# R2. Python Cost Model, Document Distance

# 3. Insertion Sort, Merge Sort

* Why sorting?
  - Obvious applications (phonebook, spreadsheets, etc.)
  - Problems that become easy once items are sorted
  - Not so obvious applications: e.g. data compression, computer graphics 

## Insertion Sort

* O(n^2)

* Sorting - be aware of assumption that comparison is O(1) and cheap

A[0:i-1] is sorted, so could improve by doing a binary search in O(lg i) time

Swaps are O(1) on array, but insertions are not

## Merge Sort

* Merging two sorted arrays/lists is trivial
* Sorting two elements is trivial
* Use divide an conquer to combine the above to create merge-sort


merge_sort(a)


merge(a, b)
    for i, j, k in a, bc
        if a[i] >= b[i]
            out[k++] = a[i++]
        else
            out[k++] = b[j++]

20 13 7 2 12 11 9 1

