f 0 = 1
f 1 = 2
f 2 = 4
f 3 = 9
f 4 = 16

fcarre x = x*x

fdeuxdeux x = 2*x + 2

monerp x = reverse $ prenom x

prenom "Curry" = "Haskell"
prenom "Newton" = "Isaac"
prenom "Curie" = "Marie"
prenom "Turing" = "Alan"
prenom "Tesla" = "Nikola"
prenom "Einstein" = "Albert"
prenom "Kepler" = "Johannes"

n = f 4
m = prenom "Kepler"

o = fcarre 5
p = fdeuxdeux 4

q = monerp "Turing"

main = do
  print n
  print m
  print o
  print p
  print q