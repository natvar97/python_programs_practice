class Solution:
    def isPalindrome(self, x: int) -> bool:
        original_string = str(x)
        reversed_string = original_string[::-1]
        return original_string == reversed_string


solution = Solution()
print(solution.isPalindrome(-121))
