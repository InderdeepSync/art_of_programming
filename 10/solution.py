
from typing import List

def trap(heights: List[int]) -> int:
        highest_left = [-float("inf")]
        highest_right = [-float("inf")]
        
        for index in range(1, len(heights)):
            temp = max(highest_left[-1], heights[index - 1])
            highest_left.append(temp)
            
        for index in reversed(range(0, len(heights) - 1)):
            highest_right.insert(0, max(heights[index + 1], highest_right[0]))
            
            
        volume = 0
        for index in range(1, len(heights) - 1):
            volume += max(min(highest_left[index], highest_right[index]) - heights[index], 0)
        
        return volume