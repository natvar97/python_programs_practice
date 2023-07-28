class Solution:

    def two_sum(self, nums: list[int], target: int) -> list[int]:
        index_array = []
        is_inner_break = False
        for index, num in enumerate(nums):
            for inner_index in range(index + 1, len(nums)):
                if target == num + nums[inner_index]:
                    is_inner_break = True
                    index_array.append(index)
                    index_array.append(inner_index)
                    break

            if is_inner_break:
                break
        return index_array


solution = Solution()
print(solution.two_sum([3, 2, 4], 6))
