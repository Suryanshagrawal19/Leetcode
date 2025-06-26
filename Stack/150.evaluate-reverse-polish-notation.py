#
# @lc app=leetcode id=150 lang=python3
#
# [150] Evaluate Reverse Polish Notation
#

# @lc code=start
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        for i in tokens:
            if i=='+':
                stack.append(stack.pop()+stack.pop())
            elif i=='*':
                stack.append(stack.pop()*stack.pop())
            elif i=='-':
                r=stack.pop()
                l=stack.pop()
                stack.append(l-r)
            elif i=='/':
                r=stack.pop()
                l=stack.pop()
                if l*r>=0:
                    stack.append(int(l/r))
                else:
                    stack.append(int(-(-l // r)))
            else:
                stack.append(int(i))
        return stack[0]
# @lc code=end

