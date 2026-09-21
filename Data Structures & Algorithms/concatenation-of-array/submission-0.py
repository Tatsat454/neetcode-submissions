class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:

        stack = []
        ans = []

        for i in nums:
            stack.append(i)
        
        ans += stack 
        ans += nums

        return ans 
