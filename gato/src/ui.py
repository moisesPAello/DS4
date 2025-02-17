import pygame
import sys
from game import Game

class UI:
    def __init__(self):
        pygame.init()
        self.game = Game()
        self.screen = pygame.display.set_mode((300, 300))
        pygame.display.set_caption("Tic-Tac-Toe")
        self.font = pygame.font.Font(None, 74)
        self.create_board()

    def create_board(self):
        self.board = [[None for _ in range(3)] for _ in range(3)]
        for row in range(3):
            for col in range(3):
                self.board[row][col] = pygame.Rect(col * 100, row * 100, 100, 100)

    def draw_board(self):
        for row in range(3):
            for col in range(3):
                pygame.draw.rect(self.screen, (255, 255, 255), self.board[row][col], 3)
                if self.game.board[row][col] == 'X':
                    self.screen.blit(self.font.render('X', True, (255, 0, 0)), (col * 100 + 25, row * 100 + 25))
                elif self.game.board[row][col] == 'O':
                    self.screen.blit(self.font.render('O', True, (0, 0, 255)), (col * 100 + 25, row * 100 + 25))

    def on_click(self, pos):
        for row in range(3):
            for col in range(3):
                if self.board[row][col].collidepoint(pos):
                    if self.game.make_move(row, col):
                        return True
        return False

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if self.on_click(event.pos):
                        winner = self.game.check_winner()
                        if winner:
                            print(f"{winner} wins!")
                            running = False
                        elif self.game.is_draw():
                            print("It's a draw!")
                            running = False

            self.screen.fill((0, 0, 0))
            self.draw_board()
            pygame.display.flip()

        pygame.quit()
        sys.exit()

"""
Este archivo es el punto de entrada a la aplicacion.
Aqui se importan las funciones de tablero.py y se ejecutan.
"""
from ui import UI

def main():
    """Funcion principal"""
    ui = UI()
    ui.run()

if __name__ == '__main__':
    main()