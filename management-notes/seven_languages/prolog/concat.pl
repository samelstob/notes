/* Concat an empty list to anything does nothing */
concat([], [], []).
concat(A, [], A).
concat([], A, A).
/*
  A = [1]
  B = [2,3]
  C = [1,2,3]

  C is the concat of A and B if the head of A and C are the same and B is the
  tail of C and A was a list of one
*/
concat([Ahead|Atail], B, [Ahead|B]) :- concat([Ahead|[]], B, [Ahead|B]). 
concat([Ahead|Atail], B, [Ahead|B]) :- concat(Atail, B, [Ahead|B]). 
