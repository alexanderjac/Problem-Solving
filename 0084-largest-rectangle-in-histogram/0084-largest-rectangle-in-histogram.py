class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        res = float("-inf")
        area =0
        for idx, height in enumerate(heights):  
            i = idx
            while stack and stack[-1][1] >height:
                i, curr = stack.pop(-1)
                area = max(area, curr*(idx-i))
            print(height, area)
            stack.append((i, height))
        idx = len(heights)-1
        while stack:
            i, height = stack.pop(-1)
            area = max(area, height*(idx-i+1))
        return area
            
                
            