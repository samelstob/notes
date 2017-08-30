Hash join two row sources

T1, T2

inner equi-join

Receive rows from T1 and build a hash table on the join key
For each row in T2 probe the hash table for a matching from row from T1
Discard rows that didn't match?

left outer join


