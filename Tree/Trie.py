-trie is an advanced DS used for storing and searching strings efficiently
-dictionaries can be implemted efficiently using a trie DS and they are used for auto-complete features that we see in the search engines.
-it is faster than binary search trees and hash tables for storing and retrieving data.
-trie ds is also known as a prefic tree or digital tree.

TIME COMPLEXITY: 
insert - o(k)
delete - o(k)
search - o(k)
k is the length of the string

the time complexity of building a trie ds is o(n*avgL) where n is the number of strings we want to insert in Trie and avgL is the average length of n strings.
- trie ds is used in prefix based searching (counting number of strings with a particular prefix), sorting strings lexicographically, etc
- trie is a tree based ds used for storing collections of strings. 
- it can be used to sort a colelciton of stirngs alphabetically as well as search weather a string with a given prefeix is present in the trie or not. 

- trie is used for storing and retrieval of data. we can also use hash table for this but trie is more efficient


PROPERTIES OF A TRIE DS
- structure is like that of a tree
- there is a root node
- each trienode consists of a an array of pointers where every index of the arry represents a character. 
- each node represents a string and each edge represents a character. 
- root node is an empty string.
- 

