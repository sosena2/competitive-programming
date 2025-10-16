class Trie:
    def __init__(self):
        self.root = TrieNode()
class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        words = sentence.split()
        # make sure we get the shortest first
        dictionary.sort(key = len)
      
        for i in range(len(words)):
            for char in dictionary:
                if words[i].startswith(char):
                    words[i] = char
                    break 
        return ' '.join(words)
        
                   
        