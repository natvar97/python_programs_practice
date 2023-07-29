class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        is_matched = True

        count = 0
        while True:
            val = p[count]
            for i in range(count, len(s)):
                if val == s[i] or val == "." or val == "*":
                    count += 1
                    break
                elif val != "." and val != "*" and val != s[i]:
                    is_matched = False
                else:
                    break

            if not is_matched:
                break
        return is_matched


solution = Solution()
print(solution.isMatch('apple', 'a.*e'))
