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

# Binary Search Trees, BST Sort

Invariant in a heap is pretty weak - only the root is min or max.  Compared to
a BST

Invariant for BST: For all nodes if Y is in the left subtree of X then key(Y)
<= key(X) 

Insertion is O(h) where h = height of tree

min() - O(h)
max() - O(h)
next_largest() - O(h) 
rank(t) - How many nodes <= n

## RAnk

Augment BST structure with count of nodes below (i.e. in subtree)

            49(6)
      46(2)      79(3)
  43(1)      64(1)  83(1)

* Walk tree
* As you walk, add in nodes that are smaller
* Add in sub-tree sizes to the left

e.g.

rank(79) = 49 + subtree-size(46) + 79 + subtree-size(64)
rank(79) = 1 + 2 + 1 + 1

# R5. Recurssion trees, BST

Merge sort recurrence formula

       "call merge sort twice on arrays half the size" + merge
       T(n) = 2T(n/2) + O(n)

Draw call graph

                              N
                    N/2               N/2
                N/4     N/4       N/4     N/4
              ...

Base case   1   1   1   1   1   1   1   1   1   1   1

T(N) = 2T(N/2) + O(N)
T(1) = O(1) 


                              CN
                    CN/2               CN/2
                CN/4     CN/4       CN/4     CN/4
              ...

Base case   C1   C1   C1   C1   C1   C1   C1   C1   C1   C1   C1

Total cost = sum of each level


level 1                       CN                      N/2^0
level 2             CN/2               CN/2           N/2^1
level 3         CN/4     CN/4       CN/4     CN/4     N/2^2
              ...

Base case   C1   C1   C1   C1   C1   C1   C1   C1   C1   C1   C1

N/2^l-1 = 1
2^l-1 = N
l-1 = lg(N)
l ~ lg(N)

Base case is CN  

T(N) = CNl
     = O(N lg N)

## Data structure operations

* Queries
  * Max, min
  * Next-larger
  * Search
* Updates
  * Insert
  * Delete

Representation Invariant (RI) - Rep Invariant

check_ri - Check that the RI holds

## Augmented BST

* Store additional info in node that can easily be recalculated upon tree
  updates in O(h) time
  e.g. min, max, rank

# 6. AVL Trees, AVL Sort

Binary tree's are not necessarily balanced.

depth of node = levels down from root
height of node = levels up from leafs, starting from zero i.e. leafs are zero
               = max(height(left child), height(right child)) + 1

AVL trees store the heights (augmented BST).  When the heights differ 

Rep Invariant = Height of left and right subtrees of every node differs by no
more than 1

|h(l) - h(r)| <=1

We want to prove that for N nodes, how large can the height be (is it lg N)

N(h) = min #nodes in an AVL tree of height h

If we fix the height to h, what's the fewest nodes we can pack in?

The worst case for a binary search tree is N(h) = h:

      1             ^
        2           |
          3         | h
            4       |
              5     |

The ideal case is N(h) = 2^h:

                          16
                8                    24
         4           12        20          28
      2    6     10    14   18     22    26   30
    1  3  5  7  9 11 13 15 17 19 21 23 25 27 29 31

but any constant to the power of h will do so that the inverse is log.

Worst case is when right subtree has height 1 more than left for every node

How do we analyse 

T(n) =  

      1         R

      2     l       r

      3   l   r    l   -

      4 l   - l  - - -  -  -  

2^h - 2^(h-2)

h * h * h * h - h * h

Recurrence

N(h) = 1 + N(h-1) + N(h-2)

Looks like Fibonacci (actually +1 at each level)

N(h) > F(h) = Phi^h / 5^0.5

We want to know how h relates to n, which is inverting the formula

Phi^h/5^0.5 < n

h < 1.440 lg n

This is pretty good constant.  We would like 1, but 1.440 is still good.


