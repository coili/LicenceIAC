/* Faits */
mot(determinant, un).
mot(determinant, chaque).
mot(nom, criminel).
mot(nom, 'grande frite').
mot(verbe, mange).
mot(verbe, aime).

/* Règles */
phrase(A, B, C, D, E) :- mot(determinant, A), mot(nom, B), mot(verbe, C), mot(determinant, D), mot(nom, E).

/* Requêtes */

% 1) phrase(A, B, C, D, E).
% 2) phrase(A, B, mange, D, E), C=mange. 