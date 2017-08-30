# The Essence of Linear Algebra

## Vectors

* Physics student
  - Vectors are arrows pointing in space - length and direction
* CS student
  - Vectors are ordered lists of numbers
* Maths student
  - Seeks to generalise both these views.  A vector can be anything where
    there is a sensible notion of adding two vectors and multiplying a vector
by a number

Think about a vector as an arrow with it's tail rooted at the origin

The coordinates of a vector give instructions of how to get from tail to the
tip.  To distinush from points, the convetion is to write these vertically

## Vector addition

Vector addition - think of putting the tail of second vector at the tip of the
first one

if you draw a new vector from the tail of the first one to the tip of the
second one, that new vector is their sum

Each vector represents a certain movvement.

## Scalar multiplication

Stretch out or squish the vector (or reverse the direction)

Whenever you catch a number scaling some vector you call it a "scalar"

Throughout linear algebra one of the main things that numbers do is scale
vectors.  It's common to use the word scalar pretty much interchangably with
"number".

# Linear combinations, span and bases

## Basis vectors

In the x,y coordinate system there are two special vectors

i^ - Unit vector in the x direction
j^ - Unit vector in the y direction

i^ and j^ are the "basis vectors" of the xy coordinate system

Think of the x coordinate of our vector as a scalar that scales i^ and the y
coordinate as a scalar that scales j^

The vector describes the sum of two scaled vectors

What if we chose different basis vectors?

Any time we describe vectors numerically it depends on an implicit choice of
what basis vectors we are using.

Any time that you are scaling two vectors and adding them like this it is
called a linear combination of those two vectors

## Span

The set of all possible vectors you can reach with a linear combination of a
given pair of vectors is called the span of those two vectors
