class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        original_color = image[sr][sc]
        if original_color == color:
            return image
        
        def dfs(row, collumn):


            if (row < 0 or row >= len(image) or collumn < 0 or collumn >= len(image[0]) or image[row][collumn] != original_color):
                return None
            
            image[row][collumn] = color

            dfs(row+1, collumn)
            dfs(row-1, collumn)
            dfs(row, collumn+1)
            dfs(row, collumn-1)

        dfs(sr, sc)
        return image