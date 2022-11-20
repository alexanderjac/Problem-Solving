class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        hashset = {"+","-", "/","*"}
        for char in tokens:
            if char in hashset:
                second_element = stack.pop()
                first_element = stack.pop()
                if char == "+":
                    append_ele = first_element+second_element 
                elif char == "-":
                    append_ele = first_element-second_element 
                elif char == "/":
                    append_ele = int(first_element/second_element )
                elif char == "*":
                    append_ele = first_element*second_element 
                stack.append(append_ele)
            else:
                stack.append(int(char))
        return stack.pop()
            
        