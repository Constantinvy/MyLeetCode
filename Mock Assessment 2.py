from typing import List

class Solution:

    ##############
    # QUESTION 1 #
    ##############

    #   #JeSuisTropCon!!!!

    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        """
        An axis-aligned rectangle is represented as a list [x1, y1, x2, y2], where (x1, y1) is the coordinate of its bottom-left corner, and (x2, y2) is the coordinate of its top-right corner. Its top and bottom edges are parallel to the X-axis, and its left and right edges are parallel to the Y-axis.

        Two rectangles overlap if the area of their intersection is positive. To be clear, two rectangles that only touch at the corner or edges do not overlap.

        Given two axis-aligned rectangles rec1 and rec2, return true if they overlap, otherwise return false.
        """

        for i in range(4):
            rec1[i] = float(rec1[i]) - 0.001

        Ax1,Ay1,Ax2,Ay2 = rec1
        Bx1,By1,Bx2,By2 = rec2



        if (Ax2 == Bx1): return False
 
        if (Bx1 <= Ax1 <= Bx2) or (Bx1 <= Ax2 <= Bx2) or (Ax1 <= Bx1 <= Ax2) or (Ax1<=Bx2<=Ax2):
            if (By1 <= Ay1 <= By2) or (By1 <= Ay2 <= By2) or (Ay1 <= By1 <= Ay2) or (Ay1<=By2<=Ay2):
                
                
                return True
        
        return False
    
    """
    CORRECTION DE CHATGPT : 
    def isRectangleOverlap(rec1, rec2):
        # Extract coordinates
        x1, y1, x2, y2 = rec1
        x3, y3, x4, y4 = rec2

        # Check for non-overlapping conditions
        if x2 <= x3 or x4 <= x1 or y2 <= y3 or y4 <= y1:
            return False

        return True
    """

    ##############
    # QUESTION 2 #
    ##############

    def partitionLabels(self, s: str) -> List[int]:
        """
        You are given a string s. We want to partition the string into as many parts as possible so that each letter appears in at most one part. For example, the string "ababcc" can be partitioned into ["abab", "cc"], but partitions such as ["aba", "bcc"] or ["ab", "ab", "cc"] are invalid.

        Note that the partition is done so that after concatenating all the parts in order, the resultant string should be s.

        Return a list of integers representing the size of these parts.
        """
        
        answer = []
        last_letter_index = {}
        for i in range(len(s)):
            letter = s[i]
            if letter not in last_letter_index:
                last_letter_index[letter] = 0

            last_letter_index[letter]=i

        i = 0
        while i < len(s):
            
            if last_letter_index[s[i]] == i:
                answer.append(1)
                i+=1
            
            else :

                start = i+1
                end = last_letter_index[s[i]]

                while start <= end :

                    end = max(end, last_letter_index[s[start]])
                    
                    start+=1
                
                answer.append(end-i+1)
                i = end+1   
        
        return answer
        
A = Solution()
s = "ababcbacadefegdehijhklij"
print(A.partitionLabels(s))