/* Faits */
pays(france).
pays(allemagne).
pays(espagne).
pays(italie).
pays(protugal).

pays(algerie).
pays(maroc).

ville(paris).
ville(berlin).
ville(munich).
ville(lisbonne).

capitale(paris, france).
capitale(berlin, allemagne).


/* Règles */

europe(france) :- pays(france).
europe(allemagne) :- pays(allemagne).
europe(espagne) :- pays(espagne).
europe(italie) :- pays(italie).
europe(portugal) :- pays(portugal).

europe(paris, france) :- capitale(paris, france).
europe(berlin, allemagne) :- capitale(berlin, allemagne).
europe(munich, allemagne) :- ville(munich), europe(allemagne).
europe(lisbonne, portugal) :- ville(lisbonne), europe(portugal).

afrique(algerie) :- pays(algerie).
afrique(maroc) :- pays(maroc).


/* Requêtes */

% 1) europe(france). => true
% 2) afrique(munich). => false
% 3) europe(X, Y). => Paris, France | Berlin, Allemagne | Munich, Allemagne | Lisbonne, Portugal
%    afrique(X) => Algérie | Maroc
% 4) europe(X) -> afrique(X) -> europe(X, Y) -> afrique(X, Y) -> afrique(X, Y)
% 5) europe(espagne) => true | afrique(algerie) => true
% 6) capitale(X, france) => paris | capitale(X, espagne) => false | ville(madrid) => false | europe(madrid, Y) => false | europe(X, Y), capitale(X, Y) => Paris | Berlin


