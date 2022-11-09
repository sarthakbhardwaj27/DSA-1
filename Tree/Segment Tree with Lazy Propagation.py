ABSTRACT 

a segment tree is an efficient data structure that is used to solve range queries while handling updates aat the same time. 
the lazy propagation technique is used in a segment tree to solve range queries in o(log n) time complexity.
In lazy propagation, we make copy nodes for each node in the segment tree and use these copy nodes to store the updates.
Lazy propagation is a technique where we postpone the updates for the future and use them only when these updates are required 


INTRODUCTION
As discussed above a segment tree is a highly versatile and efficient data structure used to 
solve problems involving range queries and is flexible enough to handle update queries over a
range as well as point update queries in O(log n) time complexity. We would recommend everyone 
to refer to the article Segment Tree, as a prerequisite to this article where we discussed how 
we can use a Segment Tree to handle point updates. In this post, we will see how we can use a 
Segment Tree to handle range update queries.

Let's consider that you have an array as follows, array= [2,5,4,3]. Now you need to solve 
range minimum queries or the minimum in a given range for the given array while handling 
range updates at the same time. Now if we need to modify only a single element in the array 
we can do it using a simple Segment Tree. However, if we need to update an entire range in the 
update query. Say, we need to increase every element of the array in the range [1,3] 
(1 based indexing) by 5. Then we will not be able to use a simple Segment tree to solve the 
above problem efficiently. We will see why in the latter part of this article.

https://scaler.com/topics/images/segment-tree-with-lazy-propagation.webp
  
Another way to solve the above problem can be to traverse the given range in the array and 
update each element for every update query. Then find the minimum for the given range by 
again traversing the entire range in the array. This will take a time complexity of O(N) as
we are traversing the array for each update query. However, if there are Q such queries the
time-complexity will be O(Q*N).

Can we solve the above problem in a better complexity?
Yes, we can! We use the lazy propagation technique to solve the range update queries in 
O(log N) time complexity. Let us first discuss the structure of a segment tree and then 
understand the lazy propagation technique in a segment tree.

Structure of a Segment Tree.
A segment tree is a binary tree in which every node is associated with a certain range. The interval associated with the child nodes is approximately half the size of the interval associated with the parent node.

We can visualize the structure of the segment tree as follows-

Every node is associated with some intervals of the parent array. Parent Array refers to the array from which the segment tree is built.
The root of a segment tree represents the entire array. i.e [0,n-1] (0 based indexing).
Every leaf node is associated with a single element which is an element of the array.
The intervals associated with any two child nodes of a given node are disjoint.
The union of two child intervals gives us the interval associated with the parent node.
If we consider the root node to be indexed at 0. The left and right children of a node will be given by 2*parent_id+1 and 2*parent_id+2. We can also consider the root node to be indexed at 1. Then the index of the left and right children of a node will be 2*parent_id and 2*parent_id+1. Here parent_id is the index of the parent node.
Below is a visual representation of a segment tree used for minimum range queries.

SEGMENT TREE USED FOR MINIMUM RANGE QUERIES 

In the Segment Tree shown above, we should note that we have used 1 based indexing
for the root node. Each node's associated range is taken as left range inclusive and right
range exclusive. That is Range [Left_Range, Right_Range) means [Left_Range, Right_Range-1]. 
The leaf nodes of the tree represent the array element from which the tree is made. 
Whenever the number of elements in the array is not a power of 2 some underlying subintervals 
may not be completely filled.
                                
