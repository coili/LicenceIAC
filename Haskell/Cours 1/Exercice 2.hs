c = 78

f1 x = a*x*x + b*x + c 
    where a = 6
          b = 42

f2 x = let a = 6 
           b = 42
         in a*x*x + b*x + c   

x1 = f1 53
x2 = f2 53

main = do
    print x1
    print x2