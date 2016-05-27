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

Ted Codd and followers (mostly researchers and academics):

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

* Lesson 13: Packages will not sell to users unless they are in "major pain"

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

* Lesson 14: The major benefits of OR is two-fold: putting code in the data
  base (and thereby blurring the distinction between code and data) and a
  general purpose extension mechanism that allows OR DBMS to quickly respond to
  market requirements.

* Lesson 15: Widespread adoption of new technology requires either standards
  and/or an elephant pushing hard.

## X Semi-Structured Data

### 10.1 Schema Later

* Schema Later
  * Really schema later
  * Easy schema evolution: A schema exists in advance, but it should be
    trivial to evolve the schema as the meaning of the data changes.
* Really schema Later
  - Without a self-describing format, a record is merely "a bucket of bits"

* Semantic heterogeneity: where information on a common object does not
  conform to a common representation
  - No structure on which to base indexing decisions and query execution
    strategies

* "We present the following scheme that classifies applications into four
  buckets"
  i) Ones with rigidly structured data
  ii) Ones with rigidly structured data with some text fields
  iii) Ones with semi structured data
  iv) Ones with text

i) Essentially all data on which business processes must operate e.g. payroll
data base
ii) e.g. Personnel data
iii) e.g. entered as text, then parsed to find information of interest
iv) Pure text, IR (schema not at all)

* "Schema-later proposals deal only with the third class of data in our
  classification system"

  - Arguable since this was written, system and application logs are the
    killer use case for schema later (although many logs fit into i) or ii)

* "Semantic heterogeneity has been with enterprises for a very long time.
  They  spend vast sums on warehouse projects to design standard schemas and
then convert operational data to this standard."

## 10.1.2 Schema Evolution

* "Current relational data bases have fairly primitive and rigid facilities for
  schema evolution." e.g. ALTER TABLE.  Oracle has online redefinition but
I've never investigated this.

* It would be nice if ALTER TABLE style schema changes was a background
  operation (or was not needed i.e. new data uses new schema)

* Data lineage in e.g. scientific data base community.  Interesting that
  Pachyderm File System deals with this to some degree (a decade later it is
still an unsolved problem).

## 10.2 XML Data Model

* "DTDs and XML Schema were intended to deal with the structure of formatted
  documents (and hence the word "document" in DTDs).  As a result they look
like a markup lagnuage, in particular a subset of SGML... As a document
specification system, we have no quarrel with these standards... As a data
model for structured ddata we believe both stadards are seriously flawed."

* "To a first approximation, these standards have everything that was ever
  specified in any previous data model proposal.  In addition, they contain
additional features that are complex enough, taht nobody in the DBMS community
has ever seriously proposed them in a data model."

1) XML records can be hierarchical, as in IMS
2) XML reccords can have "links" (references to) other records, as in
CODASYL, GEM and SDM
3) XML records can have set-based attributes, as in SDM
4) XML records can inherit from other records in several ways, as in SDM

"XMLSchema has several features which are well known in the DBMS community but
never attempted in previous data models because of complexity.  One xample is
*union types*, that is, an attribute in a record can be of one of a set of
possible types."

* SE: What happened to XMLSchema?

## 10.3 Summary

* XML will be a popular "on the wire" format for data movement across a
  network: XML goes through firewalls, and other formats do not
  * Since there is always a firewall between the machines of any two
    enterprises, it follows that cross-enterprise data movement will use XML.
* "RPCs that go through firewalls are much more useful than ones that don't.
  Hence, SOAP will dominate other RPC proposals"
* "It is possible that native XML DBMSs will become popular, but we doubt it.
  We expect native XML DBMSs to be a niche market."
* "Consider now XQuery.  A (sane) subset is readily mappable to the OR SQL
  systems of several of the vendors."
* "XML is sometimes marketed as the solution to the semantic heterogeneity
  problem.  Nothing could be further from the truth.  Just because two people
tag a data element as a salary does not mean that the two data elements are
comparable.  One could be salary after taxes in French Francs including a
lunch allowance, while the other could be salary before taxes in US dollar.
Furthermore, if you call them "rubber gloves" and I call them "latex hand
protectors" then XML will be useless in deciding that they are the same
concept.  Hence, the role of XML will be limited to providing the vocabulary
in which common schemas can be constructed"
* "We believe that cross-enterprise data sharing using common schemas will be
  slow in coming, because semantic heterogeneity issues are so difficult to
resolve. We believe that cross-enterprise information sharing willbe limited
to:

1. Enterprises that have high economic value in co-operating.  After all, the
   airlines have been sharing data across disparate reservation systems for
years.

2. Applications that are semantically simple (such as e-mail) where the main
   data type is text and there are no complex semantic mappings involved.

3. Applications where there is an "elephant".  Enterprises like WalMart and
   Dell have little difficulty in sharing data with their suppliers.  They
simply say "if you want to sell to me; here is how you will interact with my
information systems"

"We claim that technological advances keep changing the rules.  For example,
it is clear that the micro-sensor technology coming to the market in the next
few years will have a huge impact on system software, and we expect DBMSs and
their itnerfaces to be affected in some (yet to be figured out) way."

"In such an ever changing world, it is crucial that a DBMS be very adaptable,
so it can deal with whatever the next "big ting" is.  OR DBMSs have that
characteristic; native XML DBMSs do not."

* Lesson 16: Schema-later is probably a niche market

* Lesson 17: XQuery is pretty much OR SQL with a different sysntax

* Lesson 18: XML will not solve the semantic heterogeneity either inside or
  outside the enterprise

## XI Full Circle

* "If native XML DBMSs gain traction, then customers will have problems with
  logical data independence and complexity"

* "We see few new data model ideas.  
