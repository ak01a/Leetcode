class Solution:
    def isValid(self, s: str) -> bool:
        mapping = {'}':'{',')':'(',']':'['}
        stack = []
        for i in s:
            if i in mapping:
                ele = stack.pop() if stack else '#'
                ''' This line ensures that if the stack is empty (i.e., stack evaluates to False), 
                    instead of trying to pop from it, the variable top_element is assigned the value '#'.
                    This prevents the function from attempting to pop from an empty stack, which would indeed cause a runtime error.
                '''
                if mapping[i] != ele:
                    return False
            else:
                stack.append(i)

        return not stack 
        ''' not is a Python operator that negates the truthiness of a value.
            An empty list (which is what the stack is when all brackets are matched) is considered False in Python.
            Therefore, not stack will return True if the stack is empty (which means the string is valid) and False 
            if the stack is not empty (which means the string is invalid).
        '''