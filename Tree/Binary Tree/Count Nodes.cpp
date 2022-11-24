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
