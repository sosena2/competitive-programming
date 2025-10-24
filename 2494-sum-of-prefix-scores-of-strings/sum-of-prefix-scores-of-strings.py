class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        # storing the score of the prefix
        # time complexity: o(n*n*l)
        count = defaultdict(int)
        
        ans = []

        for w in words:
            for i in range(len(w)):
                count[w[:i+1]] += 1
        
        for w in words:
            score = 0
            for i in range(len(w)):
                score += count[w[:i+1]]
            ans.append(score)
        return ans