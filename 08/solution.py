
from typing import List

def spiralOrderTraversal(matrix: List[List[int]]) -> List[int]:
    top = 0
    bottom = len(matrix) - 1
    left = 0
    right = len(matrix[0]) - 1
    
    result = []
    while top <= bottom and left <= right:
        if top == bottom:
            result.extend(matrix[top][left: right + 1])
            break
        elif right == left:
            for row in matrix[top: bottom + 1]:
                result.append(row[left])
            break
            
        result.extend(matrix[top][left: right])
        for row in matrix[top: bottom]:
            result.append(row[right])
        
        result.extend(matrix[bottom][right: left: -1])
        
        for row in matrix[bottom: top: -1]:
            result.append(row[left])
            
        top += 1
        bottom -= 1
        left += 1
        right -= 1
    
    return result