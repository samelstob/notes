module Main where
    data Suit = Heart | Spade | Club | Diamond deriving (Show)
    data Rank = Ten | Jack | Queen | King | Ace deriving (Show)
    type Card = (Suit, Rank)
    type Hand = [Card]

    factorial :: Integer -> Integer
    factorial 0 = 1
    factorial x = x * factorial (x - 1)

    myreverse :: [char] -> [char]
    myreverse [] = []
    myreverse (head:tail) = myreverse(tail) ++ [head]

    value :: Rank -> Int
    value Ten = 10
    value Jack = 10
    value Queen = 11
    value King = 12
    value Ace = 13

    sortpair :: [Integer] -> [Integer]
    sortpair [] = []
    sortpair [a] = [a]
    sortpair [a, b]
        | a > b = [b, a]
        | otherwise = [a, b]

    merge [] [] = []
    merge [a] [] = [a]
    merge [] [b] = [b]
    merge [a] [b]
        | a > b = [b, a]
        | otherwise = [a, b]
    merge [a:b] [c:d] = concat [1,2]

-- merge sort
-- 7,2,4,1,3,5,2,4
-- 2,7,1,4,3,5,2,4
-- 1,2,4,7,2,3,4,5
-- 1,2,2,3,4,5,7
-- 
-- 1. Cut list in half
-- 2. If list is two elements then sort
-- 3. else 1. 
-- Once both sides are sorted, merge them
--
-- 2,4 -> 2,4
-- 1,3 -> 1,3
-- 1,2,3,4
--
-- heap sort
-- something about binary tree
--
-- quick sort?
