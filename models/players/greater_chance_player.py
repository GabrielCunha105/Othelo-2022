from models.board import Board

class GreaterChancePlayer:
    def __init__(self, color):
        self.color = color

    # Retorna um movimento
    def play(self, board):
        moves = board.valid_moves(self.color)
        best_move = moves[0]
        best_chance = 0
        moves_left = 64 - sum(board.score())

        for m in moves:
            temp_board = board.get_clone()
            temp_board.play(m, self.color)
            board_chance = self._win_chance(temp_board, (74 - moves_left))
            print("Board chance: ", board_chance) 
            if board_chance > best_chance:
                best_chance = board_chance
                best_move = m
                if best_chance == 1:
                    break

        return best_move

    # Calcula as chances de vitória de um tabuleiro `board` gerando jogos aleatórios
    # que partem dele. O número de jogos aleatórios é dado por `iterations`
    def _win_chance(self, board, iterations):
        wins = 0
        for i in range(iterations):
            winner = self._random_game(board.get_clone())
            if winner == self.color:
                wins += 1
        return wins/iterations

    import random
    
    # Gera um jogo aleatório e retorna o vencedor partindo de `board`
    def _random_game(self, board):
        players = [Board.BLACK, Board.WHITE]
        player_idx = 0
        if (self.color == Board.BLACK):
            player_idx = 1

        game_end = 0
        while (True):
            if game_end == 2:
                break

            curr_player = players[player_idx]
            valid_moves = board.valid_moves(curr_player)
            if len(valid_moves) == 0:
                game_end += 1
                continue

            game_end = 0
            board.play(self.random.choice(valid_moves), curr_player)
            player_idx = not player_idx
        
        score = board.score()
        if (score[0] > score[1]): return Board.WHITE
        elif (score[0] == score[1]): return Board.EMPTY
        else: return Board.BLACK

        
        

