class Solution:
    def length_of_longest_substring(self, s: str) -> int:
        n = len(s)
        res = 0
        for i in range(n):
            for j in range(i, n):
                if self.are_distinct(s, i, j):
                    res = max(res, j - i + 1)

        return res

    def are_distinct(self, s: str, i: int, j: int) -> bool:
        visited = [0] * 26
        for k in range(i, j + 1):
            if visited[ord(s[k]) - ord('a')] == True:
                return False
            visited[ord(s[k]) - ord('a')] = True
        print(visited)
        return True


solution = Solution()
print(solution.length_of_longest_substring('dvdf'))
