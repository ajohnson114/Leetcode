"""
To begin, the explanation you have to understand what a trie is. It's a collection of nodes that allows you to quickly search to see if a certain prefix 
is in a word. For instance, if you wanted to see if there were words that started with a b in a list with a million elements that would be pretty inefficient
but what you can do is have a root node then add nodes to that successively for each letter and mark the last node in a word as the end of the word. That's
what this solution does. 

First, we create a generic node class that will make a letter or root of our trie and we give it two properties, the ability to 
have children and a marking to see if it's the last letter of a word. Then we move to the trie class and we make the instantiation portion of it just 
calling the TrieNode class we just made. For the insert function, we want to insert the word letter by letter so what we do is we start at the root
(i.e. say curr = self.root) and then iterate through the word and see if the character is a child of curr if it's not we add a node to the curr.children
then we update curr to the next character in the Trie. When we reach the end of the word we want to mark it as such in the trie so we do that. Then for 
search we would like to iterate the collection of nodes we made previously and see if the word ends where we want it to end. Therefore, we again start at 
the root (set curr = self.root) then iterate through the root and if the character is not in the children dictionary of the current character we return 
False, otherwise we update curr to be the entry of the character in its children dictionary. Following all this we should be at the end of the word so 
we return whatever that value is because we want to see if that particular word is in the trie. Finally for the Startswith function we want to do basically
the same thing as the search function but return True after iterating through the word (return True instead of curr.endofword) since 
"""


class TrieNode:
    def __init__(self):
        self.children = {}
        self.endofword = False
    
class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.root
        
        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            curr = curr.children[char]
        
        curr.endofword = True

    def search(self, word: str) -> bool:
        curr = self.root
        
        for i in word:
            if i not in curr.children:
                return False
            else:
                curr = curr.children[i]
                
        return curr.endofword

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        
        for i in prefix:
            if i not in curr.children:
                return False
            else:
                curr = curr.children[i]
                
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
