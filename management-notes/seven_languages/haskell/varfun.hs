circleArea r = pi * r^2

squareArea a = a^2

abs x
    | x < 0     = 0 - x
    | otherwise = x

cubeVolume a b c = a * b * c

cylinderVolume r h = (circleArea r) * h

triangleArea a b c = let s = (a+b+c)/2 in
     sqrt (s*(s-a)*(s-b)*(s-c))

areaRightTriangle b h = (b * h) / 2

readLineWithMessage :: String -> IO String
readLineWithMessage message = do
    putStrLn message 
    getLine

main = do
    base <- readLineWithMessage "The base?"
    height <- readLineWithMessage "The height?"
    putStrLn ("The area of that triangle is " ++ (show (areaRightTriangle (read base) (read height))))

