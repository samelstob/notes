digraph

# 6.006

* Efficient procedures for solving large problems.
* Scalability
* Classic data structures
* Real implementations in Python

"By fun I don't mean easy, I mean challenging and worthwhile so at the end of
it you feel like you have learnt something"

# Peak Finding

* O - upper bound (worst case)
* Theta - upper and lower bound
* Omega - lower bound (best case)

* Local peak - surrounding by numbers which are smaller or equal
* 1d peak finding - binary search

What is the recurrence relation?

  T(n) = T(n/2) + Θ(1)

Base case

  T(1) = Θ(1)

Complexity

  Θ(log₂n)

This is the difference between 2^n and n

## 2d peak finding

1. Greedy ascent algorithm - Θ(mn) complexity

i.e. it's possible to touch every element

2. Try to jam binary search into 2d version

Find a 1D peak on column, then use that column to find one peak on row

This algorithm is incorrect.  A 2D peak may not exist on row i

3. 

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

## AVL Insert

1. Simple BST insert
2. Fix AVL property using rotations from the changed node up

Insert 23

                       4(4)

            20(3)                   65(1)

       11(0)   29(2)           50(0)

              26(1)

            23(0)

### Rotations

* O(1)
* In-order traversal remains the same
* Reversable

Right rotate 29

                       4(3)

            20(2)                   65(1)

       11(0)   26(1)           50(0)

          23(0)   29(0)

Insert 55

                       4(3)

            20(2)                   65(2)

       11(0)   26(1)           50(1)      (-1)

          23(0)   29(0)          55(0)

Left Rotate 50

                       4(3)

            20(2)                   65(2)

       11(0)   26(1)           55(1)    (-1)

          23(0)   29(0)    50(0) 

Right rotate 55

                       4(3)

            20(2)                   55(1)

       11(0)   26(1)           50(0)      65(0)

          23(0)   29(0)

- if x's right child is right-heavy or balanced

      x                         y   
   A      y       LR(x)     x     C
        B   C             A   B

- else

          x

AVL sort

1. Insert n items
2. In-order traversal

Abstract Data Type

# R6. AVL Trees

## BST operations

* Find/Search
* Insert
* Delete
* Next-larger/Next-smaler
* Min
* Max

All operations are O(h)

* AVL doesn't care about node count
* Height of empty tree is -1

AVL Rep Invariant

For every node |h(r)-h(l)| <= 1

## Proving the height is lg(n)

Minimum number of nodes

        n     0

        n     1
          n   0


        n         2
      n   n       1
            n     0

          0             3
       1       1        2
        2    2   2      1
                  3     0

      N(h) = N(h-1)+N(h-2)+1

      N(h) ~ phi^h

All the magic in AVL is in the rebalance (insert and delete are the same as a
plain BST)

* Calculate the new height

Perfect BST - full except the last level

## Rebalancing AVL

# Lecture 7: Counting Sort, Radix Sort, Lower bounds for sorting

## Comparison Model

* All input items are black boxes (ADTs)
* Only operations allowed are comparisons (<, <=, >, >=)
* Time cost = #comparisons

## Linear-time sorting

(Integer sorting)

### Counting Sort

Relies on RAM model 

* Create an array of k empty lists to "count" items with each key
* Append value with key to list at position k 

  3a 6a 3b 1a 2a 8a 2b 3c

  1 -> 1a
  2 -> 2a 2b
  3 -> 3a 3b 3c
  4
  5
  6 -> 6a
  7
  8 -> 8a

### Radix Sort

Apply d rounds of counting sort to a string of d digits starting from least
significant

Relies on stable counting sort

# R7: Comparison Sort, Counting Sort, Radix Sort

# R8: Hashing with Chaining

Searching faster than lg n time

O(1) with high probability

"Two types of database, those that use hashing and those that use search
trees"

Prehash - map keys to integers.  At this point not worrying about
how big those integers are

## Analysis

- Expected length of chain for n keys, m slots = n/m

  = n/m = alpha = load factor
  = O(1) if M = O(n)
  = O(1 + |chain|)
  = O(1 + alpha)

## Hash functions

1. Division method

  h(k) = k mod m

2. Multiplication method

  h(k) = [(a.k) mod 2^w] >> (w-r)
  
  assuming w bit machine

  Φ

3. Universal hashing

  h(k) = ((ak + b) mod p) mod  m)

  p = prime > |u|

  a,b {0,..,p-1}

# R8. Simulation Algorithms

# 9. Table Doubling

We don't know the size of m (number of slots).

Use table double to amortise cost of growing/shrinking the table

= Θ(1 + 2 + 4 + 8 + .. n)

Amortisation "Spread out the high cost so it's cheap on average"

Randomised data structure

If grew table by 1 then we would be

## Deletion

Don't want to shrink when it gets to half size (n=m/2) we will flip/flop between
doubling and halving the table.

Instead use e.g. m/4

## Resizable arrays

Use same technique

## Grep (String matching)

### Simple algorithm

is s in t?

any(s==t[i:i+len(s)]
  for i in range(len(t)-len(s))

  Θ(|s| * (|t|-|s|))
  = O(|s| * |t)

### Karp-Rabin

  Rolling hash ADT

  - compute hash function of s (search string)
  - use rolling hash function to calculate hash of first s characters of t
  - if not equal, roll hash one character over in t
  - if equal, do character by character check

linear time for one match

O(|s| + |t| + #match X |s|)

#### Rolling hash function

- division method
= h(k) = k mod m
- m use a random prime >= |s|

to shift over, use 

# R9: Rolling Hashes, Amortised Analysis

n   the fox is in the hat

k   "the" -> h(k)

Naive string matching is O(|n||k|)

* Computing hash of k
* Computing rolling hash of first three characters of n.
* Compare hashes of k and n
* If not match, then roll hash of n along one character

Can we make a hash function without duplicates?

Universe of inputs:  number of characters ^ length of string e.g. 256^100000
Universe of outputs: 2^64

Rolling hash needs to be O(1) for this to work

  3 14 15 29 65

slide:xa

## Multiplicative inverse

Where p is prime

  a {1 .. p-1}
  a(-1) {1 .. p-1}  -- Multiplicative inverse

  a X b X a(-1) = b mod p

  a X a(-1) = 1 mod p

e.g.

  p = 23

  6 X 4 = 24 mod 23 = 1

## Amortised analysis

Look at all the operations, rather than one operation at a time.  Make an
argument for the average cost

Table doubling

  D I D I I D I I I D I I I I I I I D I I I I I I I I

The cost of the expensive operation (table doubling) is evenly spread over
cheap operations (insert).

In-order traversal

  min
  while(successor)

successor is O(h) (lg n if balanced) so this traversal algorithm should be
O(n lg n)

However, if you look at all the operations we only traverse each edge twice.

There are O(n-1) edges so there are 2n traversals - O(n) asymptotoically

# R9b DNA sequence matching

With random inputs most hash functions will do a good job of producing a
random output.  The problem is that real life inputs are not random.

For example if you get pixels from a camera, the last few digits may be the
same due to noise.  Strings may all start similarly (e.g. list of file paths)

If a non-random property of the input (e.g. evenness) is reflected in the output then that is a bad hash function.

Although shift may be quicker than mod, better hash functions (e.g. mod) give
better performance overall.




# 10. Open Addressing, Cryptographic Hashing

## Open Addressing

* Hash tables with no chaining!
* Probe hash table until find an empty slot
* Need a hash function that specifies the order of slots to probe

## Cryptographic Hashing

### Password storage

* One-way.  Given h(x) it is very hard to find x

# R10. Quiz 1 Review

# 11. Integer Arithmetic, Karatsuba Multiplcation

Sometimes we want to compute with numbers longer than word length

## Irrationals

Pythagoras "All is numbers".

  \
  |\
  | \ √2 
1 |  \
  |   \
  ------
    1

### Catalan Numbers

Set P of balanced paraenthesis strings

1) 

wtf

### Newton's method

Let's say you have a function y = f(x)

We are going to try and find the root of f(x) = 0 through successive
approximation (i.e. where the function crosses the x-axis on a graph).

f(x) = x²-a

Newton's method uses tangents and successive approximation

To find x[i+1]

1. Find the gradient of the curve (the tangent) at x[i] (the deriviative).

  derivative f(x) = f'(x) (f prime)

2. Follow the gradient linearly to the x-axis

        |                          /
        |                         /
        |                       -/     y = f(x)
        |                     -//| slope = f'(x)
        |                   -/ / |
        |                 --/ /  |
        |              --/   /   |
        |           --/     /    |
  -----------------/-------------------------------
        |      ---/   x[i+1]     x[i]
        |  ---/
       -+-/
   ---/ |

Equation for tangent line:

  y = mx + b

      ^    ^
      |    |
  slope    y-intercept

  Slope = derivative = f'(x)

  y-intercept: y = f(x) where x = i

  Point-slope form

  y - y[0] = m(x-x[0])

  y - f(x[i]) = f'(x[i])(x-x[i]

  y = f'(x[i])(x-x[i]) + f(x[i]

Solve for y=0

  0 = x[i+1]-x[i] + f(x[i])/f'(x[i]

  x[i+1] = x[i] - f(x[i])/f'(x[i])

Unit circle:

  tangent = opposite / adjacent

  f'(x[i]) = f(x[i]) / (x[i]-x[i+1]) 

  f'(x[i]) . (x[i]-x[i+1]) = f(x([i])

  x[i]-x[i+1] = f(x[i]) / f'(x[i])

  x[i] - f(x[i])/f'(x[i]) = x[i+1]

  x[i+1] = x[i] - f(x[i])/f'(x[i])

3. Use that x value as the input to the next iteration

Note: Most division algorithms have multiplication as a subroutine

Problem: Calculate √2 to d places

### High Precision Multiplication

# R10. Algorithm Design

## Searching a shifted array

# 12. Square Roots, Newton's Method

## High Precision Division

We want a/b

We will compute R/b where R is a large value such that it is easy to divide by
R (R=2^k)

Newton's method for computing R/b

f(x) = 1/x - b/R

f'(x) = -1/x²

Division: Quadratic convergence - # digits doubles at each step

# R12 Karatsbua Multiplication, Newton's Method

# 13: BFS

## Graph search "exploring a graph"

* Web crawling
* Social networking
* Network broadcast
* Garbage collection
* Model checking
* Checking mathematical conjecture
* Solving puzzles and games

6042

graph G=(V,E) directed or undirected

### Pocket cube (2x2x2)

#vertices = 8! x 3^8

Configuration graph
* Vertex for each possible state of the cube
* Edge for each possible move (moves are reversible so the graph is
  undirected)

The worst case is the width of the graph (11 moves for 2x2x2, for 3x3x3 = 20)

## Graph representation

* Adjacency lists
  * Array Adj of |v|
  * Linked lists
  * For each vertex u
    * Adj[u] stores it's neighbours

* For graph exploration this is what you want.
* There are different ways to implement adjacency lists:
  * Array
  * Hash table
  * v.neighbours
  * Adj[u] is a function (i.e. not stored, computed)

  |V|+|E| size

Ideally our algorithms will run in V+E time - that's what you need just to
look at the graph.

* BFS
  * Visit all nodes reachable from given starting point s
  * O(V+E) time
  * Careful to avoid duplicates (revisiting)

O(V+E) is essentially optimal - it's linear in the size of the graph.  Ideally
all our algorithms will run in V+E time.

BFS(s, adj)
  level = {s:0}
  parent = {s:None}
  i=1
  frontier=[s]
  while frontier:
    next = []
    for u in frontier:
      for v in Adj[u]:
        if v not in level:
          level[v]=i
          parent[v]=u
          next.append(v)
    frontier=next
    i+=1

* Parent pointers all lead to s and form a shortest path
* Works on directed and undirected graphs
* Could be used to detect which vertices can not be reached from S

Sometimes you want to visit every vertex so you need another outer loop so you
can iterate over all the vertices even if the graph is disconnected.

# R13: BFS



# 14. Depth-First Search (DFS), Topological Sort

Like exploring a maze

* Recursively explore graph, backtracking as necessary 

parent = {S : None}
dfs-visit(Adj):
  for v in Adj[S]
    if v not in parent:
      parent[v] = S
      dfs-visit(Adj[v])
    
dfs(V, Adj):
  parent = {}
  for S in V:
    if S not in parent:
      parent[S] = None
    dfs-visit(V, Adj[v])

## Analysis

  Θ(V + E)

Linear time just like BFS

* BFS versus DFS
** BFS great for shortest paths (e.g. fastest way to solve rubick's cube, DFS
will not find it)
** DFS - edge classification

## Edge classification

* Tree edges (parent pointers)
  * When we visit a new vertex by this edge.  They form a directed tree (a
    forest)
* Forward edges: node->decedent in tree 
* Backward edges: node->ancestor in tree (grey/currently exploring)
* Cross edges: between two non-ancestor related subtrees

Use counters (start/finish time) to determine cross edges from forward edges

## Cycle detection

G has a cycle if G has a back edge

Detecting cycles is pretty easy in undirected graphs.  It's a little more
subtle in direct graphs because you have to worry about edge direction.

## Topological Sort

Sorting vertices in a graph

Job scheduling:

* Given a DAG
* Order vertices so that all edges point from lower order to higher order

Solution:

* Run DFS
* Output the reverse of finishing times of vertices (every time you finish a
  vertex, add it to a list)


# 15: Single-Source Shortest Paths Problem

G(V,E,W)
Vertices
Edges
Weights W E->R

* Simple graph - at most one edge between any pair of vertices
* Complete graph - has an edge between each pair of vertices
* Multi-graph - could have multiple edges between pairs of vertices

An upper bound or E is V² (in a complete graph)

* Optimal Substructure

* Path
  - Path must consist of edges in the graph
  - (v[i], v[i+1]) ϵ E for 0 
  - Weight of path, is sum of weights of edges on the paths

The problem is to find P with minimum weight

Two algorithms

* Dijkstra
  ** non-negative edges
  ** O(VlgV + E)

* Bellman-Ford
  ** positive and negative edges
  ** O(VE)
  ** E could be V² so O(V³)
  ** When you can, use Dijkstra

Neither algorithm is a function of weight.  The dynamic range of the weights
can be very very large.

With these algorithms you want the weight, but you also want the path as well.

δ(u,v) = {min{w(p) u->v}} ∃ any such path otherwise ∞

∃ there exists

min of all possible paths from u to v

d(v) Value inside circle - current weight
π(v) Predecessor on best path to v  π(s) = NIL

## Negative weights

Motivation for negative weights

Negative cycles can make shortest path lengths indeterminate.  We want
algorithm to mark these with -∞ 

## Relaxation

General Structure:

* Initialise for u
* Repeat select edge (u,v)
* "Relax" edge (u,v)

  if d[v] > d[u] + w(u,v):
    d[v] = d[u] + w(u,v)
    π[v] <- u

Until all edges have d[v] <= d[u] + w(u,v)

## Optimum substructure

* Sub paths of a shortest path are shortest paths

# R15: Shortest Paths

BFS find shortest paths without weights.

Intuitively we want BFS to favour paths with lower weights.

## Exponential number of paths

There are potentially exponential number of paths for any graph

      A       D       G
  S       C       F       I
      B       E       H

      2       2       2

      2       4       8

    2^n i.e. exponential in the number of vertices

Think of some alternative ways to create a SSSP algorithm:

In real-life you will not be creating new algorithms e.g. have to do analysis on running time and correctness, have to create proof

You are more likely to be using algorithms as black box and transforming the
problem to fit

e.g. Could create dummy nodes to simulate weights.  Run BFS.  Remove dummy
nodes.

New running time is:

   E = O(W'E')
   V = O(W'E' + V')
     = O(V' + W'E')

  Dijkstra  O(E lg V)    -- With fancy data structure O(VlgV + E)
  BF        O(V.E)

If W <= lg V this algorithm is on par with Dijkstra

## Consider a problem where two drivers alternate but one must do the first leg
and the last leg.

* Need a SP with odd number of edges
* Modify the input and then run Dijkstra
  * Duplicate each node
  * Construct even and odd graphs from original 

## Highway with traffic

* Each edge has two additional considerations
  * time cost ()
  * fuel cost ()

Take a variable and make it a state

Make time a state

* For each vertex, duplicate it M times (number of minutes in a day)
* Modify the input graph to create M copies
* Allow for waiting - at each vertex, create an edge t+1 which loops back

  E' = EM + VM
  V' = VM

# 16: Dijkstra

Review

  S(0) →1→ A(∞)
   \       ↓
     \     1
       3   ↓
         \ B(∞)

  δ(S,v) = 2

d[v]      length of current shortest path from source S to v
δ(s,v)    length of a shortest path
π[v]      predecessor of v in the shortest path from S to v.  Can follow the
predecessor to construct the shortest path

Relax(u,v,w)
  if d[v] > d[u] + w(u,v)
    d[v] = d[u] + w(u,v)
    π[v] = u
    
Lemma: The relaxation operation maintains the invariant that d[v] >= δ(S,v)
for all v ϵ V

By △ inequality δ(S,v) <= δ(S,u) + δ(u,v)

In other words, if there is a shortest path from S to v, then a shortest path
from S to v that goes through node u must be no shorter (otherwise it would
*be* the shortest path from S to v)

* δ(a,b) is the shortest path from a to b (it may be direct or indirect i.e.
 travel through other nodes)

  δ(S,v) <= d[u] + w(u,v) = d[v]

## DAGs

* Can't have cycles
* Can have negative weights, just no cycles

1) Topologically sort the DAG.  Path from u->v implies that is u is before v
in the ordering
2) One pass over vertices in topologically sorted order relaxing each edge that
leaves each vertex.

## Dijkstra

Dijkstra is a greedy algorithm

Dijkstra(G,W,S)
  Initialise (G,S)

  Q.add(s)
  for each v in adj[u]
    Q.add(v)    # queue is ordered by weight ascending
    Relax(u,v,w)

  while Q:
    u=Q.remove  
  # Once we have traversed all edges from v, remove v from q
  Q.remove(v)


# R16: Rubick's Cube, Starcraft Zero

2x2x2 Rubik's cube

2^3 cubes =  8
half the faces are not visible so 8x3 faces = 24

How many configurations are there?

24 faces can be mapped in any of the 24 available positions

Permutations - 24!

Can we afford to build the graph and then run BFS? Nope.  Going to have to
operate on an implicit graph representation.

## Inverse Permutations

  1 2 3 4 5 = π
  3 4 1 5 2

  a b c d e
  c d a e b = inverse π
  a b c d e

  Swap and sort the original permutation

  3 4 1 5 2
  1 2 3 4 5

  1 2 3 4 5
  3 5 1 2 4
  
## Starcraft



# 17: Bellman-Ford

* Negative weights and negative cycles

Naive SP algo:

1. Can take EXP time
2. With negative cycles, never completes

* "Polynomial time is great, exponential time is bad, infinite time gets you
  fired"

    Initialization
    for i=1 to |V| - 1
        for each edge (u,v) ϵ E
            Relax(u,v,w)
    for each edge (u,v) ϵ E
        if d[v] > d[u] + w(u,v)
            then report -ve cycle exists

Relax:
  if d[v] > d[u] + w(u,v)
      d[v] = d[u] + w(u,v)
      π[v] = u

If there are no negative cycles then after |V|-1 passes we will have the
correct weights.

E=O(V²)

So Bellman-Ford could be V³

Dijkstra can be linear complexity compared to Bellman-Ford which is cubic.

If you can use Dijkstra, unless you have negative weight cycles.

## Theorem

If G=(V,E) contains no -ve weight cycles then after B-F executes then d[v] =
δ(s,v) for all v ϵ V

Corollary: If a value d[v] fails to converge after |v|-1 passes there exists a
-ve weight cycle reachable from S

After 1 pass through E we have d[v] = δ(S,v1) because we will relax edge
(v0,v1)

After k passes d[vk] = δ(S,k)

Because we have optimum substructure

Corollary proof:

  After |V|-1 passes, we find an edge that can be relaxed then the current
shortest path from S to some vertex is not simple (have a repeated vertex)

## Longest paths

* Can't naively translate positive weights to negative weights because we may
  create negative weight cycles

* If you have a graph with negative weight cycles it is NP-Hard

# 18: Shortest Paths IV: Speeding up Dijkstra

Improving in real-world cases

* Single-source, single target
* Bi-directional search
* All pairs shortest paths

## Single-source, single target (s->t)

Emphasise that worst-case complexity is unchanged

  Initialize() <- d[s]=0, d[u != s]=∞
  Q<-V[G]
  while Q != empty
    do u <- extract-min(Q)  # Stop if u=t
    for each vertex V ϵ Adj[u] 
      do relax(u, v, w)
        π[v] <- u
        d[v] = d[u] + w(u, v)

Basically, stop Dijkstra when target is extracted from the queue. (Proof?)

Runs no-slower than Dijkstra (if target is the last vertex you find).

## Bi-directional search

- Alternate forward search from S with backward search from t (following edges
  backwards)

df[u] : distances for forward search
db[u] : distances for backward search

Priority queues: Qf : forward
                 Qb : backward

πf: normal
πb: following edges back

Q: What is the terminating condition?

Some vertex w has been processed both in the forward search and the backward
search i.e. extracted from both Qf and Qb.

w is intersection of two frontiers

Q: How do we find the shortest path?

Find S.P. from s to w using π[f]
Find S.P from w to t using π[b] backwards

However w may not be on the shortest path

     3  (u)  3   (u')  3 
 (s)                      (t)
       5    (w)    5 

If we run Dijkstra the shortest path is 9 (s->u->u'->t)

                       Q
  -----------------------------
  s0                 | u3 w5
  s0 u3              | w5 u'6
  s0 u3 w5           | u'6 t10
  s0 u3 w5 u'6       | t9
  s0 u3 w5 u'6 t9    |

However, bi-direction search would meet not on the shortest weight path, but
the nearest (fewest nodes):

  s0                 | u3 w5  
  t0                 | u'3 w5

  s0 u3              | w5 u'6
  t0 u'3             | w5 u6

  s0 u3 w5           | u'6 t10
  t0 u'3 w5          | u6 s10

Bi-directional search terminates because we have removed w from both
directions.

However, w is *not* on the shortest path from s->t.

Instead we look for the node with the lowest distance from s+t that
has been processed by at least one direction

s(0+10) u(3+6) u'(3+6) w(5+5) t(10+0)

## Goal Directed Search

Modify edge weights with potential function

If there is a landmark that you know you have to go through from s->t, modify
the weights so that Dijkstra favours that path.

Doesn't change the asymptotic complexity but in practice should visit fewer
nodes before terminating.

# 19. Dynamic Programming I - Fibonacci, Shortest Paths

Especially good at optimisation problems - e.g. finding the minimum or
maximum.

D.P is sort of "careful bruteforce".  There are lot of problems where
essentially the only known polynomial time algorithm is a DP algorithm

D.P is sort of subproblems + "re-use"

Take a problem, split it into sub-problems, solve those sub-problems, and
re-use those solution to sub-problems

## Why is it called DP?

Invented by Richard Bellman (of Bellman-Ford algorithm).

Bellman invented the name to hide the fact he was doing mathematical research.

## Fibonacci numbers

F1 = F2 = 1
Fn = Fn-1 + fn-2

Goal: Compute Fn

### Naive recursive algorithm

fib(n):
  if n <= 2:
    f=1
  else:
    f=fib(n-1)+fib(n-2)
  return f

Exponential time (EXP)

T(n) = T(n-1) + T(n-2) + O(1)
    >= Fn ~ goldenratio^n
            φ

T(n) >= 2T(n-2)
      = 2^(n/2)

### Memoized DP algorithm:

memo = {}
  if n <= 2:
    f=1
  else if n in memo:
    f=memo[n]
  else:
    f=fib(n-1)+fib(n-2)
    memo[n] = f
  return f

T(n) = T(n-1) + O(1)

Recursion Tree

                Fn
        Fn-1            Fn-2

    Fn-2    Fn-3     Fn-3    Fn-4
    
fib(k) only recurses the first time it's called ∀k

- memoized calls cost O(1)
- # non memoized calls is n

So it's O(n)?

(Best algorithm for Fibonacci is logn (wtf?)

### DP ~ recursion + memoization + guessing

- Memoize (remember - like a memo pad) & reuse solutions to subproblems that help solve the
  problem

- Time = # subproblems X time/sub-problem
- Don't count memoized recusrions

### Bottom up DP algorithm (no recursion)

  fib = {}
  for k in range(k)
    if k<=2:
      f=1
    else:

* Exactly same computation
* Topological sort of subproblem dependency DAG
  - In the case of Fibonacci the dependency DAG is very simple
* Can often save space

XXXSE Thinking about this some more: i) we don't need a hash table - just an
array would do as the keys are the integers ii) we only need to remember the
last 2 results (Constant space not linear) to calculate the next Fibonacci number, we don't need a
complete history - anyway I understand that the point is to illustrate to
general principal of recursion + memoization

In the bottom-up version it is more obvious that it is linear time

## Shortest paths

Single source shortest path:

  δ(s,v) ∀ v

Guessing: Don't know the answer? guess - try all guesses & take best one

Sub paths of shortest paths are shortest paths - optimal sub-structure.

CLRS has a succint definition of Optimal Sub-structure - something like
"The global optimal solution contains optimal solutions to sub-problems"

Guess the last edge u->v in the shortest path from s->v.  Minimise over all
the possible u->v choices

  δ(s,v) = δ(s,u) + w(u,v)
          ∀ (u,v) ε E

XXXSE So are they saying that to compute the S.P., calculate the shortest path
to u of all incoming edges, of all incoming edges, of all incoming edges.  I
don't really get it - how do we know when we are done?  Oh well if we have
done all incoming edges, then there is other way to reach u.

                         u''->u
                               \
      s                  u'->u->v
                           \   / 
                            \ /
                             u
v
  for all u with incoming edges to v
    δ(u,v) = min( δ(s,u) + w(u,v) )
  # Now we have done all incoming edges, we know the shortest paths from all
u->v
  # Now for all u with incoming edges to each of those u
    δ(s,v) = δ(s,u') + 

I think I nearly get the idea but I don't see how we can practically calculate the δ(u,v) as we need to wait until all of the results from δ(u,v) δ(u',u) δ(u'',u') are in.
   
  shortest_path(s,v)
    if (s == v)
      return 0
    for all u in (u,v) ε E
      δ(s,v) = shortest_path(s,u) + w(u,v)
    return δ(s,v)

This looks EXP with the base being the avg number of incoming edges (indegree)

XXXSE Doesn't starting at the end and working backwards mean that we could
visit lots of nodes that are not even on a path from S

Will memoization improve this algorithm?  It depends on how much "reuse" there
is?

Infinite time on graphs with cycles

Lesson: Sub-problem dependencies should be acyclic

DAGS: O(V+E)

"This is really the same as DFS to do a topological sort to do one round of
Bellman-Ford.  The min is doing the same thing as the relaxation step.  The
same algorithm but we come at it from a different perspective"

XXXSE Shortest Path

All weights are 1

      S -> v

      δ(S,v) = min( δ(S,u) + w(u,v) )

      1

      S -> u -> v

      δ(S,v) = min( δ(S,u) + w(u,v) )
      δ(S,v) = min( δ(S,u) + 1 )
      δ(S,u) = min( δ(S,u) ) = δ(S,u) = 1
      δ(S,v) = min( 1 + 1 ) = 2

      S -> d -> u -> v

      δ(S,v) = min( δ(S,u) + w(u,v) )
      δ(S,v) = min( δ(S,u) + 1) )
      δ(S,u) = min( δ(S,d) + w(d,u) )
      δ(S,u) = min( δ(S,d) + 1 )
      δ(S,d) = min( δ(S,d) ) = w(S,d) = 1
      δ(S,d) = min( min( w(S,d) + w(d,u)) + w(u,v) )

        1-> a 1-> d 3->
      S 2-> b 2-------> v
        1-> c 2------->

      for u in v where there exists an edge from u to v 
        δ(S,v) = min( δ(S,u) + w(u,v) )

      δ(S,v) = min( δ(S,d) + w(d,v),
                    δ(S,b) + w(b,v),
                    δ(S,c) + w(c,v) )

      δ(S,d) = min( δ(S,a) + w(a,d) )

      δ(S,d) = min( 1 + 1 ) = 2

      δ(S,a) = w(s,a) = 1

      δ(S,b) = w(S,b) = 2

      δ(S,c) = w(S,c) = 1

      δ(S,v) = min( (2 + 3),
                    (2 + 2),
                    (1 + 2) ) = 3

      S -> u -> v           S -> d -> u -> v
           a ->                  e -> a
           b ->                  f ------>

Why doesn't this work from the other end?

1. For all outgoing edges
    δ(S,v) = min( w(S,u) + δ(u,v) )

      3-> 
    S     u 1-> v
      1-> 

    δ(S,v) = δ(S,u) + δ(u,v)

This is incorrect.  The shortest path to v may not pass through u.  This is
shortest path to v that passes through u.

But - SSSP finds the shortest path to all vertices from S, so it seems
intuitve that we would start from S.  Dijkstra starts from S doesn't it?

I need to understand Dijkstra and Bellman-Ford better to compare.


# Lecture 20: Dynamic Programming II: Text Justification, Blackjack

DP ~ "Careful brute force"
  - Reduce the exponential search space to a polynomial one
DP ~ Guessing + recursion + memoization
DP ~ Shortest paths in some DAG

## 5 easy steps

1. Define subproblems
2. Guess (part of solution)
3. Relate subproblem solutions
4. Recurse & memoize
  OR
   Build DP table bottom-up
5. Solve original problem 

## Text justification
## Blackjack

# 23: Computational Complexity

Complexity classes

set of {}
P = { problems solvable in polynomial time }
EXP = { " exponential time }
R = { " finite time }

# Examples

- Negative-weight cycle detection P

## EXP (!P)

- nXn chess EXP
- Tetris EXP (don't whether in P)

# !R

R = { problems solvable in finite time }

- Halting problem (given a program, does it ever halt/stop) !R
  i.e. there is no algorithm that solves it for all programs
- Most decision problems are uncomputable
  - Decision problems (answer is yes or no)
 
# NP

Non-deterministic polynomial

{ decision problems solvable in polynomial time via a "lucky" algorithm }

{ decision problems with solutions that can be "checked" in polynomial time }

## Tetris

Tetris is in NP

We know how to solve in EXP time - just try all the options.

The decision problem "can i survive is in NP" - If I make a guess about each
decision (how to rotate, where to place) and there is a possible yes answer,
then the guesses will find it.

Whenever yes, you can prove & check proof in polynomial time

Tetris = proof is sequence of moves to make

The big question does P = NP?  Big conjecture

"can't engineer luck"

"solving problems is harder than checking solutions"

# NP-hard

As hard as every problem in NP (the hardest extreme of NP)

# NP-complete

Intersection of NP and NP-hard (like Tetris - just on the line)

* Travelling salesman (shortest path that visits all vertices)
* Longest common subsequence for 'n' strings
* Minesweeper, Sudoku, most puzzles that are interesting
* SAT
  * Given a boolean formula, is there some setting that makes it true
    (actually the first problem that was shown NP-Complete)
* 3-colour graph colouring
* Shortest path in 3D
* Knapsack

# Reductions

Have a problem A, convert into problem B that you know how to solve (e.g.
convert it into a graph problem)

e.g. Dijkstra works with weighted paths, if you have unweighted you could set
each weight to a constant

e.g. Min-product path -> shortest path.  Solution: convert problem to use logs

Longest path -> Shortest path - negate all the weights

3 Partition [Karp] is NP Complete

All NP Complete problems you can reduce to each other

# 24. Topics in Algorithm Research

Problems in parallel architectures

# Geometric Origami

Hyperbolic parabola - Bauhaus
Algorithmic Sculpture
* There is an algorithm - any set of polygons on a plane you can fold and make
  one straight cut and get exactly those polygons.

Memory hierarchy

# Cache oblivious algorithms (minimise number of transfers)
* Search O(logB n) : B size of cache line
* Sorting O(n/B
 
Integer data structures

n integers {0,..,u-1}

Improving on trees for insert, delete, successor, predecessor 
* O (lglgu)
* Fusion trees O (lg

