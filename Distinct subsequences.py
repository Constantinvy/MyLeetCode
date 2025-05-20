# HARD PROBLEM => beats 5.07% in time and 6.6% in memory... but did it without hint and in < 1h


class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        """
        Given two strings s and t, return the number of distinct subsequences of s which equals t.

        The test cases are generated so that the answer fits on a 32-bit signed integer.
        """

        return self.numDistinctDynamic(s,t,{})

    def numDistinctDynamic(self, s, t, memory):

        if (s,t) in memory:
            return memory[(s,t)]

        n = len(s)
        m = len(t)

        if m==0:
            if (s,None) not in memory:
                memory[(s,None)] = 0
            
            memory[(s, None)] += 1
            return 1
        
        if n==0:
            return 0
        
        if s[0]!=t[0]:
            return self.numDistinctDynamic(s[1:], t, memory)

        a = self.numDistinctDynamic(s[1:], t[1:], memory)
        
        if (s[1:], t[1:]) not in memory:
            memory[(s[1:], t[1:])] = a
    
        b = self.numDistinctDynamic(s[1:], t, memory)
        if (s[1:], t) not in memory:
            memory[(s[1:], t)] = b
        
        if (s, t) not in memory:
            memory[(s,t)] = a+b

        return a+b


S = Solution()
print(S.numDistinct("baagg", "bag"))
print(S.numDistinct("rabbbit", "rabbit"))