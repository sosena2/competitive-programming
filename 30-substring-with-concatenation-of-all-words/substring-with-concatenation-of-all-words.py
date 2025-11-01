class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not s or not words:
            return []

        word_length = len(words[0])
        word_count = Counter(words)
        num_words = len(words)
        substring_len = word_length * num_words

        result = []

        for i in range(word_length):  
            left = i
            tmp_count = Counter()
            word_used = 0

            for j in range(i, len(s) - word_length + 1, word_length):
                word = s[j:j + word_length]
                if word in word_count:
                    tmp_count[word] += 1
                    word_used += 1

                    # More than expected, shrink from the left
                    while tmp_count[word] > word_count[word]:
                        left_word = s[left:left + word_length]
                        tmp_count[left_word] -= 1
                        word_used -= 1
                        left += word_length

                    # Exactly matched num of words
                    if word_used == num_words:
                        result.append(left)
                else:
                    # Reset window
                    tmp_count.clear()
                    word_used = 0
                    left = j + word_length

        return result