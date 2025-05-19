# https://leetcode.com/problems/remove-element/?envType=study-plan-v2&envId=top-interview-150
"""
Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. The order of the elements may be changed. Then return the number of elements in nums which are not equal to val.

Consider the number of elements in nums which are not equal to val be k, to get accepted, you need to do the following things:

Change the array nums such that the first k elements of nums contain the elements which are not equal to val. The remaining elements of nums are not important as well as the size of nums.
Return k.
"""
from typing import List

class Solution:

    def removeElement(self, nums: List[int], val: int) -> int:

        answer = []
        for i in nums :
            if i != val:
                answer.append(i)
        
        for i in range(len(answer)) :
            nums[i] = answer[i]

        return len(answer)



def __main__():

    A = Solution()

    #### TEST 1 ####
    nums = [3,2,2,3]
    print("k = {0}".format(A.removeElement(nums, 3)))


# INCORRECT BECAUSE NOT IN PLACE !!!

__main__()