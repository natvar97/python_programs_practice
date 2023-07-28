class Solution:
    def myAtoi(self, s: str) -> int:
        list_of_decimals = []
        for val in s:
            ordinal_value = ord(val)
            if 48 <= ordinal_value <= 57:
                list_of_decimals.append(val)
            elif ordinal_value == 43 or ordinal_value == 45:
                if len(list_of_decimals) == 0:
                    list_of_decimals.append(val)
            else:
                if len(list_of_decimals) > 0 and ord(list_of_decimals[0]) != 43 and ord(list_of_decimals[0]) != 45:
                    break

        if len(list_of_decimals) == 0:
            return 0

        if len(list_of_decimals) == 1 and (ord(list_of_decimals[0]) == 45 or ord(list_of_decimals[0]) == 43):
            return 0

        result_value = ''
        for val in list_of_decimals:
            result_value += val

        final_result = int(result_value)
        if final_result < -pow(2, 31) or final_result > (pow(2, 31) - 1):
            return 0
        return final_result


solution = Solution()
print(solution.myAtoi('00000-42a1234'))
