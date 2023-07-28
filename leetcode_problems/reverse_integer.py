class Solution:
    def reverse(self, x: int) -> int:
        if x > (pow(2, 31) - 1) or x < (-pow(2, 31)):
            return 0

        is_minus = x < 0
        if is_minus:
            x = -x

        digit_string = str(x)[::-1]

        reversed_number_string = ''
        for digit in digit_string:
            reversed_number_string += str(digit)
        result_digit = int(reversed_number_string)
        if is_minus:
            result_digit = -result_digit

        if result_digit > (pow(2, 31) - 1) or result_digit < (-pow(2, 31)):
            return 0
        return result_digit


solution = Solution()
print(solution.reverse(1534236469))
