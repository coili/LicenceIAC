/* Colin Senot */


/* Faits */
directementDans(olga, katarina).
directementDans(natasha, olga).
directementDans(irina, natasha).


/* Règles */
dans(X, Y) :- directementDans(X, Y).
dans(X, Z) :- directementDans(X, Y), dans(Y, Z).