int heightoftree(node* curr)
{
	if(curr==NULL)
		return 0;
	
	int LH = heightoftree(curr->left);
	int RH = heightoftree(curr->right);
	
	return max(LH,RH)+1;
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
