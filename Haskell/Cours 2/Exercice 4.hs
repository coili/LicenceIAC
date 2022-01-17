listeImpaires = [1,3..24]

tete:queue = listeImpaires

nouvelleListeImpaires = queue ++ [tete]

[e1, _, _, e4, _, _, e7, _, _, e10, _, _] = listeImpaires

nouvelleListeElements = [e1, e4, e7, e10]
[_, e2, _, _] = nouvelleListeElements

main = do
    print listeImpaires 
    print nouvelleListeImpaires
    print e2