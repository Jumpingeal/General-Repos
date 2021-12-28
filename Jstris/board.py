
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