# Author: Kristin Towns 
# GitHub username: kristinlashun
# Date: November 15th, 2023
# Description: This program contains a function square_list that takes a list of numbers as input and mutates the original list by squaring each element in it. 

def square_list(nums):

    for i, num in enumerate(nums):
        nums[i] = num ** 2 