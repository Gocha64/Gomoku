class Board:
    board_size = 15
    game_board = []

    char2num = {}

    def init_board(self, size=15):
        self.game_board = []
        self.board_size = size
        for i in range(self.board_size):
            aLine = ['*' for j in range(self.board_size)]
            self.game_board.append(aLine)

            self.char2num[chr(ord('A') + i)] = i

    def print_board(self):
        for row_num in range(self.board_size):
            print("[%2d]" % row_num, end=" ")
            print(*self.game_board[row_num], sep=" ")

        print("     ", end="")
        for col_num in range(self.board_size):
            print(chr(ord('A') + col_num), end=" ")
        print()

    def place_board(self, turn=1, row=0, col='A'):
        row = int(row)
        col = self.char2num[col]

        if self.game_board[row][col] == 'b' or self.game_board[row][col] == 'w':
            print("이미 착수된 자리 입니다")
            return False

        if turn % 2 == 1:
            self.game_board[row][col] = 'b'
        else:
            self.game_board[row][col] = 'w'
        return True

    def check_end(self, turn=1, row=0, col='A'):
        row = int(row)
        col = self.char2num[col]

        horizontal = self.game_board[row][col]
        vertical = self.game_board[row][col]
        rDiag = self.game_board[row][col]
        lDiag = self.game_board[row][col]



        for i in range(1, 5):
            negativeRow = row - i >= 0
            positiveRow = row + i < self.board_size
            negativeCol = col - i >= 0
            positiveCol = col + i < self.board_size

            if negativeRow:
                horizontal = self.game_board[row-i][col] + horizontal

            if positiveRow:
                horizontal = horizontal + self.game_board[row + i][col]

            if negativeCol:
                vertical = self.game_board[row][col - i] + vertical

            if positiveCol:
                vertical = vertical + self.game_board[row][col + i]

            if negativeRow and negativeCol:
                rDiag = self.game_board[row - i][col - i] + rDiag

            if positiveRow and positiveCol:
                rDiag = rDiag + self.game_board[row + i][col + i]

            if negativeRow and positiveCol:
                lDiag = self.game_board[row - i][col + i] + lDiag

            if positiveRow and negativeCol:
                lDiag = lDiag + self.game_board[row - i][col - i]





        # print(f'horizontal: {horizontal}')
        # print(f'vertical: {vertical}')
        # print(f'rDiag: {rDiag}')
        # print(f'lDiag: {lDiag}')


        if turn % 2 == 1:
            check = 'b' * 5
        else:
            check = 'w' * 5

        if check in horizontal or check in vertical or check in rDiag or check in lDiag:
            print("게임 종료: ", end = '')
            if turn % 2 == 1:
                print("흑의 승리입니다")
            else:
                print("백의 승리입니다")
            return True

        for line in self.game_board:
            if '*' in line:
                return False

        print("게임 종료: ", end='')
        print("무승부입니다")
        return True






if __name__ == "__main__":
    b = Board()

    b.init_board()
    # b.print_board()
    b.place_board(10, 10, 10)
    b.print_board()
    print(b.char2num['C'])
