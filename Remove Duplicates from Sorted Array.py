# https://leetcode.com/problems/remove-duplicates-from-sorted-array/?envType=study-plan-v2&envId=top-interview-150

"""
Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same. Then return the number of unique elements in nums.

Consider the number of unique elements of nums to be k, to get accepted, you need to do the following things:

Change the array nums such that the first k elements of nums contain the unique elements in the order they were present in nums initially. The remaining elements of nums are not important as well as the size of nums.
Return k.

"""

from typing import List

class Solution:

    def removeDuplicates2(self, nums: List[int]) -> int:
        
        index = 1
        unique = 1

        while index < len(nums):

            if nums[index] <= nums[index-1]:

                other = self.find_other_val(nums, index, nums[index-1])
                if other==None:
                    return unique
                
                if other > nums[index-1] :
                    nums[index] = other
            
            index+=1
            unique+=1
    
        return unique


    
    def find_other_val(self, nums, index, val):
        for i in nums[index:]:
            if i > val:
                return i 
    

    def removeDuplicates(self, nums):

        ptr1 = 0
        ptr2 = 1
        unique = 1

        while ptr2 < len(nums):

            if nums[ptr1] < nums[ptr2]:
                nums[ptr1+1] = nums[ptr2]

                ptr2+=1
                ptr1+=1
                unique+=1
            
            else:
                while nums[ptr1] == nums[ptr2]:
                    ptr2+=1
                    if ptr2 == len(nums):
                        return unique
            
        return unique





def __main__():

    A = Solution()

    #### TEST 1 ####
    nums = [0,0,1,1,1,2,2,3,3,4]
    print("k = {0}".format(A.removeDuplicates2(nums)))

    #### TEST 1 ####
    nums = [0,1,1,1,2,2,3,3,4]
    print("k = {0}".format(A.removeDuplicates2(nums)))

__main__()


####    DEBRIEF     ####
#   Beats 55.57% in time (2ms)
#   Beats 11.25% in space
# Close from the best solution