#leet code : 48
class Solution(object):
    def rotate(self, matrix):
        '''
        n = len(matrix)
        for i in range(n):
            for j in range(i+1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i] , matrix[i][j]
        for row in matrix:
            row.reverse()
            '''
        matrix[:] = [list(row)[::-1] for row in zip(*matrix)]

#leetcode : 1886
