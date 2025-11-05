class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        row = [poured]
        
        for r in range(query_row):
            new_row = [0] * (r + 2)
            for i in range(len(row)):
                excess = max(0, row[i] - 1)
                new_row[i] += excess / 2
                new_row[i + 1] += excess / 2
            row = new_row
        
        return min(1, row[query_glass])