from typing import List

class Solution:

    def countCharacters(self, words: List[str], chars: str) -> int:
    
        """
        You are given an array of strings words and a string chars.
        A string is good if it can be formed by characters from chars (each character can only be used once for each word in words).    
        Return the sum of lengths of all good strings in words.
        """

        letter_available = {}
        for letter in chars:
            if letter not in letter_available:
                letter_available[letter] = 0
            
            letter_available[letter]+=1

        total = 0
        for word in words:
            
            if len(word) <= len(chars):

                letter_available_copy = letter_available.copy()
                same_letter = 0

                for letter in word:
                    if letter in letter_available_copy and letter_available_copy[letter] > 0:
                        letter_available_copy[letter]-=1
                        same_letter+=1
                    else:
                        break
                
                if same_letter==len(word):
                    total+=same_letter
        
        return total


    ##############
    # QUESTION 2 #
    ##############  

    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        """
        You have n dice, and each dice has k faces numbered from 1 to k.
        Given three integers n, k, and target, return the number of possible ways (out of the kn total ways) to roll the dice, so the sum of the face-up numbers equals target. Since the answer may be too large, return it modulo 109 + 7.
    
        """

        return self.solve(n, k, target, {})
    

    def solve(self, n, k, target, memory):

        if (n,target) in memory:
            return memory[(n,target)]

        if n == 0:
            return 1 if target == 0 else 0
        
        if target < 0:
            return 0
        
        tot = 0
        for val_i in range(1,k+1):
            tot = (tot + self.solve(n-1, k, target-val_i, memory)) % (10**9 + 7)


        memory[(n,target)] = tot % (10**9 +7)

        return memory[(n,target)]






