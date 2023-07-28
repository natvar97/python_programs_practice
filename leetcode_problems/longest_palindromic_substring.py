class Solution:
    def longest_palindrome(self, s: str) -> str:
        total_length = len(s)
        if total_length < 2:
            return s
        start = 0
        max_length = 1
        for i in range(total_length):
            low = i - 1
            high = i + 1

            while high < total_length and s[high] == s[i]:
                high += 1

            while low >= 0 and s[low] == s[i]:
                low -= 1

            while high < total_length and low >= 0 and s[high] == s[low]:
                low -= 1
                high += 1
            length = high - low - 1
            if max_length < length:
                max_length = length
                start = low + 1

        return s[start:start + max_length]


solution = Solution()
print(solution.longest_palindrome('cbbd'))
