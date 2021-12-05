/* Colin Senot */

/* 

PARTIE 1 : 

    Explications :

    On passe en paramètre deux élements : X et la liste.
    X est le deuxième élement de la liste s'il correspond à la queue de la liste ET s'il correspond à la tête de la queue*

    * La queue d'une liste est également une liste

    Exemple : 
    X = b
    Liste = [a, b, c, d, e, f]

    deuxieme(b, Liste) = true car b est le premier élément de la queue de la liste "Liste"

 */
deuxieme(X, Liste) :- Liste = [_|Queue], Queue = [X|_]. 


/* 

PARTIE 2 : 

    Explications :

    On vérifie que la tête de la liste1 correspond au deuxième élément de la liste2, et inversement. 
    On vérifie également que le reste est bien identique.

    Exemple : 
    Liste1 = [a,b,c,d]
    Liste2 = [b,a,c,d]

    reflet12(Liste1, Liste2) = true car a est la tête de Liste1 et le deuxième élement de Liste2, (même raisonnement avec b pour 
    Liste2) et le reste de Liste1, à savoir [c,d] est identique à celui de Liste2, à savoir [c,d].

 */

reflet12(Liste1, Liste2) :- Liste1 = [T1|Queue1], Liste2 = [T2|Queue2], Queue1 = [T2|Q], Queue2 = [T1|Q].


/* 

PARTIE 3 : 

    Je n'ai pas réussi cette partie. Ce que j'ai écris est une piste de réflexion. Je cherche à utiliser la récursivité : pour 
    chaque élément de la liste, on détermine sa traduction.

 */  

trad(ein, un).
trad(zwei, deux).
trad(drei, trois).
trad(vier, quatre).
trad(fuenf, cinq).
trad(sechs, six).
trad(sieben, sept).
trad(acht, huit).
trad(neun, neuf).
  
 
elementTrad(Element, X) :- trad(Element, X).  
listeDTrad(ListeA, X) :- ListeA = [T|Q], elementTrad(T, X), listeDTrad(Q, Y).
  