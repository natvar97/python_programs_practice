from collections import defaultdict


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        line = defaultdict(list)
        zig_zag_string = ''

        count = 0
        delta = 1
        for index, value in enumerate(s):
            line[count].append(value)
            count += delta
            if count == numRows:
                delta = -1
                count = numRows - 2

            if count == 0:
                delta = 1

        for index, val in line.items():
            for item in val:
                zig_zag_string += str(item)
        return zig_zag_string


solution = Solution()
print(solution.convert('PAYPALISHIRING', 3))
