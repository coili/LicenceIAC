f :: (Ord a) => a -> a -> Bool
f x y = x > y

main = do
    print $ f 5 10
    print $ f 10 5
    print $ f 128.0 2.0
    print $ f 2 1.04
