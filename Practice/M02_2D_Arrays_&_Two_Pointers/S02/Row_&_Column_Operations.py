'''
#leetcode : 1351
class Solution(object):
    def countNegatives(self, grid):
        rows = len(grid)
        cols = len(grid[0])
        count = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] < 0:
                    count += 1
        return count
'''
# optimal solution
class Solution(object):
    def countNegatives(self, grid):
        rows = len(grid)
        cols = len(grid[0])
        i = rows -1
        j = 0
        count = 0
        while i >= 0 and j < cols:
            if grid[i][j] < 0:
                count += cols - j
                i -= 1
            else:
                j += 1
        return count

#leetcode : 832
class Solution(object):
    def flipAndInvertImage(self, image):
        for row in image:
            row.reverse()
            for j in range(len(row)):
                row[j] = 1 - row[j]
        return image


#optimal solution
class Solution(object):
    def flipAndInvertImage(self, image):
        for row in image:
            left = 0 
            right = len(row) - 1
            while left  <= right :
                row[left], row[right] = 1-row[right], 1-row[left]
                left += 1 
                right -= 1
        return image
