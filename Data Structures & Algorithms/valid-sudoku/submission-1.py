class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        ROWS = 9
        COLS = 9
        SUBSQUARE = 3

        seen_numbers = set()

        # validate rows
        for row in board:
            for number in row:
                if number in seen_numbers:
                    return False
                if number != '.':
                    seen_numbers.add(number)
            seen_numbers.clear()

        # validate columns
        #row[0][0] + row[1][0] + row[2][0].. check
        #row[1][0] ... 
        for column in range(0, COLS):
            for row in range(0, ROWS):
                number = board[row][column]
                if number in seen_numbers:
                    return False
                if number != '.':
                    seen_numbers.add(number)
            seen_numbers.clear()

        # validate squares
        square_row_offset = 0
        square_col_offset = 0

        for subsquare_number in range(0, 9):
            square_row_offset = (subsquare_number // SUBSQUARE) * 3
            square_col_offset = (subsquare_number % SUBSQUARE) * 3

            print(f"checking subsquare {subsquare_number} {square_row_offset} {square_col_offset}")

            for row in range(0, SUBSQUARE):
                for col in range(0, SUBSQUARE):
                    number = board[row + square_row_offset][col + square_col_offset]
                    print(number)
                    if number in seen_numbers:
                        return False
                    if number != '.':
                        seen_numbers.add(number)
            seen_numbers.clear()

        return True



["1","2",".",".","3",".",".",".","."],["4",".",".","5",".",".",".",".","."],[".","9","8",".",".",".",".",".","3"],["5",".",".",".","6",".",".",".","4"],[".",".",".","8",".","3",".",".","5"],["7",".",".",".","2",".",".",".","6"],[".",".",".",".",".",".","2",".","."],[".",".",".","4","1","9",".",".","8"],[".",".",".",".","8",".",".","7","9"]
