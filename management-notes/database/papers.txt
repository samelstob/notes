# Redbook

JSON can be viewed in one of three ways

1. A general purposes hierarchical data format.  

2. A representation for sparse data

3. As a mechanism for schema on read

# What Goes Around Comes Around

Michael Stonebraker
Joey Hellerstein

## Introduction

We present data model proposals in nine historical epochs

1. Hierarchical (IMS): late 60's and 70's
2. Directed graph (CODASYL): 70's
3. Relational: 70's, early 80's
4. Entity-relationship: 70's
5. Extended Relational: 80's
6. Semantic: late 70's and 80's
7. Object-oriented: 80's early 90's
8. Object-relational: 80's and early 90's
9. Semi-structured (XML): late 90's to present

## II IMS

IMS was released around 1968, and initially had a hierarchical data model.

i) Record type is a collection of named fields with their associated data 
types
ii) Each instance of a record type is forced to obey the data description 
indicated in the definition of the record type
iii) Some subset of the named fields must uniquely specify a record instance, 
i.e. they are required to be a key
iv) Record types must be arranged in a tree, such that each record type (other 
than the root) has a unique parent record type.

* Lesson 1: Physical and logical data independence are highly desirable

The ability of a data base application to continue to run, regardless of what 
tuning is performed at the physical level will be called physical data 
independence.

* Lesson 2: Tree structured data models are very restrictive

i) Data may be duplicated: e.g. Supplier->Part - Parts are duplicated for 
every supplier
ii) Every record is forced to have a parent record.  e.g. Part->Supplier - it 
is impossible to have a supplier that suppliers no parts

* Lesson 3: It is a challenge to provide sophisticated logical reorganizations 
  of tree structured data

* Lesson 4: A record-at-a-time user interface force the programmer to do 
  manual query optimization, and this is often hard

## III CODASYL Era

In 1969 the CODASYL (Committee on Data Systems Languages) released their first 
report.  CODASYL was an ad hoc committee that championed a directed graph data 
model along with a record-at-a-time data manipulation language.

This model organised a collection of record types, each with keys, into a 
directed graph rather than a tree.  Hence a given record can have multiple 
parents rather than a single one as in IMS.

The direct graph approach solves many of the problems of the hierarchical data 
model of IMS.  For example it is now possible to have e.g. a supplier that 
supplies no parts.

There are still situations that are hard to model in IMS.  Relationships are 
two-way.  A three-way relationship e.g. bride-groom-minister

The CODASYL proposal provided essentially no physical data independence.  For 
example if the key of a record is changed (and hence the hash storage).  With 
regard to logical data independence, CODASYL proposed the notion of a logical 
data base, which is constrained to be a subset of the record types and set 
types in a physical data base.

* Lesson 5: Directed graphs are more flexible than hierarchies but more 
  complex

The CODASYL proposal trades increased complexity for the possibility of easily 
representing non-hierarchical data.  CODASYL offers poorer logical and physical 
data independence than IMS.

* Lesson 6: Loading and recovering directed graphs is more complex than 
  hierarchies

In CODASYL all the data was typically in one large network which had to be 
bulk-loaded all at once.  If a CODASYL data base became corrupted, it was 
necessary to reload all of it from a dump.

A CODASYL load program tended to be complex because large numbers of records 
had to be assembled into sets, and this usually entailed many disk seeks.  As 
such, it was usually important to think carefully about the load algorithm to 
optimize performance.

## IV Relational Era

Ted Codd proposed his relational model in 1970.  In a conversation with him 
years later, he indicated that the driver for his research was the fact that 
IMS programmers were spending large amounts of time doing maintenance on IMS 
applications, when logical or physical changes occurred.  Hence, he was 
focused on providing better data independence.

His proposal was threefold:

i) Store the data in a simple data structure (tables)
ii) Access it through a high level set-at-a-time DML
iv) No need for a physical storage proposal

The relational model is flexible enough to represent almost anything.  Hence, 
the existence dependencies that plagued IMS can be easily handled e.g. a 
supplier with no parts.  Three way relationships that were difficult in 
CODASYL are easily represented.

Codd made several (increasingly sophisticated) relational model proposals 
over the years.  His early DML proposals were the relational calculus and the 
relational algebra.  His DML proposals were rigorous and formal, but not 
necessary for mere mortals to understand.

Codd's proposal immediately touched off "the great debate" which lasted for a 
good part of the 1970's.

Tedd Codd and followers (mostly researchers and academics):

a) Nothing as complex as CODASYL can possibly be a good idea
b) CODASYL does not provide acceptable data independence
c) Record-at-a-time programming is too hard to optimize
d) CODASYL and IMS are not flexible enough to easily represent common 
situations (e.g marriage ceremonies)

Charlie Bachman and followers (mostly DBMS practitioners):

a) COBOL programmers cannot possibly understand the new-fangled relational 
languages
b) It is impossible to implement the relational model efficiently
c) CODASYL can represent tables, so what's the big deal?

In the next couple of years:

Relational advocates:

a) Relational calculus and algebra are not user friendly - SQL and QUEL are 
more user friendly
b) System R and INGRES proved that efficient implementations of Codd's ideas 
are possible.  Moreover, query optimizers can be built that are competitive 
with all but the best programmers at constructing query plans.
c) 

CODASYL

Dec

IMS and CODASYSL were written for Mainframe systems such as IBM and were part 
of the batch processing era.  e.g. IDMS (CODASYSL) were written in IBM 
assembly and not easily portable.

Mini-computers came along bringing interactive computing.  The early relation 
systems had the VAX market to themselves.  Serious data processing was still 
done on mainframes in IMS or CODASYL.

In 1984 IBM created a relational database DB/2 which used SQL.  IBM's adoption 
of SQL and the relational model was the death of IMS and CODASYL.  Other 
(possibly better) query languages, such as QUEL, were immediately dead.

Note: IBM attempted to provide a relational front end on top of IMS.  
Unfortunately, it proved too hard to implement SQL on top of the IMS notion of 
logical data bases, because of semantic issues.

a) the success of the VAX
b) the non-portability of CODASYL engines
c) the complexity of the IMS logical data bases

* Lesson 7: Set-a-time languages are good, regardless of the data model, since 
  they offer much improved physical data independence.

* Lesson 8: Logical data independence is easier with a simple data model than 
  with a complex one

* Lesson 9: Technical debates are usually settled by the elephants of the 
  marketplace, and often for reasons that have little to do with technology

* Lesson 10: Query optimizers can beat all but the best record-at-a-time DBMS 
  application programmers

## V The Entity-Relationship Era

In the mid 1970's Peter Chen proposed the ER data model as an alternative to 
the relational, CODASYL and hierarchical data models.

The E-R model never gained acceptance as the underlying data model taht is 
implemented by a DBMS.  However, it has been successfully in data base schema 
design.

Chen's papers contained a methodology for constructing an initial E-R diagram.  
in addition, it was straightforward to convert an E-R diagram into a 
collection of tables in third normal form.

* Lesson 11: Functional dependencies are too difficult for mere mortals to 
  understand.  Another reason for KISS

## VI R++ Era

Beginning in the early 1980's a sizable collection of papers appeared:

i) Consider an application, call it X
ii) Try to implement X on a relational DBMS
iii) Show why queries are difficult or why poor performance is observed
iv) Add a new "feature" to the relational model to correct the problem

Many X's were investigated including mechanical CAD, VLSI CAD, text management, 
time and computer graphics.

Gem was one such paper that offered extensions.

The problem with extensions of this sort is that while they allowed easier 
query formulation than was available in the conventional relational model, the 
offered very little performance improvement.

In the early 1980's the relational vendors were singularly focused on 
improving transaction performance and scalability of their systems so that 
they could be used for the large scale business data processing applications.

* Lesson 12: Unless there is a big performance or functionality advantage, new 
  constructs will go nowhere

## VII The Semantic Data Model Era

* Another school of thought suggested the relational data model is 
  "semantically impoverished", i.e. incapable of easily expressing a class of 
  data of interest.  Hence, there is a need for a "post-relational" data 
  model.
* Post-relational data models were typically called semantic data models.
* SDM from Hammer and McLeod is arguably the more elaborate semantic data 
  model.
* "Most semantic data models were very complex, and were generally paper 
  proposals.  Several years after SDM was defined, Univac explored an 
  implementation of Hammer and McLeod's ideas.  However, they quickly 
  discovered that SQL was an intergalactic standard, and their incompatible 
  system was not very successful in the marketplace."
* "In our opinion, SDMs had same problems as R+:"
    - Lot of machinery that was easy to simulate on relational systems
    - Established vendors were focussed on transaction processing performance
* Semantic Data models had little long term influence.

## VIII OO Era

* "Beginning in the mid 1980's there was a "tidal wave" of interest in OODB.  
  Basically, this community pointed to an "impedance mismatch" between 
  relational data bases and languages like `C++` "
* It would seem cleaner to integrate DBMS into a persistent programming 
  language i.e. one where the variables in the language could represent 
  disk-based data as constructs.
    - Several prototype persistent languages were developed in the late 1970's 
      including Pascal-R, Rigel, and a language embedding PL/1.
* "Programming language experts have consistently refused to focus on I/O in 
  general and DBMS functionality in particular."
* mid 80's - resurgence of interest in persistent programming languages: OODB 
  - mainly persistent `C++`.
    - Garden, Exodus, Ontologic, Object Design, Versant
    - General form was support C++ as a data model: any C++ structure could be 
      persisted.  Extend C++ with relationships.
* OODB targets engineering CAD
* Loader would "swizzel" disk-based representation into a memory C++ object.
* Reqs:
    - No query language
    - No transaction management.  This market is largely one-user-at-a-time 
      processing large engineering objects.  Versioning would be nice.
    - Run-time had to competitive with conventional C++ and a customer loader.
* Market was niche.  Most OODB vendors have failed or repositioned.
    - Absence of leverage: avoid writing a load/unload is not a big money 
      feature
    - No standards
    - Relink if anything changed
    - Tied to a single language

## Lesson 13: Packages will not sell to users unless they are in "major pain"

## IX The Object-Relational Era

* GIS doesn't fit relational well
    - B-tree's are one dimensional: awful performance for GIS
    - Simple GIS queries are difficult to express in SQL 
    - Need Quad trees or R-trees
* Need to add custom types, operators, functions, access methods
* UDF - User defined functions
    - Postgres figured out the mechanisms required to support this 
      extensibility

* Stored procedures
    - Sybase pioneered.  Idea to offer high performance on TPC-B by reducing 
      round trips
    - To go fast on standard benchmarks such as TPC-B all vendors implemented 
      stored procedures.
* Postgres UDTs and UDFs allow code to be written in a conventional 
  programming language and be called in the middle of processing conventional 
  SQL queries

Illustra + Informix

a) Inside every OR application, there is a transaction processing 
sub-application.
b) 

* "OR technology is gradually finding market acceptance.  It is more effective 
  to implement data mining algorithms as UDFs: adopted by Redbrick and Oracle.  
  Move processing to the data.  OR technology is also being used to support 
  XML processing"
* Absence of standards.  Most vendors support Java, Microsoft does not.

## Lesson 14: The major benefits of OR is two-fold: putting code in the data 
base (and thereby blurring the distinction between code and data) and a 
general purpose extension mechanism that allows OR DBMS to quickly respond to 
market requirements.

## Lesson 15: Widespread adoption of new technology requires either standards 
and/or an elephant pushing hard.
