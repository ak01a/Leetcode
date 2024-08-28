class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        perimeter = 0 
        row , col = len(grid),len(grid[0])
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:
                    perimeter += 4
                    if i > 0 and grid[i-1][j] == 1:
                        perimeter -= 2
                    if j > 0 and grid[i][j-1] == 1:
                        perimeter -=2
        
        return perimeter
        '''
            def islandPerimeter(grid):
        rows = len(grid)
        cols = len(grid[0])
        perimeter = 0
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    perimeter += 4  # Assume each land cell contributes 4 to the perimeter
                    # Check the cell above
                    if i > 0 and grid[i-1][j] == 1:
                        perimeter -= 1
                    # Check the cell below
                    if i < rows - 1 and grid[i+1][j] == 1:
                        perimeter -= 1
                    # Check the cell to the left
                    if j > 0 and grid[i][j-1] == 1:
                        perimeter -= 1
                    # Check the cell to the right
                    if j < cols - 1 and grid[i][j+1] == 1:
                        perimeter -= 1
                        
        return perimeter

        '''