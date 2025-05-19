# https://leetcode.com/problems/merge-sorted-array/?envType=study-plan-v2&envId=top-interview-150
"""
You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.

Merge nums1 and nums2 into a single array sorted in non-decreasing order.

The final sorted array should not be returned by the function, but instead be stored inside the array nums1. To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.

"""
from typing import List

class Solution:
    
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        index1 = 0
        index2 = 0
        answer = []

        
        while index1 < m and index2 < n:
            
            if nums1[index1] <= nums2[index2]:
                answer.append(nums1[index1])
                index1+=1
            
            if nums2[index2] < nums1[index1]:
                answer.append(nums2[index2])
                index2+=1


        if index1 == m:
            for i in nums2[index2:]:
                answer.append(i)

        else:
            for i in nums1[index1:m]:
                answer.append(i)

        for i in range(n+m):
            nums1[i] = answer[i]


def __main__():

    A = Solution()

    #### TEST 1 ####
    nums1 = [1,2,3,0,0,0]
    A.merge(nums1, 3, [2,5,6], 3)
    print("nums1 = {0}".format(nums1))


    #### TEST 2 ####
    nums1 = [4,5,6,0,0,0]
    A.merge(nums1, 3, [1,2,3], 3)
    print("nums1 = {0}".format(nums1))


#####   DECISION     ####
#   Beats 100% time     #
#   Beats 8.17% memory  #
# => Should sort by increasing value (and thus starting from the end of the arrays !!



__main__()