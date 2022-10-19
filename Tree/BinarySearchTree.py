A BST is a sorted binary tree, where we can easily search for any key using Binary Search algo. 

To sort a BST the node's left subtree contains elements smaller than the node's key 

------------------------COMPLEXITIES-----------------------
Insertion: o(n)
Searching: o(height)
Deletion: o(n)
  
  
WHY DO WE NEED BINARY SEARCH TREES?

You: Wait!!!!! But Binary Search is already a super awesome searching algorithm. Why do we even need this so-called BST?

Rahul: Great question! Yes Binary Search is a perfect algorithm, correction: almost perfect 🙂 But it works only on a fixed sorted data set. If your data set is not sorted, or elements are added/removed from it, do you think Binary Search would perform well?

You: Ummmmmmm……..

Rahul: Let’s try to understand this with an example.

class node{
  int key;
  node left;
  node right;
}
------------------------------------------------------------------
Insertion:
  insert k

if node == null, create an ew node with the vlaue of the field equal to k. then return this newly createed node directly
if k <= node, then insert k in the left subtree. user recursion
if k > node, then insert k in the right subtree, using recursion
return the current node
-------------------------------------------------------------------------
Search
--------------------------------------------
Pre order traversal;

if node == null, do nothing
else
 print the current node
  visit the left subtree and repeat step 1
  visit the right subtree and repeat the step 1

In-oder traversal;

if node == null, do nothing
else:
  vist the left subtree and repeat step 1
  print the current node 
  visit the right subtree and repat step 1
 
post-order traversal;

if node -- null do nothing 
else:
  visit the left subtree and repeat step 1
  visit the right subtree and repeat step 1
  print the current node.

  --------------------------------------------
Implementation;

#include <iostream>
using namespace std;

class Node
{
public:
    int key;
    Node *left;
    Node *right;

    Node(int key)
    {
        this->key = key;
        this->left = this->right = NULL;
    }
};

class `BST`
{
private:
    Node *root;

    Node *insert(Node *node, int key)
    {
        if (node == NULL)
        {
            return new Node(key);
        }
        if (key <= node->key)
        {
            node->left = insert(node->left, key);
        }
        else
        {
            node->right = insert(node->right, key);
        }
        return node;
    }

    Node *search(Node *node, int key)
    {
        if (node == NULL || node->key == key)
        {
            return node;
        }
        if (key < node->key)
        {
            return search(node->left, key);
        }
        return search(node->right, key);
    }

    void inOrder(Node *node)
    {
        if (node == NULL)
        {
            return;
        }
        inOrder(node->left);
        cout << node->key << " ";
        inOrder(node->right);
    }

    void preOrder(Node *node)
    {
        if (node == NULL)
        {
            return;
        }
        cout << node->key << " ";
        preOrder(node->left);
        preOrder(node->right);
    }

    void postOrder(Node *node)
    {
        if (node == NULL)
        {
            return;
        }
        postOrder(node->left);
        postOrder(node->right);
        cout << node->key << " ";
    }

public:
    `BST`()
    {
        this->root = NULL;
    }

    void insert(int key)
    {
        root = insert(root, key);
    }

    Node *search(int key)
    {
        return search(root, key);
    }

    void inOrder()
    {
        cout << "The inOrder traversal is: ";
        inOrder(root);
        cout << "\n";
    }

    void preOrder()
    {
        cout << "The preOrder traversal is: ";
        preOrder(root);
        cout << "\n";
    }

    void postOrder()
    {
        cout << "The postOrder traversal is: ";
        postOrder(root);
        cout << "\n";
    }
};

static void search(`BST` `bst`, int key)
{
    if (`bst`.search(key) != NULL)
    {
        cout << key << " found\n";
    }
    else
    {
        cout << key << " not found\n";
    }
}

int main()
{
    `BST` `bst`;
    `bst`.insert(10);
    `bst`.insert(15);
    `bst`.insert(5);
    `bst`.insert(8);
    `bst`.insert(18);
    `bst`.insert(12);
    `bst`.insert(10);

    `bst`.preOrder();
    `bst`.inOrder();
    `bst`.postOrder();

    search(`bst`, 12);
    search(`bst`, 9);
}

--------------------------------------------------
in python 
#include <iostream>
using namespace std;

class Node
{
public:
    int key;
    Node *left;
    Node *right;

    Node(int key)
    {
        this->key = key;
        this->left = this->right = NULL;
    }
};

class `BST`
{
private:
    Node *root;

    Node *insert(Node *node, int key)
    {
        if (node == NULL)
        {
            return new Node(key);
        }
        if (key <= node->key)
        {
            node->left = insert(node->left, key);
        }
        else
        {
            node->right = insert(node->right, key);
        }
        return node;
    }

    Node *search(Node *node, int key)
    {
        if (node == NULL || node->key == key)
        {
            return node;
        }
        if (key < node->key)
        {
            return search(node->left, key);
        }
        return search(node->right, key);
    }

    void inOrder(Node *node)
    {
        if (node == NULL)
        {
            return;
        }
        inOrder(node->left);
        cout << node->key << " ";
        inOrder(node->right);
    }

    void preOrder(Node *node)
    {
        if (node == NULL)
        {
            return;
        }
        cout << node->key << " ";
        preOrder(node->left);
        preOrder(node->right);
    }

    void postOrder(Node *node)
    {
        if (node == NULL)
        {
            return;
        }
        postOrder(node->left);
        postOrder(node->right);
        cout << node->key << " ";
    }

public:
    `BST`()
    {
        this->root = NULL;
    }

    void insert(int key)
    {
        root = insert(root, key);
    }

    Node *search(int key)
    {
        return search(root, key);
    }

    void inOrder()
    {
        cout << "The inOrder traversal is: ";
        inOrder(root);
        cout << "\n";
    }

    void preOrder()
    {
        cout << "The preOrder traversal is: ";
        preOrder(root);
        cout << "\n";
    }

    void postOrder()
    {
        cout << "The postOrder traversal is: ";
        postOrder(root);
        cout << "\n";
    }
};

static void search(`BST` `bst`, int key)
{
    if (`bst`.search(key) != NULL)
    {
        cout << key << " found\n";
    }
    else
    {
        cout << key << " not found\n";
    }
}

int main()
{
    `BST` `bst`;
    `bst`.insert(10);
    `bst`.insert(15);
    `bst`.insert(5);
    `bst`.insert(8);
    `bst`.insert(18);
    `bst`.insert(12);
    `bst`.insert(10);

    `bst`.preOrder();
    `bst`.inOrder();
    `bst`.postOrder();

    search(`bst`, 12);
    search(`bst`, 9);
}


















