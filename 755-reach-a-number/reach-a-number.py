class Solution:
    def reachNumber(self, target: int) -> int:
        target = abs(target)
        n = 0
        sum_ = 0
        while True:
            n += 1
            sum_ += n
            if sum_ >= target and (sum_ - target) % 2 == 0:
                return n
