#include<bits/stdc++.h>
using namespace std;

#define vi vector<int>
#define vii vector<pii>
#define vvi vector<vector<int>>
#define lli long long int
#define li long int
#define f(i,a,b) for(int i=a;i<b;i++)
#define fr(i,n,b) for(int i=n;i>=b;i--)
#define pb push_back
#define pii pair<int,int>

class node{
	public:
	int data;
	node* left;
	node* right;
};
//or use this, here we do not have to put scope 
//struct node{
//	int data;
//	struct node *left;
//	struct node *right;
//};
node* createnode(int k)
{
	node* newnode = new node();
	newnode->data = k;
	newnode->left = NULL;
	newnode->right = NULL;
	
	return newnode;
}

void traverseTree(node* curr)
{
	if(curr==NULL)
		return;
		
	traverseTree(curr->left);
	cout<<curr->data<<" ";
	traverseTree(curr->right);
}
void levelorder(node* root)
{
	if(root == NULL)
		return;
		
	queue<node*> q;
	q.push(root);
	q.push(NULL);
	
	while(!q.empty())
	{
		node* node = q.front();//node - 1
		q.pop();
		if(node!=NULL)
		{
			cout<<node->data<<" ";
			if(node->left)
				q.push(node->left);
			if(node->right)
				q.push(node->right);	
		}
		else if(!q.empty())
			q.push(NULL);
	}
}
int countnodestwo(node* curr)
{
	int count = 0;
	if(curr==NULL)
		return count;
	
	//use any traversal and maintain the count
	//here i will be using level order traversal just for practise
	
	queue<node*> q;
	q.push(curr);
	
	while(!q.empty())
	{
		node* top = q.front();
		q.pop();
		count++;
		if(top!=NULL)
		{
			//cout<<top->data<<" ";
			if(top->left!=NULL)
				q.push(top->left);
			if(top->right)
				q.push(top->right);
		}
	}	
	return count;
}

//better approach 
//using recursion

int countnodes(node* root)
{
	if(root==NULL)
		return 0;
	int leftcount = countnodes(root->left);
	int rightcount = countnodes(root->right);
	
	return leftcount+rightcount+1;
}

//one way could be to traverse all the data and then cumulate them
//2nd would be using recursion
int sumofnodes(node* curr)
{
	if(curr==NULL)
		return 0;
	
	int leftsum = sumofnodes(curr->left);
	int rightsum = sumofnodes(curr->right);
	
	return leftsum + rightsum + curr->data;
}
//we can use level order traversal and use NULL as a reference point meaning, 
//number of nulls is equal to number of levels which is equal to the height
int heightoftree_naive(node* curr)
{
	//level order traversal
	int height = 0;
	queue<node*> q;
	if(curr==NULL)
		return height;
	
	q.push(curr);
	q.push(NULL);
	height++;
	while(!q.empty())
	{
		node* top= q.front();
		q.pop();
		if(top!=NULL)
		{
			if(top->left)
				q.push(top->left);
			if(top->right)
				q.push(top->right);
		}
		else if(!q.empty())
		{
			q.push(NULL);
			height++;
		}
	}
	
	
	return height;
}
int heightoftree(node* curr)
{
	if(curr==NULL)
		return 0;
	
	int LH = heightoftree(curr->left);
	int RH = heightoftree(curr->right);
	
	return max(LH,RH)+1;
}
int diameteroftree(node* curr)
{
	//diameter is the longest distance betwenn any 2 nodes in a tree
	//there are two cases 
	//case 1 - longest path passes through root node
	//case 2 = longest path does not pass through root node
	
	//approach 1 - o(n^2)
	//1) calculate the maximum diameter of left subtree
	//2) calculate the maximum diamter of right subtree
	//3) calculate the left height from root node and right height from root node +1
	//do a max of the 3 values
	if(curr==NULL)
		return 0;
	int diam1 = diameteroftree(curr->left);
	int diam2 = diameteroftree(curr->right);
	int diam3 = heightoftree(curr->left)+heightoftree(curr->right)+1;
	
	return max(max(diam1,diam2),max(diam2,diam3));
}
int main()
{
	ios_base::sync_with_stdio(false);
    cin.tie(NULL);
	
//		5
//	7		6
//1     9		10
//					11
	node* curr = createnode(5);
	curr->left = createnode(7);
	curr->left->left = createnode(1);
	curr->left->right = createnode(9);
	curr->right = createnode(6);
	curr->right->right = createnode(10);
	curr->right->right->right = createnode(11);
//	traverseTree(curr);
//	cout<<endl;
//	levelorder(curr);
	
//	cout<<countnodes(curr);
//	cout<<sumofnodes(curr);	
	
//	cout<<heightoftree(curr);
	cout<<diameteroftree(curr);
}

