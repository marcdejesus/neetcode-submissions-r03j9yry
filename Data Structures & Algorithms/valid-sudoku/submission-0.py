class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        row = [set() for _ in range(9)]
        col = [set() for _ in range(9)]
        box = [set() for _ in range(9)]

        for i in range(9):
            for j in range(9):
                val = board[i][j]
                current_box = (i//3) * 3 + (j//3)
                
                # Skip empty values
                if val == ".":
                    continue

                # Check duplicates
                if val in row[i]:
                    return False

                if val in col[j]:
                    return False

                if val in box[current_box]:
                    return False
                
                # Add entries
                box[current_box].add(val)
                row[i].add(val)
                col[j].add(val)

        return True

                


            