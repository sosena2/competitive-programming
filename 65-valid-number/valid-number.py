class Solution:
    def isNumber(self, s: str) -> bool:
        s = s.strip()
        if not s:
            return False

        num_seen = False
        dot_seen = False
        e_seen = False

        for i, c in enumerate(s):
            if c.isdigit():
                num_seen = True

            elif c in ['+', '-']:
                if i > 0 and s[i - 1].lower() != 'e':
                    return False

            elif c == '.':
                if dot_seen or e_seen:
                    return False
                dot_seen = True

            elif c.lower() == 'e':
                if e_seen or not num_seen:
                    return False
                e_seen = True
                num_seen = False 

            else:
                return False

        return num_seen