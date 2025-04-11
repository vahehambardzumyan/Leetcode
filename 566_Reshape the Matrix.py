class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])

        if m * n != r * c:
            return mat

        flat = [mat[i][j] for i in range(m) for j in range(n)]
        result = [[0] * c for _ in range(r)]

        for k in range(m * n):
            result[k // c][k % c] = flat[k] 

        return result



        