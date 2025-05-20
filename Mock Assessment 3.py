from typing import List

class Solution:

    ##############
    # QUESTION 1 #
    ##############

    def rotateString(self, s: str, goal: str) -> bool:
        """
        Given two strings s and goal, return true if and only if s can become goal after some number of shifts on s.

        A shift on s consists of moving the leftmost character of s to the rightmost position.

        For example, if s = "abcde", then it will be "bcdea" after one shift.
        """
        word = s
        for shift in range(len(s)):
            word = word[1:] + word[0]

            if word == goal:
                return True
        
        return False
    

    ##############
    # QUESTION 2 #
    ##############

    def majorityElement(self, nums: List[int]) -> List[int]:
        
        answer = set()
        min_occ = len(nums)//3

        nums.sort()        
        i = 0

        while i < (len(nums)-min_occ):

            if nums[i] not in answer and nums[i] == nums[i+min_occ]:
                answer.append(nums[i])
                i+= max(1, min_occ) #if len(nums) < 3
            else:
                i+=1
        
        return list(answer)
