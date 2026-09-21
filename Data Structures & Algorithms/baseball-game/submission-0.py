class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []

        for op in operations:
            if op == "+":
                stack.append(stack[-1] + stack[-2]) #we add to the stack
            elif op == "D":
                stack.append(stack[-1] * 2) #we add the doubled value 
            elif op == "C":
                stack.pop() #we invalidate/take out
            else:
                stack.append(int(op))
        return sum(stack)