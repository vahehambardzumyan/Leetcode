class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]


        for i in range(9):
            for j in range(9):

                if board[i][j] == '.':
                    continue
                
                digit = board[i][j]



                if digit in rows[i]:
                    return False
                rows[i].add(digit)



                if digit in cols[j]:
                    return False
                cols[j].add(digit)

                box_id= (i // 3) * 3 + (j // 3)
                if digit in boxes[(i // 3) * 3 + (j // 3)]:
                    return False
                boxes[box_id].add(digit)
        return True
        