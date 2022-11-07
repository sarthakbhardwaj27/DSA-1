- it is a flexible tree based DS that is used to effectively solve porblems involving range query operations
- it allows answering range queries over an array effectively. while still being flexible enough to allow
modifying the array

# WHAT IS SEGMENT TREE?
- A segment tree enters the scene, where other techniques such as prefix computation fail. 
Let's understand this contrast between the two. Suppose we need to compute the sum of the 
elements of an array within a range. The prefix sum array method yields an O(1) solution, 
while the segment tree would result in an O(log n) solution. Doesn't sound very helpful?

What if the operation was finding the maximum/minimum element within a range, 
bitwise OR over a range, gcd over a range, etc.?

Suppose we have an array Arr = [0,1,2,3,4,5]. Its prefix sum array will be 
preSum = [0,1,3,6,10,15]. Now to calculate the sum of elements within index 
bounds [1,4] we use ans = preSum[4]-preSum[0]. Easy peasy.

Unfortunately, the prefix minimum element array will be preMin = [0,0,0,0,0,0]. 
Is there any way of calculating the minimum element within the same range [1,4]? 
NO! :( Not with prefix technique. Fortunately, with segment trees' versatility, such 
problems can be solved efficiently.

Prefix computation does enable making updates to the array, but it needs to recompute the 
whole array making O(n) time complexity overhead per update. One would not only update the 
element at a given index in the array but will have to also make changes in prefix array. 
Thus prefix computation is definitely not the smart choice to make when updation is required. 
The segment tree is!

Now imagine if we could update such ranges in logarithmic time as well, wouldn’t it be cool?

# LETS SEE HOW SEGMENT TREE ACHIEVES IT
- A segment tree is implemented in the array-based tree format { C.P. GUYS COULD RELATE }. 
The parent-child hierarchy is such that each array block represents a node by storing its 
value. For ith node, its left and right children are stored in (i * 2)th and (i * 2 + 1)th 
block respectively. The entire array of elements to be operated upon is present in the 
segment tree in chunks of many sizes referred to as segments; hence the name segment tree 😉.

The divide and conquer strategy here dictates that during traversal along some path from top 
to bottom in the tree, at each level the sample space is halved. This tremendously improves 
efficiency during searching, updation, etc. Let’s have a look at a pictorial representation 
of a segment tree:


