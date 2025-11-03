class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        def bit(d):
            return 1 << d

        # initialize masks
        rows = [0] * 9
        cols = [0] * 9
        boxes = [0] * 9
        empties = []

        for r in range(9):
            for c in range(9):
                ch = board[r][c]
                if ch == '.':
                    empties.append((r, c))
                else:
                    d = int(ch)
                    b = (r // 3) * 3 + (c // 3)
                    mask = bit(d)
                    rows[r] |= mask
                    cols[c] |= mask
                    boxes[b] |= mask  

        ALL = (1 << 10) - 1

        def dfs(k: int) -> bool:
            # k is index in empties
            if k == len(empties):
                return True 

            # choose the empty with minimum candidates (MRV heuristic helps speed)
            best_idx = -1
            best_count = 10
            for i in range(k, len(empties)):
                r, c = empties[i]
                b = (r // 3) * 3 + (c // 3)
                used = rows[r] | cols[c] | boxes[b]
                candidates = (~used) & (ALL) 
           
                candidates &= ~1
                cnt = candidates.bit_count()
                if cnt == 0:
                    return False
                if cnt < best_count:
                    best_count = cnt
                    best_idx = i
                    if cnt == 1:
                        break
            
            # swap chosen empty into position k
            empties[k], empties[best_idx] = empties[best_idx], empties[k]
            r, c = empties[k]
            b = (r // 3) * 3 + (c // 3)
            used = rows[r] | cols[c] | boxes[b]
            candidates = (~used) & (ALL)
            candidates &= ~1

            while candidates:
                v = candidates & -candidates # lowest set bit
                d = v.bit_length() - 1 # digit
                # place
                mask = bit(d)
                rows[r] |= mask
                cols[c] |= mask
                boxes[b] |= mask
                board[r][c] = str(d)


                if dfs(k + 1):
                    return True

                # undo
                rows[r] &= ~mask
                cols[c] &= ~mask
                boxes[b] &= ~mask
                board[r][c] = '.'

                candidates &= candidates - 1

            empties[k], empties[best_idx] = empties[best_idx], empties[k]
            return False

        dfs(0)