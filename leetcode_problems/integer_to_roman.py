class Solution:
    def intToRoman(self, num: int) -> str:
        roman_string = ''
        dict_num = {1: 'I', 4: 'IV', 5: 'V', 9: 'IX', 10: 'X', 40: 'XL', 50: 'L', 90: 'XC', 100: 'C', 400: 'CD',
                    500: 'D', 900: 'CM', 1000: 'M'}

        for index, (key, value) in enumerate(dict_num.items()):
            if num == key:
                roman_string = value
                break
            else:
                keys_list = list(dict_num)
                if key > num:
                    count = index - 1
                    while count >= 0:
                        current_key = keys_list[count]
                        temp = num % current_key
                        if count == 0:
                            while num > 0:
                                roman_string += dict_num.get(1)
                                num -= 1
                            break
                        if temp < num and temp != 0:
                            store_num = num
                            num = temp
                            if int(store_num / current_key) >= 2:
                                temp = int(store_num / current_key)
                                dict_value = dict_num.get(current_key)
                                roman_string += (dict_value * temp)
                            else:
                                dict_value = dict_num.get(current_key)
                                roman_string += dict_value

                        elif temp == 0:
                            temp = int(num / current_key)
                            dict_value = dict_num.get(current_key)
                            roman_string += (dict_value * temp)
                            break
                        count -= 1
                    break
                elif num > 1000:
                    count = len(keys_list) - 1
                    while count >= 0:
                        current_key = keys_list[count]
                        temp = num % current_key
                        if count == 0:
                            while num > 0:
                                roman_string += dict_num.get(1)
                                num -= 1
                            break
                        if temp < num and temp != 0:
                            store_num = num
                            num = temp
                            if int(store_num / current_key) >= 2:
                                temp = int(store_num / current_key)
                                dict_value = dict_num.get(current_key)
                                roman_string += (dict_value * temp)
                            else:
                                dict_value = dict_num.get(current_key)
                                roman_string += dict_value

                        elif temp == 0:
                            temp = int(num / current_key)
                            dict_value = dict_num.get(current_key)
                            roman_string += (dict_value * temp)
                            break
                        count -= 1
                    break

        return roman_string


solution = Solution()
print(solution.intToRoman(1020))
