# leet code : 54
class Solution(object):
    def spiralOrder(self, mat):
        top = 0
        bottom = len(mat) -1
        left = 0 
        right = len(mat[0]) -1
        res = []
        while left <= right and top <= bottom:
            for j in range(left,right +1):
                res.append(mat[top][j])
            top += 1 
            for i in range(top,bottom+1):
                res.append(mat[i][right])
            right -= 1
            if top <= bottom:
                for j in range(right,left-1,-1):
                    res.append(mat[bottom][j])
                bottom -= 1
            if left <= right:
                for i in range(bottom,top-1,-1):
                    res.append(mat[i][left])
                left += 1
        return res

#leet code : 59

