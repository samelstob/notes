# Problem solving

* Listen
  - Key information in the question e.g. sorted, is it to run be run
    repeatadly
* Examples
  - Try some examples to check you understand the problem 
  - Make sure the examples are not simple
* Brute force
* Optimise
  * Use intuition - try manually
  * BUD
    - Bottlenecks
    - Unnecesary work
    - Duplicate work
  * simplify and generalise
  * divide and conquer - base case and recursion
  * 
  * Data structure brainstorm
  * Best Conceivable Runtime
* Walk through
* Test
* Implement
  - Well factored

# Linux and C

* fork - create new process
* wait - wait for signal
* signal - handle signal
* files
  - descriptor = open(path, mode)
  - descriptor dup(existing_descriptotr)
  - close(descriptor)
  - unlink(path)
  - link(path, path)
  - dir = opendir(path)
  - dir_ent = readdir(dir)
  - write(descriptor, buf, len)
  - read(descriptor, buf, len)
  - error = lseek(descriptor, pos)
  - errno
  - stat(path, stat)
* buffered
  - fopen, fgets, fread
  - fprintf
* exit
* strerror
* network
  - socket
  - accept
  - bind
  - listen 
* system
* pthread_create
* pthread_lock
