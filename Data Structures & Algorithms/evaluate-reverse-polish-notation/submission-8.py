class Solution:

    def evalRPN(self, tokens: List[str]) -> int:
        ops = ["*","/","+","-"]
        stack = []
        

        for token in tokens:
            if token[0] not in ops or (len(token) > 1 and token[0] == '-'):
                stack.append(int(token))
            else:
                result = 0
                op = token
                n2 = stack.pop()
                n1 = stack.pop()

                match op:
                    case "+":
                        stack.append(n1+n2)
                    case "-":
                        stack.append(n1-n2)
                    case "*":
                        stack.append(n1*n2)
                    case "/":
                        stack.append(int(n1/n2))
        return (int(stack[0]))
                
        