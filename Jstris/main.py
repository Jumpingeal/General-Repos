from PIL import Image
from PIL.ImageStat import Stat
import pyautogui
from piece import Piece
from board import Board
#Get whole game screen
img = pyautogui.screenshot(region=(629,195,330,430))
img.save("empty.png")
#img = Image.open("test.png")

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