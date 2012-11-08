/* Prolog */
count(0, []).
count(1, [_]).
count(Count, [_|Tail]) :- count(TailCount, Tail), Count is TailCount + 1.

sum(0, []).
sum(Sum, [Sum]).
sum(Sum, [Head|Tail]) :- sum(TailSum, Tail), Sum is TailSum + Head.

factorial(0, 1).
factorial(N, Factorial) :- M is N - 1, factorial(M, TailFactorial), Factorial is N * TailFactorial.

