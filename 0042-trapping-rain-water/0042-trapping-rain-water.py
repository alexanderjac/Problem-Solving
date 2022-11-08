class Solution:
    def trap(self, height: List[int]) -> int:
        heights = height
            # Write your code here.
        forward = [0]
        max_element = 0
        for i  in range(len(heights)-1):
            height = heights[i]
            if height>max_element :
                max_element = height
            forward.append(max_element)
        backward = [0 for i in range(len(heights))]
        max_element = 0
        for i  in range(len(heights)-1, 0,-1):
            height = heights[i]
            if height>max_element :
                max_element = height
            backward[i]=max_element
        backward.append(0)
        result_array =[]
        for i in range(len(heights)):
            height = heights[i]
            if height<min(forward[i], backward[i]):
                result_array.append(min(forward[i], backward[i]) - height)
            else:
                result_array.append(0)
        return sum(result_array)