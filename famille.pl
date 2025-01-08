% Définir des faits

homme(pierre).
homme(marc).
homme(paul).
homme(jacques).
femme(marie).
femme(sophie).
femme(julie).

parent(julie, sophie).
parent(pierre, paul).
parent(marie, paul).
parent(marc, sophie).
parent(jacques, marc).


% Définir des règles

pere(X, Y) :- homme(X), parent(X, Y).
mere(X, Y) :- femme(X), parent(X, Y).
grandparent(X, Y) :- parent(X, Z), parent(Z, Y).
freresoeur(Y, Z) :- parent(X, Y), parent(X, Z), not(Y=Z).
oncletante(X, Y) :- freresoeur(X, Z), parent(Z, Y).
cousin(X, Y) :- parent(Z, X), freresoeur(Z, W), parent(W, Y).

% Règles de longueur

longueur([], 0).
longueur([_ | Queue], N) :- longueur(Queue, M), N is M + 1.

present([N|_], N).
present([_ | Queue], X) :- present(Queue, X).



