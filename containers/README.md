# Containers

## hash tables

h(key) = int

![hashmap](hashmap.png)

A good hash function h(key) = int needs the following properties:
* It should be deterministic—equal keys must produce the same hash value.
* efficient to evaluate
* uniformly distributed 

**types of hash functions**
 * ***Positive integers*** (known as modular hashing): h : key % M -> int.
 * ***Floating-point***: do modular hashing on the binary representation of the key.
 * ***String***: sum modular hash of each char element.
 
 ### collisions
 
 * Seperate Chaining
 * Open Addressing
 
    h_i(x) = (Hash(x) + F(i)) % M
    keep trying i = 1....M until a spot is found.
 
    F(i) = i: linear probing
    
    F(i) = i^2: quadratic probing
    
    F(i) = i * Hash_2(x) : double hashing

**which method is better to handle collisions**:

Open Addressing: better cache performance (better memory usage, no pointers needed)

Chaining: less sensitive to hash functions (OA requires extra care to avoid clustering)
and the load factor α (OA degrades past 70% or so and in any event cannot support values larger than 1)

### references

[cs princeton](https://algs4.cs.princeton.edu/34hash/)
[open addressing](https://www.cse.cuhk.edu.hk/irwin.king/_media/teaching/csc2100b/tu6.pdf)
