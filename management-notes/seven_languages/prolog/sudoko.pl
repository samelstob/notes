/* Prolog */
/*
valid_row(1, 2, 3).
valid_row(1, 3, 2).
valid_row(3, 1, 2).
valid_row(3, 2, 1).
valid_row(2, 1, 3).
valid_row(2, 3, 1).
*/
valid_row(A, B, C) :- valid_list([A, B, C]).
valid_list(A) :- fd_domain(A, 1, 3), fd_all_different(A).

valid_column(A, B, C) :- valid_row(A, B, C).

valid_diagonal(A, B, C) :- valid_row(A, B, C).
/*
A B C 1 2 3
D E F 2 3 1
G H I 3 1 2
*/
sudoko([A,B,C],[D,E,F],[G,H,I]) :-
valid_row(A, B, C),
valid_row(D, E, F),
valid_row(G, H, I),
valid_column(A, D, G),
valid_column(B, E, H),
valid_column(C, F, I),
valid_diagonal(A, E, I).
/*valid_diagonal(G, E, C).*/
