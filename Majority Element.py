# https://leetcode.com/problems/majority-element/?envType=study-plan-v2&envId=top-interview-150
"""
Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.
"""
from typing import List


class Solution:
    
    def majorityElement(self, nums: List[int]) -> int:
        # O(n) + O(1) space

        nums = sorted(nums)
        counter = 1
        
        for i in range(1, len(nums)):
            
            if nums[i] == nums[i-1]:
                counter+=1
                if counter >= len(nums)/2:
                    return nums[i]
            
            else:
                counter=1

        return nums[-1]




def __main__():

    A = Solution()

    #### TEST 1 ####
    nums = [3,3,4]
    print("majority element = {0}".format(A.majorityElement(nums)))


__main__()

####    DEBRIEF     ####
#       L'élément majoritaire se trouvve en nums[n//2] si nums est trié !
# [0,1,1,2,3,4,5,6,7,8,9,10]
