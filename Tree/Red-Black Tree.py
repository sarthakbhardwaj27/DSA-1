- a red black tree is a type of self-balancing binary search tree. 
- it usees an additional attribute to denote the colour of its nodes )either red or black)
- when a tree is modified by inserting or deleting nodes, the tree is often rotated and recoloured to 
ensure logarithmix time complexity for insert, search and delete operations 
- red black tree takes less time to structure the tree by restoring the height of the binary tree
- in  AVL trees, we used to rotate the trees if the height of the tree was not balances. Similarly 
rotations are made in Red-Black tree as well with an addition step i.e. recolouring of nodes to guarantee logarithmic time complexity

PROPERTIES OF RED-BLACK TREE:
 -follows all the properties of BST, left subtree should be smaller than node and right subtree bigger
- every node should have a colour (red or black)
- root node is ALWAYS BLACK
- all the leaf nodes of the tree are also BLACK IN colour
- there cant be two adjacent red nodes i.e. red node cant have a red child/parent
- every path from any node to any of its descendant null nodes must have an equal number of black nodes.

https://scaler.com/topics/images/example-of-red-black-tree.webp
  
WHY RED-BLACK TREES:
  -all the operations in BST cost O(height) to perform. h in the worst case can go to n(number of nodes) in case of skewed tree
  -https://scaler.com/topics/images/why-red-black-trees.webp
  -Since we can guarantee that at any instance of time the height of the red-black tree will be O(log(n))O(log(n)) therefore we can place an upper bound 
  of O(log(n))O(log(n)) on the time complexity of the search, insert, and delete operations.
  - But the same upper bound can also be achieved with AVL trees, so why do we even need red-black trees? 
  The answer is, AVL trees will cause more number of rotations during inserting and deleting. So it is advisable to use red-black trees when 
  we have a large number of insert/delete operations to be performed.
  
SEARCHING? 
same as BST

ALGORITHM: 
lets say we are searching for a node with key x in the red-black tree
1. start from the root node of the given tree
2. if x is smaller than the root node then recurse the left subtree, 
else if x is greater than the root , then recurse the right subtree
3. if x is found anywhere in the tree, return true else return false in the other case

Search (Node, x):
    If (Node is NULL):
        Return False
    If (Node.key == x):
        Return True
    Else If (Node.key < x):
        Search (Node.left, x)
    Else:
        Search (Node.right, x)
C++
// Node Definition 
// ------------------------------------------
class Node{
public:    
    // Key of the node
    int key;
    // Color Either R or B
    char color;
    Node *left, *right, *parent;
    // Constructor
    Node(int Key){
        // Assigning the key value.
        key=Key;
        // Assigning default color as R (Red).
        color='R';
        left=NULL;
        right=NULL;
        parent=NULL;
    }
};
// ------------------------------------------

// Function to search node. 
bool search(Node *node, int x){
    // If the node is NULL
    // return false.
    if(node==NULL)
        return false;
    // If node's key is 
    // equal to x return true.
    if(node->key==x)
        return true;
    // Search for left subtree
    // if x is greater than root's key.
    // and right subtree in the other case.
    if(node->key<x)
        return search(node->left, x);
    else 
        return search(node->right, x);
}


JAVA
// Node Definition 
// ------------------------------------------
class Node{
    // Key of the node
    int key;
    // Color Either R or B
    char color;
    Node left, right, parent;
    // Constructor
    Node(int key){
        // Assigning the key value.
        this.key=key;
        // Assigning default color as R (Red).
        color='R';
        this.left=null;
        this.right=null;
        this.parent=null;
    }
}
// ------------------------------------------

// Function to search node. 
boolean search(Node node, int x){
    // If the node is null
    // return false.
    if(node==null)
        return false;
    // If node's key is 
    // equal to x return true.
    if(node.key==x)
        return true;
    // Search for left subtree
    // if x is greater than root's key.
    // and right subtree in the other case.
    if(node.key<x)
        return search(node.left, x);
    else 
        return search(node.right, x);
}

PYTHON 
# Node Definition 
# ------------------------------------------
class Node:
# Constructor
    def __init__(self, Key):
        # Assigning the key value.
        self.key=Key
        # Assigning default color as R (Red).
        self.color='R'
        self.left=None
        self.right=None
        self.parent=None
# ------------------------------------------

# Function to search node. 
def search(node, x):
    # If node is NULL
    # return false.
    if(node==None):
        return False
    # If node's key is 
    # equal to x return true.
    if(node.key==x):
        return True
    # Search for left subtree
    # if x is greater than root's key.
    # and right subtree in the other case.
    if(node.key<x):
        return search(node.left, x);
    else:
        return search(node.right, x);

 ----------------------------------
time complexity is o(log(n))

APPLICATIONS OF RED BLACK TREE:
  1. almost all the STL/library functions which use self-balancing BST like  map,set,
  multimap, multiset ,TreeMap/TreeSet in java are using red-black trees internally
  2. completely dair scheduler (CPU scheduler used in Linux Kernel) is implemented using RB trees
  3. MySQL uses RB tree for indexing of tables present in it.
  

    

