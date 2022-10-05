If there are n nodes in a perfect binary tree, and its height is given by "logn". 
At every level the number of child nodes double so that is why

The minimum number of nodes possible at the height h of a binary tree is given by h+1

If the BT has L number of leaf nodes, then height is given by L+1

At each level i of a BT, the number of total nodes is given by 2^i

In full binary tree, if there are n number of total nodes: 
  the number of internal nodes is given by (n-1)/2
  the number of leaf nodes is given by (n+1)/2
  
COMPLETE BINARY TREE: 
  a complete binary tree is a BT in which all the elements are aaranges without missing any sequence
  all the levels are completely filled except the last level that may or may not be completely filled

PERFECT BINARY TREE: 
  if in a tree all the internal nodes have exactly two children nodes, 
  all the leaf nodes are on the same level
  a perfect binary tree with height h, the total number of nodes in this case is given by 2h-1
  
DEGENERATE BINARY TREE:
  if in a binary tree each node contains only one child node either on the left side or the right side of the tree
  they are equal to linked lists in terms of performance
  
BALANCED BINARY TREE:
  a BT is said to be balanced if the height of the left and the right subtree differ by 0 or 1

-------------------IMPLEMENTATION---------------------------------

// Binary Tree in C++
//structure that contains data, address of left child, address of the right child
struct Node {
 int data;
 struct node *left;
 struct node *right;
};
 
// function to create a new node
Node *newNode(int data) {
 //allocating space for the node
 Node *node = new Node;
 
 //storing in the data
 node->data = data;
  //setting left and right children to NULL
 node->left = NULL;
 node->right = NULL;
 return (node);
}

# Binary Tree in Python
 
# node that hold data, address of the left child, and address of the right child
class Node:
   def __init__(self, key):
       # setting left and right child equal to NULL
       self.left = None
       self.right = None
      
       # inserting data into the node
       self.val = key
 
root = Node(1)
root.left = Node(2)
root.right = Node(3)

------------------BENEFITS OF BINARY TREE------------------
1. BT are used in BST, It helps in searching for elements in a faster and efficient way 
2. They are also used in heaps that are special kind of binary trees. Heaps are used in heap sort,
which is an efficient sorting algorithm. Heaps are used in building priority queues in which 
elements are arranged in the order of their priorities.
3. Binary trees are used in converting different prefix and postfix expressions.
4. BT are also used in graph traversal algorithms like Dijkastra's algo
5. some real life application of BT include virtual memory management and 3D where faster 
rendering of objects is required

---------------------------COMPLEXITIES-------------------------
Binary tree time complexity:
Seraching: worst case is O(n)
Insertion: worse case O(n)
Deletion: worst case O(n)
  
Binary tree space complexity:
Searching: O(N)
Insertion: O(N)
Deletion: O(N)

