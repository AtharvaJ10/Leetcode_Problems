class Solution:
    def calculate(self, s: str) -> int:
        """def operate(op, left, right):
            if op=='+':
                return left+right
            elif op=='-':
                return left-right
            elif op=='*':
                return left*right
            elif op=='/':
                return int(left/right)
        
        def compute():
            right = nums.pop()
            left = nums.pop()
            op = ops.pop()
            nums.append(operate(op, left, right))
            
        ops, nums, i = [], [],0
        while i<len(s):
            if s[i].isdigit():
                tmp = 0
                while i<len(s) and s[i].isdigit():
                    tmp = tmp*10 + int(s[i])
                    i+=1
                nums.append(tmp)
                continue
            elif s[i] in ['+', '-']:
                while ops and ops[-1] in ['+','-','*','/']:
                    compute()
                ops.append(s[i])
            elif s[i] in ['*', '/']:
                while ops and ops[-1] in ['*','/']:
                    compute()
                ops.append(s[i])
            i+=1
        while ops:
            compute()
        return nums[0]"""
        
        num = 0
        res = 0
        pre_op = '+'
        s+='+'
        stack = []
        for c in s:
            if c.isdigit():
                num = num*10 + int(c)
            elif c == ' ':
                    pass
            else:
                if pre_op == '+':
                    stack.append(num)
                elif pre_op == '-':
                    stack.append(-num)
                elif pre_op == '*':
                    operant = stack.pop()
                    stack.append((operant*num))
                elif pre_op == '/':
                    operant = stack.pop()
                    stack.append(math.trunc(operant/num))
                num = 0
                pre_op = c
        return sum(stack)
            