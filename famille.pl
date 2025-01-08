% Définir des faits

homme(pierre).
homme(marc).
homme(paul).
homme(jacques).
femme(marie).
femme(sophie).


parent(pierre, paul).
parent(marie, paul).
parent(marc, sophie).
parent(jacques, marc).

% Définir des règles

pere(X, Y) :- homme(X), parent(X, Y).
mere(X, Y) :- femme(X), parent(X, Y).
grandparent(X, Y) :- parent(X, Z), parent(Z, Y).
freresoeur(Y, Z) :- parent(X, Y), parent(X, Z), Y \= Z.

% Règles de longueur

longueur([], 0).
longueur([_ | Queue], N) :- longueur(Queue, M), N is M + 1.

present([_ | Queue], X) :- present(Queue, X).

