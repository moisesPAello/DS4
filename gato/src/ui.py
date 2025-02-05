import tkinter as tk
from tkinter import messagebox
from game import Game

class UI:
    def __init__(self):
        self.game = Game()
        self.root = tk.Tk()
        self.root.title("Tic-Tac-Toe")
        self.buttons = {}
        self.create_board()

    def create_board(self):
        for row in range(3):
            for col in range(3):
                button = tk.Button(self.root, text="", font=("Arial", 24), width=5, height=2,
                                   command=lambda r=row, c=col: self.on_button_click(r, c))
                button.grid(row=row, column=col)
                self.buttons[(row, col)] = button

    def on_button_click(self, row, col):
        if self.game.make_move(row, col):
            self.update_board()
            winner = self.game.check_winner()
            if winner:
                messagebox.showinfo("Game Over", f"{winner} wins!")
                self.root.quit()
            elif self.game.is_draw():
                messagebox.showinfo("Game Over", "It's a draw!")
                self.root.quit()

    def update_board(self):
        for (row, col), button in self.buttons.items():
            button.config(text=self.game.board[row][col])

    def run(self):
        self.root.mainloop()