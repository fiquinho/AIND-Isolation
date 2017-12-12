import time
import random
import datetime
from isolation import Board
from sample_players import improved_score
from game_agent import AlphaBetaPlayer, custom_score, custom_score_2, custom_score_3


# CPU agent (the opponent)
cpu_agent_AB_improved = AlphaBetaPlayer(score_fn=improved_score)

# Create global variables
DATE = datetime.datetime.now()
RESULTS = "output/1v1-results - {}-{}-{} - {}.{}hs.txt".format(DATE.day, DATE.month, DATE.year, DATE.hour, DATE.minute)
NUMBER_OF_MATCHES = 1

# Play 200 matches - AB_normal vs cpu_agent_AB_improved
AB_normal = AlphaBetaPlayer(score_fn=custom_score)

total_time = 0
total_wins = 0

for match in range(NUMBER_OF_MATCHES):
    start_match = time.time()

    game = Board(player_1=AB_normal, player_2=cpu_agent_AB_improved)

    # First move of each player is random
    for _ in range(2):
        move = random.choice(game.get_legal_moves())
        game.apply_move(move)

    winner, _, _ = game.play()

    end_match = time.time()
    match_time = end_match - start_match

    total_time += match_time

    if winner == AB_normal:
        total_wins += 1

# Print statistics
print("AB_normal vs cpu_agent_AB_improved")
print("Win rate = {}".format(total_wins / NUMBER_OF_MATCHES))
print("Average match time = {} seconds".format(total_time / NUMBER_OF_MATCHES))
print("Total elapsed time = {} minutes".format(total_time / 60))
print("----------------------------------------")

# Save statistics to results file
with open(RESULTS, "w") as output:
    output.write("AB_normal vs cpu_agent_AB_improved" + "\n")
    output.write("Win rate = {}".format(total_wins / NUMBER_OF_MATCHES) + "\n")
    output.write("Average match time = {} seconds".format(total_time / NUMBER_OF_MATCHES) + "\n")
    output.write("Total elapsed time = {} minutes".format(total_time / 60) + "\n")
    output.write("----------------------------------------" + "\n")

# Play 200 matches - AB_offensive vs cpu_agent_AB_improved
# Each time modify the offensive score by 0.1, save all the results, and the best values

offensive_value = 1.5

for i in range(11):
    offensive_test = offensive_value + (i * 0.1)

    AB_offensive = AlphaBetaPlayer(score_fn=custom_score_2)
