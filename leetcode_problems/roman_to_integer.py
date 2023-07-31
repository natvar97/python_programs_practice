class Solution:
    def roman_to_int(self, s: str) -> int:
        dict_num = {'I': 1, 'IV': 4, 'V': 5, 'IX': 9, 'X': 10, 'XL': 40, 'L': 50, 'XC': 90, 'C': 100, 'CD': 400,
                    'D': 500, 'CM': 900, 'M': 1000}

        number = 0
        length = len(s)

        prevValue = -1
        prevKey = ''
        for i in range(length):
            for key, value in dict_num.items():
                if s[i] == key:
                    if prevValue != -1 and prevValue < value:
                        number -= prevValue
                        number += dict_num.get(f"{prevKey}{key}")
                    else:
                        number += value
                    prevKey = key
                    prevValue = value
                    break

        return number


solution = Solution()
print(solution.roman_to_int('IX'))
