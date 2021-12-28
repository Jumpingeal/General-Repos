
class Piece:
    def __init__(self,colour: tuple = None, piece_char: str = None) -> None:
        self.piece = piece_char
        if colour is not None:
            self.get_piece(colour)
        self.size = None
        #pos represents location of bottom leftmost tile of tetromino
        self.rotation = 0
        self.matrix = self._set_matrix(self.piece)
        self.pos = self._set_initial_pos(self.piece,self.rotation)
        self.initial = self.pos[0]

    
    def get_piece(self, colour: tuple):
        #if LINE piece
        if colour == (15,155,215):
            return "LN"
        #if S piece
        if colour == (89,177,1):
            return "S"
        #if BACK S piece
        if colour == (215,15,55):
            return "BS"
        #if L piece
        if colour == (227,91,2):
            return "L"
        #if BACK L piece
        if colour == (33,65,198):
            return "BL"
        #if SQUARE piece
        if colour == (227,159,2):
            return "SQ"
        #if T piece
        if colour == (175,41,138):
            return "T"
        return None
    
    def _set_matrix(self, piece: str):
        #if LINE piece
        if piece == "LN":
            self.size = 4
            return [[0,0,0,0],[1,1,1,1],[0,0,0,0],[0,0,0,0]]
        #if S piece
        if piece == "S":
            self.size = 3
            return [[0,1,1],[1,1,0],[0,0,0]]
        #if BACK S piece
        if piece == "BS":
            self.size = 3
            return [[1,1,0],[0,1,1],[0,0,0]]
        #if L piece
        if piece == "L":
            self.size = 3
            return [[0,0,1],[1,1,1],[0,0,0]]
        #if BACK L piece
        if piece == "BL":
            self.size = 3
            return [[1,0,0],[1,1,1],[0,0,0]]
        #if SQUARE piece
        if piece == "SQ":
            self.size = 2
            return [[1,1],[1,1]]
        #if T PIECE
        if piece == "T":
            self.size = 3
            return [[0,1,0],[1,1,1],[0,0,0]]
        return None

    def _set_initial_pos(self,piece,rotation):
        #if LINE piece
        if piece == "LN":
            return (3,2)
        #if S piece
        if piece == "S":
            return (3,1)
        #if BACK S piece
        if piece == "BS":
            return (3,1)
        #if L piece
        if piece == "L":
            return (3,1)
        #if BACK L piece
        if piece == "BL":
            return (3,1)
        #if SQUARE piece
        if piece == "SQ":
            return (4,0)
        #if T PIECE
        if piece == "T":
            return (3,1)
        return None
    
    def rotate_clockwise(self):
        #rotate matrix
        self.matrix = transpose(self.matrix)
        #self.height, self.width = self.width, self.height
        reverse_rows(self.matrix)

    def rotate_counter_clockwise(self):
        #rotate matrix
        reverse_rows(self.matrix)
        #self.height, self.width = self.width, self.height
        self.matrix = transpose(self.matrix)

    def _moves_to_left_wall(self):
        count = self.pos[0]
        i = 0
        while (self.matrix[0][i] != 1 and self.matrix[1][i] != 1 and self.matrix[2][i] != 1):
            i += 1
            count += 1
        return count
    
    def _moves_to_right_wall(self):
        count = 10 - self.pos[0] - self.size
        i = self.size - 1
        while (self.matrix[0][i] != 1 and self.matrix[1][i] != 1 and self.matrix[2][i] != 1):
            i -= 1
            count += 1
        return count

    def move_left(self,count=1, wall = False):
        if wall:
            self.pos = (self.pos[0] - self._moves_to_left_wall(), self.pos[1])
        elif self._moves_to_left_wall() - count >= 0:
            self.pos = (self.pos[0] - count, self.pos[1])
    
    def move_right(self,count=1, wall = False):
        if wall:
            self.pos = (self.pos[0] + self._moves_to_right_wall(), self.pos[1])
        elif self._moves_to_right_wall() - count >= 0:
            self.pos = (self.pos[0] + count, self.pos[1])

    
def transpose(matrix):
    new_matrix = [[0 for _ in range(len(matrix))] for _ in range(len(matrix[0]))]
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            new_matrix[j][i] = matrix[i][j]
    return new_matrix

def reverse_rows(matrix):
    for i in range(len(matrix)):
        matrix[i].reverse()
    #return matrix

if __name__ == "__main__":
    p = Piece(piece_char="LN")
    print(p._moves_to_right_wall())
    p.rotate_clockwise()
    print(p._moves_to_right_wall())
    p.rotate_clockwise()
    print(p._moves_to_right_wall())
    p.rotate_clockwise()
    print(p._moves_to_right_wall())
    # p.rotate_counter_clockwise()
    # for i in range(p.height):
    #     print(p.matrix[i])
    # print()
    # p.rotate_counter_clockwise()
    # for i in range(p.height):
    #     print(p.matrix[i])
    # print()
    # p.rotate_counter_clockwise()
    # for i in range(p.height):
    #     print(p.matrix[i])
    #print(transpose(m))
