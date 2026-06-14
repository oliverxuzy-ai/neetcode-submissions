class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set) # if nums[r][c] in nums[r] 
        cols = defaultdict(set) # if nums[r][c] in nums[:][c]
        boxes = defaultdict(set) # (r // 3, c // 3)

        for r in range(9):
            for c in range(9):

                val = board[r][c]
                box = (r // 3, c // 3)

                if val == '.':
                    continue
                
                if val in rows[r] or val in cols[c] or val in boxes[box]:
                    return False

                rows[r].add(val)
                cols[c].add(val)
                boxes[box].add(val)


        
        return True


