# Oracle SecureFiles: Prepared for the Digital Deluge

* vldb 2009

* Filesystems have generall been preferred for large objects
* Filesystems don't have database features like transactional atomicity, consistency, durability, queriability
* Studies from 2005, 2006 suggested 256kB has the break even point for moving
  to a filesystem
* Primary focus of paper is on scalability on I/O bound filesystem like
  operations
* 2008 secure files paper
* A SecureFiles object uses CoW semantics i.e. Updates and overwrites are never in place
* Write Gather Cache (WGC)
  - Server processes allocate buffer from process private memory pools (sounds
    like PGA)
  - WGC Buffer writes
  - Write performance throughputs scale up with the number of server processes
  running concurrently - Yes I think we see that with JLL
* Compression 
  - Compression automatically turned off for objects that don't compress well
* De-dupe
    the entire object
  - Hashes are stored in an Oracle index
  - Byte-by-byte comparison if hashes match
* Free Space Management
  - Responsible for scalability during data manipulation operations
* Background Free Space Monitor
  - Responsible for managing space usage in secure file segments
  - Monitors fragmentation and free space caused by manipulations and CoW
  - Non blocking
* In-memory Space Dispenser
  - Memory version of free space populated from above
* Uncommitted free space blocks
  - CoW semantics result in de-allocation of space previously occupied
* ASM
  - Data Retrieval Scalability 
* Scalability Data Retrieval
  - Consistent Read (CR) is used
  - Each processes reads a transactionally consisent copy of the inode
    metadata
  - Space management supports variable sized chunks therefore metadata can map
    terabyte sized objects efficiently 
  - Intelligent pre-fetching is used for reads to overlap network RTT and disk
    I/O
* Performance evalluation
  - Each LUN (146GB 15k) has max throughput of 50MB/s for 1MB writes and
    60MB/s for 1MB reads
  - Email workload 5-14kB
  - Document workload 80-110
  - Low res images - 900 1.2MB
  - Hi res - 8.5 - 11.3
  - Video 97MB
  * Email workload
    - write 54MB/s, read 93MB/s  - CPU bound
  * Document workload
    - write 332MB/s, read 443 MB/s - CPU bound
  * Low res
    - write 686 MB/s, reads 711 MB/s  = bcoming I/O bound
  * Hi res
    - 728MB/s - I/O bound
  * Video
    - 716 write 714 read
* Future - evaluate on Exadata
* References
  - Greetings from a filesystem user
  - To BLOB or not to BLOB
  - The problem with unstructured data
  - Oracle SecureFiles system
  - :w
* Thoughts
  - We don't make use of transactional capabilities of SecureFiles
  - Small files (5-14 kB) performance was not great - hopefully extended data
    types will be better
  - Ingest performance of large files looks good
  - Concurrency of ingest looks good - this is consistent with our experience
  - Not sure how temporary LOBs are handled
  - Lots of SF complexity is about ACID and modifications e.g. CoW, CR, space management
  - We don't actually make modifications

insert first
  table 1 blah
  table 2 blah

* Oracle SecureFIles System
  - Mukherjee, Aleti
  - vldb 200

* Most journalling FS do not provide the recovry that one might expect from
  them
* MSSQL and DB2 provide support for LOBs
* LOBs are ANSI SQL data types BLOB, CLOB, NCLOB
* Main disadvantage of LOBs has been the inability to provide filesystem-like
  performance in both throughput and scalability
* Jim Gray et al. concluded files < 256kB were handled efficiently by SQL
  Server while NTFS > 1MB
* LIBTP - transactional support functions for UNIX filesystems
* BFILE - many limitations, slower than accessing file directly
* GFS, BigTable, ZFS - not much discussion
* SecureFiles
  - 100% backwrad compatab with LOB APIs
  - Delta updates - 
  - Flashback archive
* Stonebraker "Implementation of a specialised solution - 10X gain"
* SecureFiles Object
  - Collection of variable sized chunks
  - Each chunk is a set of contiguous database blocks
  - One or more columns hold locators providing reference pointers to the
    associated SecureFile objects (to the first block of an object)
  - Alongside the locator is stored metadata e.g. length, compressed,
    encrypted, de-deuped.  Also stores the starting block address and lengths
of the first few chunks for the underlying data if sufficiently small
  -  
* Space
  - Each columns shares a pool of free space.  Space is not shared across
    columns to prevent complexity
  - Free space is a SecureFiles segment
  - Logically a SF segment consists of blocks that contain metadata for space
    management and blocks that are part of SF objects
  - The first block may contain addresses and lengths of chunks if this
    metadata cannot fit in the table row/column
  -  
* Architecture
  - Six major components
  - Delta UPdate
  - Write Gather Cache
  - Transformation Management
  - Inode Management
  - Space Management
  - I/O Management
* Delta Update
  - To allow many small changes to the content to be efficiently written.
    Used for XMLDB updates
* Write Gather Cache (WGC)
  - Buffer data before writing
* Transformation Management
  - Compression, encryption, de-dupe
  - Compression is performed when bufferred contiguous data exceeds a
    configured boudnary threshold
  - Compression is performed piecewise such that efficient random access of
    large files is possible
* Inode Management
  - Inode managemenet layer is responsible for initiating on-disk storage and
    access operations on SecureFile object buffers being communicated by the
upper layers in the SF architecture
  - Requests free space from the Space Managment Layer
  - Inode Manager stores metadata either in row or the most current header of
    the SF object
  - Metadata includes start block address and length of a chunk as well as
    start and end offsets of the object being mapped by the chunk
  - Metadata structures are transactionally managed
  - Metadata can remain extremely compact as free space is returned in
    variable sized chunks up to 64M each.  Can map terabyte sized objects very
efficiently
    - 64M = 2^26   1T = 2^40
    - 2^14 64M "chunks" = 16k
* I/O Management
  - Either copies WGC buffers to buffer cache or schedules async writes
    (direct I/O)
  - Tries to further coalesce writes
  - Transactions do not commit until async I/O is complete
  - Keeps track of access patterns and issues intelligent pre-fetching  
* Transaction Atomicity
  - CoW for larger updates and overwrites
  - Small updates generate undo records 
  - When a transaction aborts metadata and space managemetn metadata roll back
    using undo records.  As a result SecureFile object locators point to the
previous image
  - Seems to say that nocache lobs do not need to log, but cache lobs do 
* FLash
  - CoW fits well with flash
  

