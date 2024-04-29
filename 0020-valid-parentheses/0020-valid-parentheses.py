class Solution:
    def isValid(self, s: str) -> bool:
        # Dictionary to hold the mappings of the brackets
        bracket_map = {")": "(", "}": "{", "]": "["}
        # Initialize an empty stack
        stack = []
        
        # Iterate through each character in the string
        for char in s:
            if char in bracket_map:
                # Pop the top element from the stack if it's not empty, otherwise assign a dummy value
                top_element = stack.pop() if stack else '#'
                
                # Check if the popped element is the correct mapping for the current closed bracket
                if bracket_map[char] != top_element:
                    return False
            else:
                # If it's an open bracket, push it onto the stack
                stack.append(char)
        
        # If the stack is empty, all the brackets are matched correctly
        return not stack
