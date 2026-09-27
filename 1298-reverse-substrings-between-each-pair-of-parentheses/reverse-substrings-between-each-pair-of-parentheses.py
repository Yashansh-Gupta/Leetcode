class Solution:
    def reverseParentheses(self, s: str) -> str:
        n = len(s)
        stack = []
        pair = [0] * n
        for i, char in enumerate(s):
            if char == '(':
                stack.append(i)
            elif char == ')':
                j = stack.pop()
                pair[i] = j
                pair[j] = i
        res = []
        curr_index = 0
        direction = 1
        
        while curr_index < n:
            if s[curr_index] in '()':
                curr_index = pair[curr_index]
                direction = -direction
            else:
                res.append(s[curr_index])
            curr_index += direction
            
        return "".join(res)
