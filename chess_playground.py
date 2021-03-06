import numpy as np 

class Piece:
    def __init__(self, name, color,position):
        self.name = name
        self.color = color
        self.position = position

        # if name == "pawn":
        #     print("Pawn Created")
            
        #     if color == "white":
        #         self.moves = ["up"]
        #     else:
        #         self.moves = ["down"]
                
        #     self.move_type = "finite"

        # elif name == "rook":
        #     print("Rook Created")
        #     self.moves = ["up", "down", "left", "right"]
        #     self.move_type = "infinite" 

        # elif name == "bishop":
        #     print("Bishop Created")
        #     self.moves = "diagonal"
        #     self.move_type = "infinite"

        # elif name == "knight":
        #     print("Knight Created")
        #     self.moves = "hook"
        #     self.move_type = "finite" 

        # elif name == "queen":
        #     print("Queen Created")
        #     self.moves = ["up", "down", "left", "right", "diagonal"]
        #     self.move_type = "infinite"

        # else:
        #     print("King Created")
        #     self.moves = ["up", "down", "left", "right", "diagonal"]
        #     self.move_type = "finite"

class Square:
    def __init__(self, name, color,populated):
        self.name = name
        self.color = color
        self.populated = populated
        
class Board:
    def __init__(self):
        self.color_turn = "white"
        
        # Create Board
        row = ["8", "7", "6", "5", "4", "3", "2", "1"]
        col = ["a", "b", "c", "d", "e", "f", "g", "h"]

        squares = []
        color = 'white'
        
        # Loop through all possible squares 
        for rows in row:
            if color == "black":
                color = "white"
            else:
                color = "black"
            for cols in col:
                # Figure out population values
                if int(rows) <= 2 or int(rows) >= 7:
                    populated = True
                else:
                    populated = False
                print(color)
                squares.append(Square(cols+rows, color=color, populated=populated))
                if color == "black":
                    color = "white"
                else:
                    color = "black"
            print()
        self.squares = squares
        
        # Add White Pieces 
        white_pawn_a = Piece("pawn", "white", "a2")
        white_pawn_b = Piece("pawn", "white", "b2")
        white_pawn_c = Piece("pawn", "white", "c2")
        white_pawn_d = Piece("pawn", "white", "d2")
        white_pawn_e = Piece("pawn", "white", "e2")
        white_pawn_f = Piece("pawn", "white", "f2")
        white_pawn_g = Piece("pawn", "white", "g2")
        white_pawn_h = Piece("pawn", "white", "h2")
        white_king_rook = Piece("rook", "white", "a1")
        white_king_knight = Piece("knight", "white", "b1")
        white_king_bishop = Piece("bishop", "white", "c1")
        white_queen = Piece("queen", "white", "d1")
        white_king = Piece("queen", "white", "e1")
        white_queen_bishop = Piece("bishop", "white", "f1")
        white_queen_knight = Piece("knight", "white", "g1")    
        white_queen_rook = Piece("rook", "white", "h1")

        # Add Black Pieces 
        black_pawn_a = Piece("pawn", "black", "a2")
        black_pawn_b = Piece("pawn", "black", "b2")
        black_pawn_c = Piece("pawn", "black", "c2")
        black_pawn_d = Piece("pawn", "black", "d2")
        black_pawn_e = Piece("pawn", "black", "e2")
        black_pawn_f = Piece("pawn", "black", "f2")
        black_pawn_g = Piece("pawn", "black", "g2")
        black_pawn_h = Piece("pawn", "black", "h2")
        black_king_rook = Piece("rook", "black", "a1")
        black_king_knight = Piece("knight", "black", "b1")
        black_king_bishop = Piece("bishop", "black", "c1")
        black_queen = Piece("queen", "black", "d1")
        black_king = Piece("queen", "black", "e1")
        black_queen_bishop = Piece("bishop", "black", "f1")
        black_queen_knight = Piece("knight", "black", "g1")    
        black_queen_rook = Piece("rook", "black", "h1")

        self.white_pieces = [white_pawn_a, white_pawn_b, white_pawn_c, white_pawn_d, white_pawn_e, white_pawn_f, white_pawn_g, white_pawn_h, \
            white_king_rook, white_king_knight, white_king_bishop, white_queen, white_king, white_queen_bishop, white_queen_knight, white_queen_rook]
        
        self.black_pieces = [black_pawn_a, black_pawn_b, black_pawn_c, black_pawn_d, black_pawn_e, black_pawn_f, black_pawn_g, black_pawn_h, \
            black_king_rook, black_king_knight, black_king_bishop, black_queen, black_king, black_queen_bishop, black_queen_knight, black_queen_rook]

        self.round()

    def round(self):
        if self.color_turn == 'white':
            row = np.asarray(["1", "2", "3", "4", "5", "6", "7", "8"])
            col = np.asarray(["a", "b", "c", "d", "e", "f", "g", "h"])            
            self.get_moves(self.white_pieces)
        else:
            row = np.asarray(["1", "2", "3", "4", "5", "6", "7", "8"])
            col = np.asarray(["h", "g", "f", "e", "d", "c", "b", "a"]) 
            self.get_moves(self.black_pieces)

    def get_moves(self, pieces):

        for piece in pieces:
            piece_col_idx = np.where(col == piece.position[0])
            piece_row_idx = np.where(row == piece.position[1])
            
            name = piece.name
            color = piece.color 

            moves = []
            if name == "pawn":
                if color == "white":
                    pass

            elif name == "rook":
                pass 

            elif name == "bishop":
                pass

            elif name == "knight":
                pass

            elif name == "queen":
                pass
            else:
                pass               

if __name__ == "__main__":
    chessboard = Board()

    
