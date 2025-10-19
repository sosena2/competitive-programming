class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        count = 0
        for char in word:
            if char.isupper():
                count += 1
        if count == 0 or count == len(word):
            return True
        elif count == 1 and word[0].isupper():
            return True
        else:
            return False