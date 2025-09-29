import tkinter as tk
from tkinter import messagebox
import random

class TicTacToe:
    def __init__(self, master):
        self.master = master
        master.title("Tic-Tac-Toe")
        master.geometry("400x500")
        master.configure(bg="#f0f0f0")

        self.board = [""] * 9
        self.current_player = "X"
        self.game_mode = None
        self.pvc_ai_player = "O"

        self.buttons = []
        self.create_widgets()

    def create_widgets(self):
        # Frame for controls
        control_frame = tk.Frame(self.master, bg="#f0f0f0")
        control_frame.pack(pady=10)

        self.status_label = tk.Label(control_frame, text="Select Game Mode", font=("Arial", 16), bg="#f0f0f0")
        self.status_label.pack(side=tk.LEFT, padx=10)

        self.new_game_btn = tk.Button(control_frame, text="New Game", font=("Arial", 12), command=self.reset_game)
        self.new_game_btn.pack(side=tk.RIGHT, padx=10)

        # Game mode selection buttons
        mode_frame = tk.Frame(self.master, bg="#f0f0f0")
        mode_frame.pack(pady=5)

        self.pvp_btn = tk.Button(mode_frame, text="Player vs Player", font=("Arial", 12), command=lambda: self.set_game_mode("pvp"))
        self.pvp_btn.pack(side=tk.LEFT, padx=5)

        self.pvc_btn = tk.Button(mode_frame, text="Player vs Computer", font=("Arial", 12), command=lambda: self.set_game_mode("pvc"))
        self.pvc_btn.pack(side=tk.RIGHT, padx=5)

        # Game board frame
        board_frame = tk.Frame(self.master, bg="black")
        board_frame.pack(pady=10)

        for i in range(9):
            row, col = divmod(i, 3)
            button = tk.Button(board_frame, text="", font=("Arial", 36, "bold"),
                               width=4, height=2, bg="white",
                               command=lambda i=i: self.make_move(i))
            button.grid(row=row, column=col, padx=2, pady=2)
            self.buttons.append(button)

    def set_game_mode(self, mode):
        self.game_mode = mode
        self.status_label.config(text=f"{self.current_player}'s turn")
        self.reset_game()
        self.pvp_btn.config(state=tk.DISABLED)
        self.pvc_btn.config(state=tk.DISABLED)
        if self.game_mode == "pvc" and self.current_player == self.pvc_ai_player:
            self.master.after(500, self.computer_move)

    def reset_game(self):
        self.board = [""] * 9
        for button in self.buttons:
            button.config(text="", state=tk.NORMAL)
        self.current_player = "X"
        if self.game_mode:
            self.status_label.config(text=f"{self.current_player}'s turn")
        else:
            self.status_label.config(text="Select Game Mode")

    def make_move(self, index):
        if self.board[index] == "" and self.game_mode:
            self.board[index] = self.current_player
            self.buttons[index].config(text=self.current_player, state=tk.DISABLED)

            if self.check_winner(self.current_player):
                self.status_label.config(text=f"{self.current_player} wins!")
                messagebox.showinfo("Game Over", f"Player {self.current_player} wins!")
                self.disable_board()
            elif "" not in self.board:
                self.status_label.config(text="It's a draw!")
                messagebox.showinfo("Game Over", "It's a draw!")
                self.disable_board()
            else:
                self.current_player = "O" if self.current_player == "X" else "X"
                self.status_label.config(text=f"{self.current_player}'s turn")
                if self.game_mode == "pvc" and self.current_player == self.pvc_ai_player:
                    self.master.after(500, self.computer_move)

    def check_winner(self, player, board=None):
        if board is None:
            board = self.board
        winning_combinations = [
            (0, 1, 2), (3, 4, 5), (6, 7, 8),  # Rows
            (0, 3, 6), (1, 4, 7), (2, 5, 8),  # Columns
            (0, 4, 8), (2, 4, 6)              # Diagonals
        ]
        for combo in winning_combinations:
            if all(board[i] == player for i in combo):
                return True
        return False

    def get_empty_spots(self, board=None):
        if board is None:
            board = self.board
        return [i for i, spot in enumerate(board) if spot == ""]

    def minimax(self, board, depth, is_maximizing):
        if self.check_winner("X", board):
            return -10 + depth
        if self.check_winner("O", board):
            return 10 - depth
        if "" not in board:
            return 0

        if is_maximizing:
            best_score = -float('inf')
            for i in self.get_empty_spots(board):
                board[i] = "O"
                score = self.minimax(board, depth + 1, False)
                board[i] = ""
                best_score = max(score, best_score)
            return best_score
        else:
            best_score = float('inf')
            for i in self.get_empty_spots(board):
                board[i] = "X"
                score = self.minimax(board, depth + 1, True)
                board[i] = ""
                best_score = min(score, best_score)
            return best_score

    def computer_move(self):
        best_score = -float('inf')
        best_move = None
        for i in self.get_empty_spots():
            self.board[i] = self.pvc_ai_player
            score = self.minimax(self.board, 0, False)
            self.board[i] = ""
            if score > best_score:
                best_score = score
                best_move = i
        if best_move is not None:
            self.make_move(best_move)

    def disable_board(self):
        for button in self.buttons:
            button.config(state=tk.DISABLED)
        self.pvp_btn.config(state=tk.NORMAL)
        self.pvc_btn.config(state=tk.NORMAL)

def main():
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()

if __name__ == "__main__":
    main()