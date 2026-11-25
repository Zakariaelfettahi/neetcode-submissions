class Solution:
    def isValid(self, s: str) -> bool:
        if s =="":
            return True
        if len(s) == 1:
            return False
        if s[0] in ['}', ']', ')']:
            return False
    
        stack = []
        for i in range(0,len(s)):
            if s[i] in ['{' ,'[' ,'(']:
                stack.append(s[i])
            elif bool(stack) and s[i] == '}' and stack[len(stack)-1] == '{': 
                stack.pop()
            elif bool(stack) and s[i] == ')' and stack[len(stack)-1] == '(': 
                stack.pop()
            elif bool(stack) and s[i] == ']' and stack[len(stack)-1] == '[': 
                stack.pop()
            else:
                return False                        
        return not bool(stack) 