# The Essence of Linear Algebra

# 1. Vectors

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
tip.  To distinguish from points, the convention is to write these vertically

## Vector addition

Vector addition - think of putting the tail of second vector at the tip of the
first one

if you draw a new vector from the tail of the first one to the tip of the
second one, that new vector is their sum

Each vector represents a certain movement.

## Scalar multiplication

Stretch out or squish the vector (or reverse the direction)

Whenever you catch a number scaling some vector you call it a "scalar"

Throughout linear algebra one of the main things that numbers do is scale
vectors.  It's common to use the word scalar pretty much interchangeably with
"number".

# 2. Linear combinations, span and bases

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

The span of most pairs of 2D vectors is all vectors of 2D space but when they
line up their span is all vectors who's tip sit on a certain line

### Vectors vs. Points

It's gets really crowded to think about collections of vectors

If you're thinking about a vector on it's own think about an arrow

If you're dealing with a collection of vectors it's convenient to think of
them all as points

### Span of 3D vectors

The span of a linear combination of two 3D vectors is a plan through the
origin

The span of a linear combination of three 3D vectors is all space (unless one
or more vectors line up or one is sitting on the span of the other two)

### Linearly dependent

When at least one of these vectors is redundant - not adding anything to the
span - whenever you have multiple vectors and you could remove one without reducing
the span they are said to be *linearly dependent*; One of the vectors can be expressed as a linear combination of the others

### Linearly independent

If each vector really does add another dimension to the span they are said to
be *linearly independent*

# 3. Matrices as Linear transformations

The word "transformation" suggests that you think using movement

* Lines remain lines - parallel and evenly spaced
* Origin remains in place

We only need to understand how the basis vectors are transformed (i^, j^) -
then everything else falls into place

A 2 dimensional linear transformation is defined by a 2x2 matrix

  ac place where first basis vector lands
  bd place where second basis vector lands

          a b
          c d
