/* Prolog */

/* Facts */
child_of(harry, sam).
child_of(harry, sarah).
child_of(harry, tom).
child_of(peter, harry).
child_of(sam, steven).

/* Rules */
is_child_of(Who, Child) :- child_of(Who, Child).
is_decendent_of(peter, steven).
is_decendent_of(Who, Decendent) :- child_of(Who, Decendent).
is_decendent_of(Who, Decendent) :- child_of(Who, IntermediateDecendent), is_decendent_of(IntermediateDecendent, Decendent).
is_decendent_of(Who, Decendent) :- child_of(Who, IntermediateDecendent), child_of(IntermediateDecendent, IntermediateDecendentTwo), is_decendent_of(IntermediateDecendentTwo, Decendent).

