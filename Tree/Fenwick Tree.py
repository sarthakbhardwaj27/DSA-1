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
------------------------------------------                                       
 WHEN TO USE FENWICK TREE?

they are mostly used when we have been given an aray “a” and we need to answer multiple getSum queries i.e. finding the sum of first x elements many times or/and we need to find the sum of a range of elements many times, and also we need to perform multiple update operations i.e. updating the value of “a” at any particular index x
--------------------------------------------
CONSTRUCT OF FENWICK TREE

array “a”, size “n”

create another aaray of size n+1 say “bit” inititate with “0”. Then we will use the update function for each index of array “a”,

--------------pseudocode

buildBIT(a[], n){
    bit=new int[n+1]
    For i=0 to n:
        bit[i]=0
    For i=0 to n:
        update(i, a[i])
}


let a = 4,2,1,5,6,3,9,7,2,3

bit = 4,6,1,12,6,9,9,37,2,5

where bit[i] represents sum of range (i-2^(x-1)+1)→i
---------------------------------------
IMPLEMENTATION

To implement the **Fenwick tree (BIT)** we will have the following global variables to maintain simplicity in the code.

- **n-** It denotes the size of the array on which we want to perform certain operations which are discussed in the previous sections.
- **bit-** It is the actual binary indexed tree that is represented in array format. Its size will be n+1 to maintain 1-based indexing.

The functions which are needed to implement functionalities of the binary indexed trees are :

- **FindSum-** It takes one argument (say ind) and we need to return the sum of values of the given array (say a) in the range [0, ind].
- **SumOfRange-** It takes two arguments (say left and right) and we will return the sum of values of a in the range [left, right]
- **Update-** It takes two arguments (sat ind and val) and we need to change the value of a at index ind to val and correspondingly we also need to update the bit.                                      
        
-------------------------------------------   
PSEUDOCODE
                                      
// n denotes the size of 'a' and bit represents 
// array implementation of Fenwick tree.
n, a[], bit[]

function FindSum ( ind ):
    // Initializing sum as 0.
    sum = 0
    
    // Iterate while the index
    // is in the range of array.
    While( ind > 0):
        // Increase the sum.
        sum += bit[ind]
        // Updating the index.
        ind -= (ind&(-ind))
    
    Return sum
    
end function

function SumRange ( left, right ):

    // Returning sum of the range 
    // [0, right] - [0, left-1].
    // Passing right+1 and left because of 
    // 1 based indexing.
    
    Return FindSum (right + 1) - FindSum (left)
    
end function

function Update ( ind, val ):

    // Calculating 'delta' that is the change
    // in value.
    delta = val - a[ind]
    a[ind] = val
    
    // Increasing the index by 1 
    // to maintain 1 based indexing.
    ind = ind + 1
    
    // Iterating till index is 
    // in the range of the array.
    While ( ind <= n ):
        // Adding delta to bit[ind].
        bit[ind] += delta
        // Updating the index.
        ind += (ind&(-ind))
    
end function        
-------------------------------------------------------------------------                                       
fENWICK IMPLEMENTATION USING C/C++                                       
                                       
// C++ program to implement
// Binary Indexed Tree (Fenwick Tree)
#include<bits/stdc++.h>
using namespace std;

// BIT array - It stores the prefix
// sum of the array. 
int *bit;
int n;

// Utility function to update the 
// bit array.
void updateUtil(int ind, int delta){
    // Increasing the index by 1 
    // to maintain 1 based indexing.
    ind++;
    // Iterating till index is 
    // in the range of the array.
    while(ind<=n){
        
        // Adding delta to bit[ind].
        bit[ind]+=delta;
        // Updating the index.
        ind+=(ind&-ind);
    }
}

// Function to build the 
// BIT array initially.
void buildBIT(int *a, int n){
    // Declaring of size n+1 becuase, 
    // It uses 1 based indexing. 
    bit=new int[n+1];
    for(int i=0;i<=n;i++)
        bit[i]=0;
    // Calling the updateUtil Function
    // for every index of the array a.
    for(int i=0;i<n;i++)
        updateUtil(i, a[i]);
}

// Function to Update the array.
void update(int *a, int ind, int val) {
    // Calculating 'delta' that is the change
    // in value.
    int delta=val-a[ind];
    a[ind]=val;
    // Calling the updateUtil function 
    // to update the bit array.
    updateUtil(ind, delta);
}

// Function to find the sum of array 
//  elements in the range [0, ind].
int findSum(int ind){
    // Initializing sum as 0.
    int sum=0;
    // Iterating while the index
    // is in the range of the array.
    while(ind>0){
        // Increasing the sum.
        sum+=bit[ind];
        // Updating the index.
        ind-=(ind&(-ind));
    }
    // Returning sum.
    return sum;
}

// Function to find the sum of a range.
int sumRange(int left, int right) {
    // Returning sum of the range 
    // [0, right] - [0, left-1].
    // Passing right+1 and left because of 
    // 1 based indexing.
    return findSum(right+1)-(findSum(left));
}

// Main Function
int main(){
    n=10;
    int a[]={4,2,1,5,6,3,9,7,2,3};
    buildBIT(a, n);
    cout<<"Sum of range 2-6 is "<<sumRange(2, 6);
    update(a, 5, 12);
    cout<<"\nSum of range 5-9 is "<<sumRange(5, 9);
    return 0;
}
-----------------------------------------------------------------------                                       
                                       
APPLICATION OF FENWICK TREE
                                       
-Fenwick Tree is mainly used to optimize the process of finding the prefix sum of the arrays such that we can have the prefix sum of an array index in logarithmic time complexity. However, there are some popular questions that can be efficiently solved using Fenwick trees:
- Mutable Range Sum Queries: Q queries can be answered in O(Q\times \log{n})O(Q×logn) time which is way better than O(Q\times N)O(Q×N) run-time of brute force approach.
- Count Inversions in an Array: The number of inversions can easily be found in O(n\times \log{n})O(n×logn) time even without sorting the array.
- Count smaller numbers after self: Many practical uses can be seen in the real world which can be computed efficiently using BIT.                                       
                                       
---------------------------------------------------------                                       
CONCLUSION                                       
                                       
- Binary Indexed Tree (Fenwick Tree) is an efficient data structure that can be used to quickly calculate the prefix sum of an array.
- If the values present in the array are mutable i.e.i.e. values can be changed using the Fenwick tree is of great use.
- Subtracting x\&(-x)x&(−x) from xx, is the efficient way to remove the least significant set-bit from xx.
- Time Complexity to calculate prefix sum or range sum of the array of size nn is O(log(n))O(log(n)) and O(n)O(n) extra space is required to store the bitbit array.                                       
                                       
                                       
                                       
                                       
                                       
