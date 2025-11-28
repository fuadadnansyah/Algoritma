# ===============================
#   TIC TAC TOE by Fuad Adnansyah
#   Beda dari temanmu (AMAN)
#   Player 1: Fuad
#   Player 2: Viardan
# ===============================

def show_board(board):
    print("\n   0   1   2")
    print("  -----------")
    for i, row in enumerate(board):
        print(i, "|", " | ".join(row), "|")
    print("  -----------\n")

def check_win(board, mark):
    win_cond = [
        [board[0][0], board[0][1], board[0][2]],
        [board[1][0], board[1][1], board[1][2]],
        [board[2][0], board[2][1], board[2][2]],
        [board[0][0], board[1][0], board[2][0]],
        [board[0][1], board[1][1], board[2][1]],
        [board[0][2], board[1][2], board[2][2]],
        [board[0][0], board[1][1], board[2][2]],
        [board[0][2], board[1][1], board[2][0]]
    ]
    return [mark, mark, mark] in win_cond

def main():
    board = [[" "]*3 for _ in range(3)]
    player_turn = "X"  # X = Fuad, O = Viardan

    print("======================================")
    print("       TIC-TAC-TOE  (3x3)")
    print("  Player 1: Fuad      (X)")
    print("  Player 2: Viardan   (O)")
    print("======================================")

    while True:
        show_board(board)
        print(f"Giliran {'Fuad' if player_turn=='X' else 'Viardan'}")

        try:
            row = int(input("Masukkan baris (0-2): "))
            col = int(input("Masukkan kolom (0-2): "))

            if board[row][col] != " ":
                print("Posisi sudah terisi! Coba lagi.\n")
                continue

            board[row][col] = player_turn

            if check_win(board, player_turn):
                show_board(board)
                print(f"🎉 Pemain {'Fuad' if player_turn=='X' else 'Viardan'} MENANG! 🎉")
                break

            if all(" " not in x for x in board):
                show_board(board)
                print("🤝 Hasilnya SERI!")
                break

            player_turn = "O" if player_turn == "X" else "X"

        except:
            print("Input harus angka 0 sampai 2!\n")

if __name__ == "__main__":
    main()
