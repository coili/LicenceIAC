/* Colin Senot */


/* Faits */
trainDirect(sarrebruck, dudweiler).
trainDirect(forbach, sarrebruck).
trainDirect(freyming, forbach).
trainDirect(stAvold, freyming).
trainDirect(faulquemont, stAvold).
trainDirect(metz, faulquemont).
trainDirect(nancy, metz).

/* Règles */
voyageDe_A(X, Y) :- trainDirect(X, Y) ; trainDirect(Y, X).
voyageDe_A(X, Z) :- trainDirect(X, Y), voyageDe_A(Y, Z). 