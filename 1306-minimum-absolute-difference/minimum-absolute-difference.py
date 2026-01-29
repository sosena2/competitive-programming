class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        ans = []
        sorted_arr = sorted(arr)
        n = len(arr)
        diff = sorted_arr[1] - sorted_arr[0]

        for i in range(n-1):
            if sorted_arr[i+1] - sorted_arr[i] < diff:
                diff = sorted_arr[i+1] - sorted_arr[i]

        for i in range(n-1):
            if sorted_arr[i+1] - sorted_arr[i] == diff:
                ans. append([sorted_arr[i], sorted_arr[i+1]])
        return ans

        