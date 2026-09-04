class Solution:
    def climbStairs(self, n: int) -> int:
        def recurse(n, seen):
            if n in (0, 1):
                return 1
            elif n < 0:
                return 0
            else:
                if n-1 not in seen and n-2 not in seen:
                    seen[n-1] = recurse(n-1, seen)
                    seen[n-2] = recurse(n-2, seen)
                elif n-1 in seen and n-2 not in seen:
                    seen[n-2] = recurse(n-2, seen)
                elif n-1 not in seen and n-2 in seen:
                    seen[n-1] = recurse(n-1, seen)
                return seen[n-1] + seen[n-2]

                
                
        seen = {0: 1, 1: 1}
        return recurse(n, seen)