def display_board(board):
    """
    Виводить поле гри на екран.
    """
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board, player):
    """
    Перевіряє, чи є переможець у гравця з символом player.
    """
    for row in board:
        if all(cell == player for cell in row):
            return True

    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True

    if all(board[i][i] == player for i in range(3)):
        return True

    if all(board[i][2 - i] == player for i in range(3)):
        return True

    return False

def get_move():
    """
    Запитує від користувача рядок та стовпець для ходу.
    """
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

def tic_tac_toe():
    """
    Головна функція гри "Хрестики-нулики".
    """
    board = [[" " for _ in range(3)] for _ in range(3)]
    players = ["X", "O"]
    current_player = 0

    display_board(board)

    for _ in range(9):
        print(f"Гравець {players[current_player]}, ваш хід.")
        row, col = get_move()

        if board[row][col] == " ":
            board[row][col] = players[current_player]
            display_board(board)

            if check_winner(board, players[current_player]):
                print(f"Гравець {players[current_player]} переміг!")
                return

            current_player = (current_player + 1) % 2
        else:
            print("Ця клітинка вже зайнята! Спробуйте ще раз.")

    print("Нічия!")

# Виклик головної функції гри для запуску
tic_tac_toe()
