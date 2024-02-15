class TicTacToe:
    def __init__(self):
        self.board = [[" " for _ in range(3)] for _ in range(3)]
        self.current_player = "X"

    def display_board(self):
        for row in self.board:
            print(" | ".join(row))
            print("-" * 9)

    def make_move(self, row, col):
        if self.board[row][col] == " ":
            self.board[row][col] = self.current_player
            self.current_player = "O" if self.current_player == "X" else "X"
        else:
            print("Ця клітинка вже зайнята! Спробуйте ще раз.")

    def check_winner(self):
        for row in self.board:
            if all(cell == self.current_player for cell in row):
                return True

        for col in range(3):
            if all(self.board[row][col] == self.current_player for row in range(3)):
                return True

        if all(self.board[i][i] == self.current_player for i in range(3)):
            return True

        if all(self.board[i][2 - i] == self.current_player for i in range(3)):
            return True

        return False

    def is_board_full(self):
        for row in self.board:
            if " " in row:
                return False
        return True

    def play_game(self):
        while not self.check_winner() and not self.is_board_full():
            self.display_board()
            print(f"Гравець {self.current_player}, ваш хід.")
            row, col = self.get_move()
            self.make_move(row, col)

        self.display_board()
        if self.check_winner():
            print(f"Гравець {self.current_player} переміг!")
        else:
            print("Нічия!")

    def get_move(self):
        while True:
            try:
                row = int(input("Введіть номер рядка (1-3): ")) - 1
                col = int(input("Введіть номер стовпця (1-3): ")) - 1
                if 0 <= row < 3 and 0 <= col < 3:
                    return row, col
                else:
                    print("Невірні координати! Спробуйте ще раз.")
            except ValueError:
                print("Невірний формат! Введіть числа від 1 до 3.")

# Використання класу для гри
game = TicTacToe()
game.play_game()
