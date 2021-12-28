import pyautogui
from Jstris.board import Board
from piece import Piece
from PIL import Image
from PIL.ImageStat import Stat

class Game:
    def __init__(self) -> None:
        self.screenshot = self.get_screenshot()
        self.board = Board()
        self.nextPieces = self.get_next_pieces(self.screenshot)
        self.currentPiece = Piece(piece_char=self.nextPieces.pop(0))
        self.heldPiece = None
        
    
    def get_next_piece_bag(self,img):
        new_pieces = []
        for i in range(5):
            piece = img.crop((242,20 + 65 * i,307, 65 + 65 * i))
            col = (Stat(piece).extrema[0][1],Stat(piece).extrema[1][1],Stat(piece).extrema[2][1])
            new_pieces += [Piece.get_piece(Piece,col)]
        return new_pieces

    def get_screenshot(self):
        return pyautogui.screenshot(region=(629,195,330,430))

    def get_next_piece(self):
        self.currentPiece = Piece(piece_char=self.nextPieces.pop(0))
        if len(self.nextPieces) == 0:
            self.nextPieces = self.get_next_piece_bag(self.get_screenshot())
    