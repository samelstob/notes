# Heap

* Array visualised as a binary tree
* First element is the root
                     1
              2             3
          4     5        6      7
        8  9  10  11  12  13  14  15

 `parent(i) = i/2
  left_child(i) = i*2
  right_child(i) = (i*2)+1`

max_heapify(A, i)

- Invariant: Children are >= parent
 `A[i*2] >= A[i] && A[i*2+1] >= A[i]`
- Correct one violation of invariant

- Go up the tree, swapping element with parent until it is not needed

Initial state:

  1               5
  2          12         9
  4      23     13   10    11
  8   

Append new value at end:

  1               5
  2          12         9
  4      23     13   10    11
  8   6 

Call max_heapify(A, 8) to fix up:

  1               5
  2          12         9
  4       6     13   10    11
  8   23

  1               5
  2           6         9
  4       12    13   10    11
  8   23

## Heapsort

* Take element from head
* Call max_heapify to fix

Initial state:

  1               5
  2           6         9
  4       12    13   10    11
  8   23

Extract max:

5

  1                23 
  2           6         9
  4       12    13   10    11
  8     

# Counting Sort, Radix Sort

Counting Sort (integer sorting)

* In comparison model, O(n lg n) is lower bound
* Can sort in O(n) if we use RAM model and can place constraints on the input
* n items
* keys are integers
* k max key

Create an array of buckets from k.min to k.max

0
1
2
3
4
5

* For each key, append the value to the k'th bucket
* Walk through the buckets in order to get the sorted list

Counting sort only makes sense when n and k are similar in size

## Radix Sort

* Divide the key into d digits of base b
* Apply d rounds of counting sort for each digit in turn, starting with the
  least significant:

  JFKA
  MVHA
  IANV
  QPVK
  INWK 
     ^

  JFKA
  MVHA
  QPVK
  INWK 
  IANV
    ^

  MVHA
  JFKA
  IANV
  QPVK
  INWK 
    ^

  IANV
  JFKA
  INWK 
  QPVK
  MVHA
   ^

  IANV
  INWK 
  JFKA
  MVHA
  QPVK
  ^

Radix sort needs a stable counting sort

Wednesday, 02 September 2015

Newton's method

Use the tangent line to a function to successively approximate the root of the
function.  

  Slope of tangent = f'(x)

  Equation for tangent line

  Point-line format:

  y-y0 = m(x-x0)

  y-y[i] = m(x-x[i])

  y-f(x[i]) = f'(x[i])(x-x[i])

  y = f(x[i]) + f'(x[i])(x-x[i])

  Solve for y=0

# BFS

// Set all vertices to white
// Put starting vertex S on the Queue

S.colour = grey
Q.pushTail(S)
distance=0

while !Q.empty() {
    u = Q.popHead()
    // For each node adjacent to u
    for v = Adj[u]
      if v.colour == white
        v.colour = grey
        v.predecessor = u
        v.distance = distance
        Q.pushTail(v)
    // When all done, mark as black
    u.colour = black;
    distance++
}

# DFS

Set all nodes to white
dfs-visit(u)
  for v in adj[u]
    if v.colour = grey|black // cycle
    else if v.colour = white
      v.colour = grey
      v.parent = u
      dfs-visit(v)
  u.colour = black // topological sort

# Dynamic programming

Recursion + memoization

Fibonacci

fib(i)
{
  if i<0
    return error
  else if i<1
    return i
  else if memo[i] != null
    return memo[i]
  else 
    memo[i] = fib(i-1) + fib(i-2)
    return memo[i]
}

  S --1-> A --2-> B → 4 → C
          | \     |       ↓ 
          1   1   5       2
          |     \ |       ↓
          D --3-> E --1-> F --2-> G

Triangle of inequality?

A   C
  B

A->C <= A->B + B->C

A shortest graph algorithm involves relaxing edges until they can be relaxed
no more.  The key is to find an algorithm that does the reliably does the minimum number of relaxation steps.

A sort of BFS/DFS that favours lower weight paths.

In practice, we use a priority queue to implement.

Dijkstra is a greedy algorithm

for u in G:
  u.colour = black
  u.predecessor = null
  u.distance = 0

Q.append(S)

while Q is not empty:
  u = Q.extract_min()
  for v in adj[u]:
    if u.colour == white:
      # already visited
    if u.colour == grey:
      # already in queue
    if u.colour == black:
      relax(u,v,w)
      Q.append(v)
  u.colour == white

relax(u,v,w):
  if u.distance + w < v.distance:
    v.predecessor = u
    v.distance = u.distance + w 

  S -> v

  S -> a > v

   --3- a -1---c --
  |     |          \
` S     2           2
  |     |            \
   --2- b -5- d - 1 - v


DFS

BFS

for u in G:
  u.colour = black
  u.predecessor = null
  u.distance = 0

Q.pushTail(S)
while Q is not empty:
  u = Q.popHead()
  for v in adj[u]:
    if v.colour == white:
      # already visited
    if v.colour == grey:
      # in the queue but not yet visited
    if v.colour == black:
      # never visited
      v.precedessor = u
      v.distance = u.distance + 1
      v.colour = grey
      Q.pushTail(v)
  u.colour = white

# In BFS we need to set the distance before pushing the node onto the queue.
# In BFS we need to distinuish between three types of nodes:
  1) Never visited
  2) Seen but not yet visited
  3) Visited (i.e. we have traversed all edges leaving this node)

  S

  S -> v

    ->  
  S    v
    -> 

What's the point of BFS?  Erm - visits all nodes?  Avoids cycles?  Does it
turn it into a tree?  Presumably yes because we have a predecessor node?
Shortest paths with equal weights?

   --3- a -1---c --
  |     |          \
` S     2           2
  |     |            \
   --2- b -5- d - 1 - v

  Visited     Q
              [S]

  S           [a,b]
  S,a         [b,c]
  S,a,b       [c,d]
  S,a,b,c     [d,v]
  S,a,b,c,d   [v]

DFS

* Find cycles
* Topological sort

# Initialise all nodes

for u in G:
  u.colour = black
  u.predecessor = null
  u.distance = 0
dfs-visit(S)

function dfs-visit(u)
  u.colour = grey
  for v in adj[u]:
    if v == black:
      # never visited
      v.predecessor = u
      v.distance = u.distance + 1
      dfs-visit(v)
    if v == grey:
      # back edge (already seen)
      # cycle detected
    if v == white:
      # already visited (cross edge?)
  v.colour = white

Test

  S

  S->v

  S -> u -> v

    - a
  S     - v
    - b

  / - a
  S     - v
  ^ - b
  |--/ 

    - a       d
  S     - c -   - v
    - b       e

Initialise
  for u in G:
    u.colour=black
    u.predecessor = null
    u.δ = infinity 

def Relax(u,v,w):
  assert(w >= 0, "Dijkstra does not deal with negative weights")
  if u.δ + w(u,v) < v.δ
    v.δ = u.δ + w(u,v)
    v.predecessor = u

Dijkstra(G,W,S)
  Initialise (G,S)

  S.δ = 0
  Q.append(S)

  while Q:
    u=Q.extract_min
    for each v in adj[u]
      Relax(u,v,w)
      if (u.colour == black)
        u.colour = grey
        Q.append(v)    # queue is ordered by δ ascending
    u.colour = white

  S

  S -1- a

    -2- a
  S       -1- c
    -1- b

    -1- a
  S       -2- c
    -2- b     |
              |
    -3--------|

Tests:
  Boundary
  Error
