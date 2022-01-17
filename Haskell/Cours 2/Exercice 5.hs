f :: (Ord a) => a -> a -> Bool
f x y = x > y

main = do
    print $ f 1 2
    print $ f 1 1
    print $ f 2 1
    print $ f 1.0 2.0
    print $ f 2.0 1