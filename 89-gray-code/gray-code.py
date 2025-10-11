class Solution:
    def grayCode(self, n: int) -> List[int]:
        result = []
        for i in range(1 << n):  # 1<<n means 2^n
            result.append(i ^ (i >> 1))
        return result