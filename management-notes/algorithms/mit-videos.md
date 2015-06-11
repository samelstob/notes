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

* Need to download handout

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

Recurrence

T(n) = C1 + 2T(n/2) + Cn
      divide + recursion + merge

Recursion tree:

   ^                        cn                  = cn
   |                cn/2            cn/2        + cn
1+lg n         cn/4    cn/4    cn/4    cn/4     + cn
   |           <-------------n------------>

T(n) = (1 + lg n).cn
     = O(n lg n)

### Auxiliary space

Insertion sort is in place (no auxiliary space)
Merge sort - O(n) auxiliary space
In-place merge sort - constant factors worse than merge sort so often
impractical

R3. Document distance, insertion sort, merge sort

* Need hand out

# 4. Heaps and Heap Sort

## Heap

"One of the cutest little data structures ever invented"

Priority queue

* Implements a set S of elements
* Each element associated with a key
  - insert(S, x): insert element x into set S
  - max(S): return element of S with largest key
  - extract-max(S): return element with largest key and remove it from S 
  - increase-key(S, x, k): increase value of x's key to new value k
  - build-max-heap: from unsorted array

An array visualised as a nearly complete binary tree

16 14 10  8  7  9  3  2  4  1

* Index 1 is the root

                1
            2       3
        4   5   6   7
    8    9 10 

parent = i/2
left child = 2i
rigth child = 2i + 1

Max heap - key of a node >= keys of children
Min heap 

### max_heapify(A, i)

max_heapify: Correct a single violation of the heap property in a subtree's
root

Assume that the trees rooted at left(i) and right(i) are max heaps
 
Visualisation of a heap is a nearly complete binary tree.  The height of the
tree is bounded by log n.

build_max_heap(A):
    for i = n/2 down to 1
        do max_heapify(A, i)

elements A[n/2+1..n] are all leaves

Observe max_heapify takes O(1) for nodes that one level above leaves and in
general O(l) time for nodes that are l levels above the leaves

Total amount of work in for loop
n/4 (1 c)
+ n/8 (2 c)
+ n/16 (3 c)
+ 

bounded by a constant

build_max_heap can be done in O(n)

heap_sort
    1. build_max_heap
    2. find maximum element
    3. swap elements a[n] with a[1].  Now max element is at end of the array
    4. Discard node n from heap.  Decrementing heap size
    5. New root may violate max heap property but children are max heaps.  Run
       max_heapify to fix.

