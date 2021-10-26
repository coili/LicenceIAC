/* Faits */
membre(X, [X|Liste]).
membre(X, [H|Liste]) :- membre(X, Liste).
deuxieme(X, [H|Liste]). 