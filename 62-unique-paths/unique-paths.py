class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
    #   buttom up

    # the last row
       row = [1]*n
       for i in range(m-1):
           new = [1]*n
           for j in range(n-2, -1, -1):
                # summing the buttom and the right row
               new[j] = new[j+1] + row[j]
            # updating row
           row = new
       return row[0]



