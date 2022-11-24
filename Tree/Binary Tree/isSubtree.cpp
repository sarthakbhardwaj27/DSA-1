bool isidentical(node* root, node* new_root)
{
	if(root==NULL and new_root==NULL)
		return true;
	if(root==NULL or new_root==NULL)
		return false;
	if(root->data == new_root->data)
	{
			return isidentical(root->left, new_root->left) and isidentical(root->right,new_root->right);
	}
	return false;
}
bool issubtree(node* root, node* new_root)
{
	//if the second tree is null then its root will be null as well, which is always 
	//a part of a tree, hence always true
	if(new_root==NULL)
		return true;
	if(root==NULL)
		return false;
	//we will traverse both the tree, maybe preorder 
	// first locate the new_root in main tree, then check left subtree and then rightsubtree
	
	if(root->data == new_root->data)
	{
		if(isidentical(root,new_root))
			return true;
	}
	
	return issubtree(root->left,new_root) or issubtree(root->right,new_root);
	
}
