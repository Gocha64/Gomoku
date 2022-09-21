from board import Board


class Game:
    game_board = Board()
    current_turn = 1

    def init_game(self):

        print("//    ________ ________      _____   ________   ____  __.____ ___ ",
              "//   /  _____/ \_____  \    /     \  \_____  \ |    |/ _|    |   ",
              "//  /   \  ___  /   |   \  /  \ /  \  /   |   \|      < |    |   /",
              "//  \    \_\  \/    |    \/    Y    \/    |    \    |  \|    |  / ",
              "//   \______  /\_______  /\____|__  /\_______  /____|__ \______/  ",
              "//          \/         \/         \/         \/        \/    ", sep = "\n")
        print("게임을 초기화 합니다")
        print("입력은 [줄번호] 공백 [열문자] 형식으로, ex) 7 F")

        self.game_board = Board()
        self.game_board.init_board()

        self.current_turn = 1

    def turn(self):
        print()
        self.game_board.print_board()
        print(f'{self.current_turn}번째 수')
        if self.current_turn % 2 == 1:
            print("흑이 착수할 차례입니다")
        else:
            print("백이 착수할 차례입니다")
        if self.place_gomoku():
            return True
        self.current_turn += 1

        return False

    def input_position(self):
        while True:
            try:
                row, col = input().split()

                if int(row) < 0 or int(row) >= self.game_board.board_size or \
                        ord(col) < ord('A') or ord(col) >= ord('A') + self.game_board.board_size:
                    print("잘못된 입력: 범위 초과")
                    continue

            except BaseException as e:
                print("잘못된 입력: ", e)
                continue
            break

        return row, col



    def place_gomoku(self):
        while True:
            row, col = self.input_position()
            if self.game_board.place_board(self.current_turn, row, col):
                break

        if self.game_board.check_end(self.current_turn, row, col):
            return True

        return False

    def doit(self):
        self.init_game()

        while True:
            if self.turn():
                break

        self.game_board.print_board()


if __name__ == "__main__":
    g = Game()
    g.doit()