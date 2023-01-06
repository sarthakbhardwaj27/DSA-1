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

the two main operations supported by Fenwick tree are: 
1. getSum(x) - this operation returns the sum of first "x" elements of the arrya i.e. a[0]+...+a[x]
2. update(x,val) - this operation updates the value of "a" at index "x" i.e. a[x] = val;
3. getSumRange(left,right) - this operation returns the sum of array elements within a rnage [left,right] getSum(x). It can be easily calculated using getSum(x) operation by returning getSum(right+1)-getSum(left)
 we can also find the sum of any arbitraty range [left,right] using the below given function which usees getSum(x) to find the same.       
                                       
--------------------------------------------
HOW DOES FENWICK TREE WORK?

FINDING THE LEAST SIGNIFICANT SET BIT OF “x”

x>0
we can express it in the binary form of “a1b” where a is any arbitrary binary string consisting of both 1s and 0s. and b is a binary string of all 0s because 1 is the last set bit present in the binary representation of x.                                        

for example the binary representation of 20 is 010100, if we write this in the form of “a1b” then “a” will be 010 and “b” will 100
we have studied that in binary form (-x) represented as 2’s compliment of x and 2’s complement of x is equal to x’+1. Now since x = a1b ⇒ x’ = a’0b’. 

Since b had contained all 0’s so b’ will be all 1’s. Adding 1 to a’0b’ will make it a’1b. 

For example, 20 ⇒ (010100)base2 will give a = 010 and b = 00
x’ = (101011)base2
we can clearly see now a1b contains all a =010 and it is of the form b = 00 with x’ = (101011)base2 and b’=11.
-x = x’+1 = (101011)base2  + (1)base2 = (101100)base2
                                       
hence it is of the form a'1b, now if we take "and" of x and -x we will get something of the form (p1q)base2 where p and q are binary strings with all 0's i.e. a number with only one set bit because a&a' = 0 and b are already zero

To remove the least significant set-bit from a'1b we can subtract the result obtained of and from x.
for example: 

x=20 and x&(-x) = 4  ⇒ x - (x&(-x)) = 16 which is the same number that could be obtained by removing the least significant bit of 20.

As discussed in the previous sections we will not be representing the fenwick tree in a “tree like structure” instead we will represent it as an array of size n+1 for any given array of size n to maintain 1-based indexing.
                                       
--------------getSum(x) operation

it returns the sum of arrau elemtns from x index to xth index i.e. a[0]+a[1]+…+a[x]

- inititalize answer, ans to 0
- increase x by 1 (to maintain 1-based indexing)
- while x is greater than 0
    ans+=bit[x]
    x-=(x&(-x))                                       

---------------update(x,val) operation

it updates the value of array x = 20 at index x&(-x)=4 to ⇒ after updating , we also need to update 20 array at those indeixes which get impacted by the element at index x, steps are:                                       
- Find the change happening at the index x, δval=val−a[x].
- Update the value at index x i.e. a[x]=val.
- While x≤n
    - bit[x]+=δval
    - x+=(x&(-x))                                       
                                       
                                       
                                       
