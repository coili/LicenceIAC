/* Faits */
mot(astante, a,s,t,a,n,t,e).
mot(astoria, a,s,t,o,r,i,a).
mot(baratto, b,a,r,a,t,t,o).
mot(cobalto, c,o,b,a,l,t,o).
mot(pistola, p,i,s,t,o,l,a).
mot(statale, s,t,a,t,a,l,e).

/* Règles */
motscroises(A, B, C, D, E, F) :- 
    mot(V1, _,L1,_,L2,_,L3,_), 
    mot(V2, _,L4,_,L5,_,L6,_), 
    mot(V3, _,L7,_,L8,_,L9,_), 

    mot(H1, _,L1,_,L4,_,L7,_), 
    mot(H2, _,L2,_,L5,_,L8,_), 
    mot(H3, _,L3,_,L6,_,L9,_), 
    
    write("== Résultat =="), nl,
    write(V1), nl,
    write(V2), nl, 
    write(V3), nl,
    write(H1), nl, 
    write(H2), nl, 
    write(H3), nl.


/* Requêtes */

% 1) motscroises(A, B, C, D, E, F).


