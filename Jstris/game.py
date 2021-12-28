import pyautogui
from board import Board
from piece import Piece
from PIL import Image
from PIL.ImageStat import Stat
import time

class Game:
    def __init__(self,img = None) -> None:
        if img is None:
            self.screenshot = self.get_screenshot()
        else:
            self.screenshot = img
        self.board = Board()
        #self.board.update_board(self.screenshot)
        self.nextPieces = self.get_next_piece_bag(self.screenshot)
        self.currentPiece = Piece(piece_char=self.nextPieces.pop(0))
        self.heldPiece = None
        
    def get_next_piece_bag(self,img):
        new_pieces = []
        for i in range(5):
            piece = img.crop((242,20 + 65 * i,307, 65 + 65 * i))
            col = (Stat(piece).extrema[0][1],Stat(piece).extrema[1][1],Stat(piece).extrema[2][1])
            new_pieces += [Piece.get_piece(Piece,col)]
        return new_pieces

    def get_next_piece(self):
        self.currentPiece = Piece(piece_char=self.nextPieces.pop(0))
        if len(self.nextPieces) == 0:
            self.nextPieces = self.get_next_piece_bag(self.get_screenshot())
    
    def get_screenshot(self):
        return pyautogui.screenshot(region=(629,195,330,430))

    def get_score():
        #takes current piece, hard drops it, and calculates score
        pass
    
    def place(self,rotation):
        if rotation == 1:
            pyautogui.press('up')
        elif rotation == 2:
            pyautogui.press('up')
            pyautogui.press('up')
        elif rotation == 3:
            pyautogui.press('z')
        x_pos = self.currentPiece.pos[0]
        count = abs(x_pos - self.currentPiece.initial)
        #if we have to move left
        if x_pos < self.currentPiece.initial:
            for _ in range(count):
                #time.sleep(0.5)
                pyautogui.press('left')
        #if we have to move right
        elif x_pos > self.currentPiece.initial:
            for _ in range(count):
                #time.sleep(0.5)
                pyautogui.press('right')
        pyautogui.press('space')
        self.board.place_piece(self.currentPiece,self.board.get_hard_drop_pos(self.currentPiece))


if __name__ == "__main__":
    
    time.sleep(2)
    pyautogui.press("f4")
    game = Game( )
    print(game.currentPiece.piece,game.nextPieces)
    #game.currentPiece = Piece(piece_char="S")
    time.sleep(2)
    for _ in range(20):
        #for all rotations
        rotations = 0
        game.currentPiece.rotate_counter_clockwise()
        for rotations in range(4):
            game.currentPiece.rotate_clockwise()
            #Calculate best move
            #print(game.currentPiece.pos)
            game.currentPiece.move_left(wall=True)
            #print(game.currentPiece.pos)
            while (game.currentPiece._moves_to_right_wall() > 0 and game.board.get_cave_count(game.currentPiece) > 0):
                game.currentPiece.move_right()
            if game.board.get_cave_count(game.currentPiece) == 0:
                break
            #game.currentPiece.move_left(4)
             
        game.place(rotations)
        game.board.clear_lines()
        game.board.print_board()
        print(rotations)
        #time.sleep(2)

        #move piece

        #update new piece
        game.get_next_piece()
    
    #game.place(7)
    #game.board.print_board()
    
    
    # game = Game()
    # #game.board.update_board()
    # game.board.grid = [[0,0,0,0,0,0,0,0,0,0],
    # [0,0,0,0,0,0,0,0,0,0],
    # [0,0,0,0,0,0,0,0,0,0],
    # [0,0,0,0,0,0,0,0,0,0],
    # [0,0,0,0,0,0,0,0,0,0],
    # [0,0,0,0,0,0,0,0,0,0],
    # [0,0,0,0,0,0,0,0,0,0],
    # [0,0,0,0,0,0,0,0,0,0],
    # [0,0,0,0,0,0,0,0,0,0],
    # [0,0,0,0,0,0,0,0,0,0],
    # [0,0,0,0,0,0,0,0,0,0],
    # [0,0,0,0,0,0,0,0,0,0],
    # [0,0,0,0,0,0,0,0,0,0],
    # [0,0,0,0,0,0,0,0,0,0],
    # [0,0,0,0,0,0,0,0,0,0],
    # [0,0,0,0,0,0,0,0,0,0],
    # [0,0,0,0,0,0,0,0,0,0],
    # [0,0,1,0,0,0,0,0,0,0],
    # [1,1,1,1,0,1,0,0,0,0],
    # [1,1,1,1,1,1,0,0,0,0]]
    # game.board.print_board()
    # game.currentPiece = Piece(piece_char="BS")
    # game.currentPiece.move_right(2)
    # print(game.board.get_hard_drop_pos(game.currentPiece))
    # game.board.place_piece(game.currentPiece,game.board.get_hard_drop_pos(game.currentPiece))
    # game.board.print_board()

    # game.currentPiece.rotate_clockwise()
    # game.currentPiece.move_right(wall=True)
    # game.board.place_piece(game.currentPiece,game.board.get_hard_drop_pos(game.currentPiece))

    # print(game.board.get_hard_drop_pos(game.currentPiece))
    # game.board.place_piece(game.currentPiece,game.board.get_hard_drop_pos(game.currentPiece))
    # game.get_next_piece()
    # game.currentPiece = Piece(piece_char="LN")
    # #game.currentPiece.rotate_counter_clockwise()
    # game.currentPiece.move_right(1)
    # print(game.board.get_cave_count(game.currentPiece))
    # game.board.place_piece(game.currentPiece,game.board.get_hard_drop_pos(game.currentPiece))
    # print(game.currentPiece.piece)
    # print(game.board.get_hard_drop_pos(game.currentPiece))
    # game.board.print_board()
    # print()
    # game.currentPiece.pos = (game.currentPiece.pos[0],game.currentPiece.pos[1])

    # game.currentPiece.pos = (game.currentPiece.pos[0] + 3,game.currentPiece.pos[1])
    # game.get_next_piece()
    # print(game.currentPiece.piece)
    # print(game.nextPieces)
    # print(game.currentPiece.pos)
    