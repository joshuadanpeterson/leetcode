class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        flattened_matrix = [element for row in matrix for element in row]
        return target in flattened_matrix
        