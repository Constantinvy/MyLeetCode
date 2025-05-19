# https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/?envType=study-plan-v2&envId=top-interview-150
"""
Given an integer array nums sorted in non-decreasing order, remove some duplicates in-place such that each unique element appears at most twice. The relative order of the elements should be kept the same.

Since it is impossible to change the length of the array in some languages, you must instead have the result be placed in the first part of the array nums. More formally, if there are k elements after removing the duplicates, then the first k elements of nums should hold the final result. It does not matter what you leave beyond the first k elements.

Return k after placing the final result in the first k slots of nums.

Do not allocate extra space for another array. You must do this by modifying the input array in-place with O(1) extra memory.
"""

from typing import List


class Solution:

    def removeDuplicates(self, nums: List[int]) -> int:

        double = False
        ptr = 1

        for i in range(1,len(nums)):

            if nums[i] == nums[i-1]:
                
                if not double:
                    nums[ptr] = nums[i]
                    ptr+=1
                    double=True
                
            if nums[i] > nums[i-1]:
                nums[ptr] = nums[i]
                ptr+=1
                double = False
        
        return ptr




def __main__():

    A = Solution()

    #### TEST 1 ####
    nums = [1,1,1,2,2,3]
    print("k = {0}".format(A.removeDuplicates(nums)))

    #### TEST 1 ####
    nums = [0,0,1,1,1,1,2,3,3]
    print("k = {0}".format(A.removeDuplicates(nums)))

__main__()


######      DEBRIEF    ######
#   SOLUTION ACCEPTED       #
#   Beats 13.41% in time    #
#   Beats 6.05% in memory   #
###############################