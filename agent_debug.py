import timeit

from isolation import Board
from sample_players import (RandomPlayer, open_move_score,
                            improved_score, center_score)

from game_agent import (MinimaxPlayer, AlphaBetaPlayer, custom_score,
                        custom_score_2, custom_score_3)


# Create the test players
player1 = AlphaBetaPlayer(score_fn=improved_score)
player2 = RandomPlayer()

# Create an isolation board (by default 7x7)
game = Board(player1, player2)

forfeited_match = [[2, 3], [4, 4], [0, 4], [5, 6], [2, 5], [6, 4],
                   [1, 3], [4, 5], [0, 1], [2, 6], [2, 2], [3, 4],
                   [0, 3], [4, 6], [1, 5], [5, 4], [3, 6], [3, 5],
                   [2, 4], [1, 4], [3, 2], [0, 2], [4, 0], [1, 0],
                   [5, 2], [3, 1], [6, 0], [4, 3]]

# for move in forfeited_match:
#    game.apply_move(move)

# print(game.get_legal_moves())
# print(len(game.get_legal_moves()))

time_millis = lambda: 1000 * timeit.default_timer()
move_start = time_millis()
time_left = lambda: 100 - (time_millis() - move_start)

# next_move = player1.get_move(game, time_left)

# print(next_move)

failed_test_case_7 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                      0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 0, 0, 0, 0, 1,
                      1, 1, 0, 1, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 0,
                      0, 0, 1, 1, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1,
                      1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0,
                      0, 0, 0, 0, 0, 0, 0, 51, 23]

game1 = Board(player1, player2, 9, 9)
game1._board_state = failed_test_case_7

next_move = player1.get_move(game1, time_left)

print(next_move)

print(game1.get_legal_moves())

