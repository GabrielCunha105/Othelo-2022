from operator import length_hint


class TrapPlayer:
    def __init__(self, color):
        self.color = color

    def play(self, board):
        if(self.checkPlay(board)):
            return self.getTrapCorner(board.valid_moves(self.color))
        else:
            return self.getBackToTheWall(board.valid_moves(self.color))
        

    def checkPlay(self, board):
        trapCorners = [[3, 3], [3, 4], [3, 5], [3, 6], [6, 3], [6, 4], 
                       [6, 5], [6, 6], [4, 3], [5, 3], [4, 6], [5, 6]]
        validMoves=board.valid_moves(self.color)
        novoArray=[[m.x,m.y] for m in validMoves]
        validCorner=[m for m in trapCorners if m in novoArray ]
        return len(validCorner)>0

    def getTrapCorner(self, moves):
        import math
        trapCorners = [[3, 3], [3, 4], [3, 5], [3, 6], [6, 3], [6, 4], 
                       [6, 5], [6, 6], [4, 3], [5, 3], [4, 6], [5, 6]]
        minDist = 10
        retMove = None
        for move in moves:
            for trapCorner in trapCorners:
                distX = abs(trapCorner[0] - move.x)
                distY = abs(trapCorner[1] - move.y)
                dist = math.sqrt(distX*distX + distY*distY)
                if dist < minDist:
                    minDist = dist
                    retMove = move

        return retMove

    def getBackToTheWall(self, moves):
        import math
        backToTheWall = [[1,2], [1,3], [1,4], [1,5], [1,6], [1,7],[1,1],[1,8],
                         [2,1], [3,1], [4,1], [5,1], [6,1], [7,1],
                         [8,2], [8,3], [8,4], [8,5], [8,6], [8,7],[8,1],[8,8],
                         [2,8], [3,8], [4,8], [5,8], [6,8], [7,8]]
        minDist = 10
        retMove = None
        for move in moves:
            for b in backToTheWall:
                distX = abs(b[0] - move.x)
                distY = abs(b[1] - move.y)
                dist = math.sqrt(distX*distX + distY*distY)
                if dist < minDist:
                    minDist = dist
                    retMove = move

        return retMove