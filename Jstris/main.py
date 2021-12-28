from PIL import Image
from PIL.ImageStat import Stat
import pyautogui
from piece import Piece
from board import Board
#Get whole game screen
img = pyautogui.screenshot(region=(629,195,330,430))
img.save("test.png")
#img = Image.open("test.png")

for i in range(5):
    piece = img.crop((242,20 + 65 * i,307, 65 + 65 * i))
    piece.save(f"{i}.png")
    col = (Stat(piece).extrema[0][1],Stat(piece).extrema[1][1],Stat(piece).extrema[2][1])
    #print(col)
    print(Piece.get_piece(Piece,col))

#Print board to terminal code
#"""
board = Board()
board.update_board(img)
for i in range(20):
    for j in range(10):
        print(board.grid[i][j],end=" ")
    print()
#"""


# while(True):
#     print(pyautogui.position())
#     #pyautogui.press("space")