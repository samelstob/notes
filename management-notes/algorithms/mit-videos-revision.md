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


