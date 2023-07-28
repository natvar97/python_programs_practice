class Solution:
    def find_median_sorted_arrays(self, nums1: list[int], nums2: list[int]) -> float:
        combined_list: list[int] = []
        for val in nums1:
            combined_list.append(val)

        for val2 in nums2:
            combined_list.append(val2)

        combined_list = self.sort_using_bubble_sort(combined_list)

        list_size = len(combined_list)
        middle = int(list_size / 2)
        if list_size % 2 == 0:
            median = (combined_list[middle - 1] + combined_list[middle]) / 2
        else:
            median = combined_list[middle]
        return median

    def sort_using_bubble_sort(self, array: list) -> list:
        already_sorted = True
        count_iterations = 0
        for i in range(len(array)):
            for j in range(1, len(array) - count_iterations):
                if array[j] < array[j - 1]:
                    already_sorted = False
                    temp = array[j]
                    array[j] = array[j - 1]
                    array[j - 1] = temp
            count_iterations += 1
            if already_sorted:
                break
            already_sorted = True

        return array


solution = Solution()
print(solution.find_median_sorted_arrays([1, 3], [2, 7]))
