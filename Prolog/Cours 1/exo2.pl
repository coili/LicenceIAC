/* Faits */
hobbit(bilbon).
hobbit(frodon).
magicien(gandalf).

ami(gandalf, bilbon).
ami(gandalf, legolas).
ami(gandalf, frodon).

aimer(gandalf, 'herbes à pipe').

/* Règles */

aimer(X, 'herbes à pipe') :- hobbit(X).

detester(saroumane, Y) :- aimer(Y, 'herbes à pipe').

ami(X, bilbon) :- ami(gandalf, X).

/* Requêtes */

% 1) hobbit(bilbon) => true
% 2) aimer(bilbon, 'herbes à pipe') => true
% 3) hobbit(X) => Bilbon | Frodon
% 4) ami(X, bilbon) => Gandalf | Bilbon | Legolas | Frodon
% 5) aimer(X, 'herbes à pipe') => Gandalf | Bilbon | Frodon
% 6) detester(saroumane, X) => Gandalf | Bilbon | Frodon