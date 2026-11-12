def is_win(game):
    # rows & columns
    for idx in range(3):
        if game[idx][0] == game[idx][1] == game[idx][2] and game[idx][0] != '.':
            return True
        if game[0][idx] == game[1][idx] == game[2][idx] and game[0][idx] != '.':
            return True
    # diagonals
    if game[0][0] == game[1][1] == game[2][2] and game[0][0] != '.':
        return True
    if game[0][2] == game[1][1] == game[2][0] and game[0][2] != '.':
        return True
    return False


def print_board(game):
    for row in game:
        print(" ".join(row))


def main():
    game = [['.' for _ in range(3)] for _ in range(3)]
    player1 = 'X'
    player2 = 'O'
    is_player1_turn = True

    print("X = Player 1")
    print("O = Player 2")

    for _ in range(9):
        while True:
            if is_player1_turn:
                print("Player 1: ", end="")
            else:
                print("Player 2: ", end="")

            print("Which cell to mark? i:[1..3], j:[1..3]: ", end="")
            try:
                i, j = map(int, input().split())
                i, j = i - 1, j - 1  # Convert 1-based input to 0-based index
                if not (0 <= i < 3 and 0 <= j < 3):
                    print("Out of range! Please enter numbers between 1 and 3.")
                    continue
                if game[i][j] != '.':
                    print("Cell already taken! Choose another cell.")
                    continue
                break
            except ValueError:
                print("Invalid input! Please enter two integers.")

        game[i][j] = player1 if is_player1_turn else player2

        if is_win(game):
            print("Win!")
            print_board(game)
            return  # Exit immediately so it won't print "Tie!" on the 9th move

        is_player1_turn = not is_player1_turn

    print("Tie!")
    print_board(game)


if __name__ == "__main__":
    main()
