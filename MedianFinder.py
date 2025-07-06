import math
nums_to_sort = str(input("Input numbers: "))
List_of_nums = nums_to_sort.split(", ")
List_of_nums.sort()
tmp = len(List_of_nums)
if (tmp % 2 != 0):
    tmp += 1
print(List_of_nums[int((tmp/4)*3)])