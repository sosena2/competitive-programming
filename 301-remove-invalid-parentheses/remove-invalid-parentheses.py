class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        def is_valid(string):
            count = 0
            for ch in string:
                if ch == '(':
                    count += 1
                elif ch == ')':
                    count -= 1
                    if count < 0:
                        return False
            return count == 0

        # BFS
        queue = deque([s])
        visited = set([s])
        result = []
        found = False

        while queue:
            current = queue.popleft()

            if is_valid(current):
                result.append(current)
                found = True

            if found:
                continue

            for i in range(len(current)):
                if current[i] not in '()':
                    continue
                new_str = current[:i] + current[i+1:]
                if new_str not in visited:
                    visited.add(new_str)
                    queue.append(new_str)

        return result if result else [""]