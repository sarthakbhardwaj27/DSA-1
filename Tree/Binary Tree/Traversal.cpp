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
//	curr->right->right->right = createnode(11);
//	traverseTree(curr);
//	cout<<endl;
//	levelorder(curr);
	
//	cout<<countnodes(curr);
//	cout<<sumofnodes(curr);	
	
//	cout<<heightoftree(curr);
	cout<<diameteroftree(curr);
}
