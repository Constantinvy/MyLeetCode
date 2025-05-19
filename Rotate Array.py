# https://leetcode.com/problems/rotate-array/?envType=study-plan-v2&envId=top-interview-150
"""
Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.
"""

from typing import List

class Solution:
    
    def rotate2(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
    
        """

        n = len(nums)
        rotation = k % n

        if n%rotation == 0:

            for i in range(rotation):

                index = i
                old_val = nums[i]
                count = 0

                while index != i or count == 0:
                    
                    a = nums[(index+rotation)%n]
                    nums[(index+rotation)%n] = old_val
                    old_val = a

                    index = (index+rotation)%n
                    count +=1
        
        else:
            i=0
            index = i
            old_val = nums[i]
            count = 0

            while index != i or count == 0:
                
                a = nums[(index+rotation)%n]
                nums[(index+rotation)%n] = old_val
                old_val = a

                index = (index+rotation)%n
                count +=1

    def rotate3(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
    
        """
        n = len(nums)
        rotation = k % n 
        answer = [0]*n

        for i in range(n):
            answer[(i+rotation)%n] = nums[i]
        
        for i in range(n):
            nums[i] = answer[i]

    
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
    
        """
        n = len(nums)
        rotation = k % n 
        
        if rotation==0:
            return
        
    
    def rotate_rec(self, nums, k, elem, index_elem):
        """
        Place nums[index_elem] = elem at its right place and ensure the switch of the previous element
        """
        return




# [1,2,3,4,Z,Z]
# [Z,Z,1,2,3,4]




def __main__():

    A = Solution()

    #### TEST 1 ####
    nums = [1,2,3,4,5,6,7]
    A.rotate(nums, 3)
    print("rotated array = {0}".format(nums))

    nums = [-1,-100,3,99]
    A.rotate(nums, 2)
    print("rotated array = {0}".format(nums))


    nums = [1,2,3,4,5,6]
    A.rotate(nums, 4)
    print("rotated array = {0}".format(nums))


__main__()       
