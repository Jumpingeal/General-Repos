
from pyautogui import FailSafeException


class Board:
    def __init__(self) -> None:
        self.height = 20
        self.width = 10
        self.grid = [[0 for _ in range(self.width)] for _ in range(self.height)]

    def update_board(self,img):
        ran = range(0,50)
        pix = img.load()
        for i in range(20):
            for j in range(10):
                val = pix[10+j*21,10+i*22]
                #self.grid[i][j] = "□" if (val[0] in ran and val[1] in ran and val[2] in ran) else "■"
                self.grid[i][j] = 0 if (val[0] in ran and val[1] in ran and val[2] in ran) else 1

    def place_piece(self,piece,pos):
        """
        with pos being the x,y coordination of the bottom left of the bounding matrix, place piece on board, assigning a value of 1 to a location that
        the piece occupies
        """
        for y in range(0,-piece.size,-1):
            for x in range(piece.size):
                #if bounding box pos is within the board dimensions
                if (0 <= pos[1] + y <= 19) and (0 <= pos[0] + x <= 9):
                    #and if bounding box pos is part of tetris piece
                    if piece.matrix[piece.size - 1 + y][x] == 1:
                        #assign to board
                        y_pos = pos[1] + y
                        x_pos = pos[0] + x
                        self.grid[y_pos][x_pos] = 1

    def get_hard_drop_pos(self,piece):
        """
        from the current position of the piece, return the position of the bottom left of the bounding matrix such that the piece is at the further down on the board
        """
        is_at_bottom = False
        y_pos = piece.pos[1]
        for i in range(piece.size):
            has_piece_tile = False
            for j in range(piece.size):
                if piece.matrix[piece.size - 1 - i][j] == 1:
                    has_piece_tile = True
                    #if tile touching bottom of board
                    if (y_pos + 1 > 19 or self.grid[y_pos + 1][piece.pos[0]] == 1):
                        is_at_bottom = True
            if has_piece_tile:
                break
        #y_pos += 1
        while not is_at_bottom:
            y_pos += 1
            for i in range(piece.size):
                has_piece_tile = False
                for j in range(piece.size):
                    if piece.matrix[piece.size - 1 - i][j] == 1:
                        has_piece_tile = True
                        #if tile touching bottom of board
                        # if (y_pos + 1 > 19 or self.grid[y_pos + 1][piece.pos[0]] == 1):
                        if (y_pos + 1 - i > 19 or self.grid[y_pos + 1 - i][piece.pos[0] + j] == 1):
                            is_at_bottom = True
                if is_at_bottom:
                    break
            #y_pos += 1
        return (piece.pos[0],y_pos)
    
    def get_cave_count(self, piece):
        #simulate hard drop of piece, count number of tiles which are open beneath piece
        cave_count = 0
        hard_drop_pos = self.get_hard_drop_pos(piece)
        for columns in range(piece.size):
            i = 0
            while (piece.size + i >= 0 and piece.matrix[piece.size + i - 1][columns] != 1):
                i -= 1
            if  piece.size + i - 1 >= 0:
                starting_pos = hard_drop_pos[1] + i + 1
                while starting_pos <= 19:
                    if self.grid[starting_pos][hard_drop_pos[0] + columns] == 0:
                        cave_count += 1
                    starting_pos += 1
        return cave_count
    
    def clear_lines(self):
        lines_cleared = 0
        for rows in range(19,-1,-1):
            tile = 0
            while (tile < 10 and self.grid[rows][tile] != 0):
                tile += 1
            if tile >= 10:
                #add 1 to count
                lines_cleared += 1
                #pop cleared line off grid
                self.grid.pop(rows)
        for i in range(lines_cleared):
            self.grid.insert(0,[0,0,0,0,0,0,0,0,0,0])
        return lines_cleared

    def print_board(self):
        #self.grid[i][j] = "□" if (val[0] in ran and val[1] in ran and val[2] in ran) else "■"
        for i in range(20):
            for j in range(10):
                if self.grid[i][j] == 1:
                    print("■", end=" ")
                else:
                    print("□", end=" ")
            print()
        print()
                


