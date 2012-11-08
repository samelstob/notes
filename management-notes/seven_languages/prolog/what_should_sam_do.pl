/* Prolog */
likes(sam, learning).
likes(sam, challenging).
likes(sam, design).
likes(sam, programming).

task(read_joel, learning).
task(learn_language, learning).
task(learn_language, challenging).
task(learn_language, programming).

sam_likes_task(X, Y) :-
    task(X, Property1), likes(Y, Property1),
    task(X, Property2), likes(Y, Property2),
    task(X, Property3), likes(Y, Property3),
    \+(Property1 = Property2),
    \+(Property1 = Property3),
    \+(Property2 = Property3).


