LINK: https://www.scaler.com/topics/data-structures/fenwick-tree/

when answering to multiple prefix sum (sum of array elements from 0 to an index x ie. a[0]+a[1]+...+a[x] queries of an aaray, the first idea that comes to our mind is to use a prefix_sum array

a = 3,1,5,-1,8,2
prefix_sum = 3,4,9,8,16,18

if we wish to find the sum of a segment then we can do prefix_sum[x]-prefix_sum[y]
and we can answer such queries in constant time, but if we also need to update array lements frequently then, using prefix_sum array would be of now use because in case of updation we may need to reconstruct the whole prefix_sum array.

In such cases, BINARY INDEXED TREE comes into the picture, popularly called Fenwick trree in DSA. 
It maintains the cumulative frequencies of the array elements at each of its nodes.

one of the best and simple use cases can be calculating the prefix sum of an array in which values are mutable (i.e. values can be changed) logatihmic time complexity

--------------------------
BASIC IDEA OF FENWICK TREE

If we want to calculate prefix_sum of a array "a" of size "n", then we will need another of array of the same size "n"

The basic idea behind "binary indexed tree" is that we can store the sum of a particular range of elements at an index of the newly formed bit array. Which will be used later to calculate prefix_sum in the fewer number of steps.

The idea that "every integer can be represented as the sum of powers of 2" is used extensivelt in the formation of the fenwick tree. Using thie fact we can calcualte the prefix_sum of an array in logairthmic time complexity

-----------------------------
REPRESENTATION OF FENWICK TREE

The "binary indexed tree" a.k.a BIT, is represented as an array (say "bit"). Where each idnex of bit stores the sum of a range of elements of the original array say "a". 

Let i be an index of the array "bit", then bit[i] will contain the sum of elements within math mode where x is the position of the LSB i.e. least significant bit in the binary representation of i

For example:
Let us say we want to tknwo the range of which sum is stored in bit[12], we know that binary represntation of 12 is 1100, we can see that the position of LSB from right, x is 3.
That means bit[12] wo;; contain the sum of the range 12 1100x

-----------------------------------------
OPERATIONS OF FENWICK TREE
