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

https://scaler.com/topics/images/pictorial-representation-of-a-segment-tree.webp
      
IMPLEMENTATION OF SEGMENT TREES:
the buildtree() function builds a segment tree using the array 'v' and stores it into the array 'tree' 
      - at each level of recursiom. the range is divided into two halves
      - then recursively the left and right children node are built for the first half and the other half og the range respectively
      - the current node will then hold the sum of its children's values. the base condition is the case of a leaf, 
      which is when the size of the range is one
      
 Suppose an array arr = [1,2,3] will be stored in the tree in 3 layers of nodes/blocks:
                      [[3+3=6]]
             [[1+2=3],  [3]]
         [[1],    [2],    [3]]
         

      
  ------------------------C++ ---------------------------------
      
    //arr->the original array, tree->the segment tree array
    vector<int>arr, tree;
    
    //s->starting index, e->end index, node->current index
    int buildTree(int node, int s int e) {
        if (s == e) {
            tree[node] = arr[s];
            return arr[s];
        }
        
        //The middle element index
        int m = s+ (e-s)/2;
        tree[node] = buildTree(node * 2, s, m) + buildTree((node * 2) + 1, m + 1, e);
        return tree[node];
    }
    
    segmentTree(const vector<int>& V) {
        arr = V;
        int max_size=4 * V.size();
        tree.resize(max_size);
        buildTree(1, 0, V.size() - 1);
    }

      
 -----------------------------PYTHON ==============
      #s->starting index
#e->end index
#node->current index
def buildTree(arr, s, e, tree, node):
    if (s == e):
        tree[node] = arr[s]
        return arr[s]
        
    #The middle element index
    mid = (s+e)/2
    tree[node] = buildTree(arr, s, mid, tree, node * 2) + buildTree(arr, mid + 1, e, tree, node * 2 + 1)
    return tree[node]

def constructST(arr, n):
    max_size = 4*n;
    tree = [0] * max_size
    buildTree(arr, 0, n - 1, tree, 1)
    return tree

      
-----------------------------------------------
 Operations of Segment Tree
This example is an implementation of a segment tree specifically as a solution to the problem 
of finding the sum of element in an array segment in range-based queries, and therefore is 
not a formal generic segment tree implementation as it would vary with each problem, just as 
the various coffees do.
      
      
Query
The ‘query()’ function takes in as parameters the boundaries of the query, ‘l’ and ‘r’, 
and returns the sum of the elements in this range of ‘l’ and ‘r’ in the array. Thus a query 
call of range [ 1,2 ] would return the sum of elements present in the array within the 
index bounds of 1 and 2.

the-sum-of-values-segment-tree segment-tree-the-sum-of-values
      
https://scaler.com/topics/images/segment-tree-the-sum-of-values.gif
      
Taking an example shown in the above cool gif, a query of [0,2] is easily retrieved as 
[0,2] happens to be present in a node already. But for a query [0,4] some extra muscle is 
required.
We don't have [0,4] on a node, but what we have are components like [0,2], [3,5], etc. 
Its almost like figuring out something from pieces of a map 😁.
We've got to extract and refine information from these components and merge them to obtain 
the desired result, i.e. an answer to the query [0,4].
We get the value of [0,2] from the pre-existing node of same label beneath [0,5]. 
How do we get [3,4]? From [3,5]. Instead of using the value present at node [3,5], 
one would look at its depth and to one's wonder, node [3,5] happens to have [3,4] as its 
left child.
This node is exactly what we need (remember [0,2] from previous case). Now we have the 
sum of arrays within indices range [0,2] and [3,4] as well which on addition would yield 
the desired output which is query(0,4). Bravo!

      
C++---------------------------
  /*
   s->current array bound start index,
   e->current array bound end index,
   qs->current query start index,
   qe->current query end index,
   node->current tree node index
  */
  int getSumUtil(int s, int e, int qs, int qe, int node) {
    if (qs <= s && qe >= e)
      return tree[node];

    if (e < qs || s > qe)
      return 0;

    int mid = s+ (e-s)/2;
    return getSumUtil(s, mid, qs, qe, 2*node) +
      getSumUtil(mid+1, e, qs, qe, 2*node+1);
  }

  int getSum(int qs, int qe) {
    if (qs < 0 || qe > n-1 || qs > qe) {
        cout<<"Invalid Input";
        return -1;
    }
    return getSumUtil(0, n-1, qs, qe, 1);
  }

      PYTHON-----------------------
      #s->current array bound start index
#e->current array bound end index
#qs->current query start index
#qe->current query end index
#node->current tree node index
def getSumUtil(tree, s, e, qs, qe, index):
    if (qs <= s and qe >= e):
        return tree[node]
    if (e < qs or s > qe):
        return 0
    mid = s+(e-s)/2
    return getSumUtil(tree, s, mid, qs, qe, 2 * node) + getSumUtil(tree, mid + 1, e, qs, qe, 2 * node + 1)

def getSum(tree, n, qs, qe):
    if (qs < 0 or qe > n - 1 or qs > qe):
        print("Invalid Input", end="")
        return -1
    return getSumUtil(tree, 0, n - 1, qs, qe, 1)

Update
The update operation takes in the new value to be set and the corresponding index. 
After making the update to the tree array, it needs to make similiar relevant changes 
to the actual segment tree. This is done by calling the ‘updateValueUtil()’ function which 
recursively updates the segment tree. To understand this better let us take a look at the
previous example. Suppose we need to set the element present at index 2 to the value of 10.

We first update the tree array at index 2 to 10, and then call the ‘updateValueUtil()’ 
function to update the segment tree.
Now begins the real adventure. The recursive function takes a bunch of parameters- the 
difference this update will produce, the index of the current node in the segment tree, 
start index and end index of the current range in recursion.
If current node index is out of range, we return. If the current node index is within the 
range, we update the value of the node and then recursively call the function on the left 
and right child of the current node. Thus the new value at node [2,2] will be 10.
This affects a couple of other nodes in the tree, naturally the ones having ranges inclusive 
of 2. These are [0,2] and [0,5]. Note that the old value at node/index 2 was 7 and the value 
of dif is 10-7=3. At [0,5] dif will be added to set its new value as 18(=15+3). Finally comes 
the turn of root node [0,5]. Its value will be updated as 47=(44+3).
     
C++----------------------------------
            void updateValueUtil(vector<int>&st, int ss, int se, int i, int diff, int si){
          if (i < ss || i > se)
              return;
          st[si] = st[si] + diff;
          if (se != ss) {
              int mid = ss + ( ( se - ss ) >> 1 );
              updateValueUtil(st, ss, mid, i, diff, 2 * si + 1);
              updateValueUtil(st, mid + 1, se, i, diff, 2 * si + 2);
          }
      }

      void updateValue(vector<int>&arr, vector<int>&st, int n, int i, int new_val){
          if (i < 0 || i > n - 1) {
              cout << "Invalid Input";
              return;
          }
          int diff = new_val - arr[i];
          arr[i] = new_val;
          updateValueUtil(st, 0, n - 1, i, diff, 0);
      }

PYTHON ----------------------------
          def updateValueUtil(st, ss, se, i, diff, si):
        if (i < ss or i > se):
            return
        st[si] = st[si] + diff
        if (se != ss):
            mid = ss+((se-ss)/2)
            updateValueUtil(st, ss, mid, i,diff, 2 * si + 1)
            updateValueUtil(st, mid + 1, se, i,diff, 2 * si + 2)

    def updateValue(arr, st, n, i, new_val):
        if (i < 0 or i > n - 1):
            print("Invalid Input", end="")
            return
        diff = new_val - arr[i]
        arr[i] = new_val
        updateValueUtil(st, 0, n - 1, i, diff, 0)

      
      
      
      
      COMPLEXITIES OF SEGMENT TREE
      tree consutruction is o(n), n being the number of elements put in the tree, as n calls to buildtree() will be made overall, 
      as there are (s*n)-1 nodes in the tree and value of each node is computed only once during tree construction. THe time complexity of a query operation is o(logn base 2) as a maximum of 4 nodes will be visited at any level 
      of recusrion and the height of the tree is logn base 2 which corrresponds to the number of levels. 
      
      The space compelxity of segment tree is o(n)
      
      
      USE CASE OF SEGMENT TREE
      - computational geometry 
      - geographic information systems
      - machine learning 

      OTHER RANGE-QUERY DATA STRUCTURES:
      - sqrt-decomposition - answers each query in o(sqrt(n)), preprocessing done in o(n)
      - fenwick tree - answers each query in o(logn), preprocessing done in o(nlogn)
      
      
      Summary: 
      - Alternatives to segment tree are Binary Indexed Tree and SQRT tree.
      - Applicable where pre-computation fails or is costly.
      - Used for efficiently solving problems involving range query operations.
      - A divide and conquer algorithm.
      - Time Complexity for tree construction is O(n).
      - Time complexity for querying and updation are O(log n).
      

      
      
      
