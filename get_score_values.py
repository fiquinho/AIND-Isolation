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
RESULTS = "/output/1v1-results - {}-{}-{} - {}.{}hs.txt".format(DATE.day, DATE.month, DATE.year, DATE.hour, DATE.minute)
NUMBER_OF_MATCHES = 200

# Play NUMBER_OF_MATCHES matches - AB_normal vs cpu_agent_AB_improved
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
print("########################################")
print("----------------------------------------")

# Save statistics to results file
with open(RESULTS, "a") as output:
    output.write("AB_normal vs cpu_agent_AB_improved" + "\n")
    output.write("Win rate = {}".format(total_wins / NUMBER_OF_MATCHES) + "\n")
    output.write("Average match time = {} seconds".format(total_time / NUMBER_OF_MATCHES) + "\n")
    output.write("Total elapsed time = {} minutes".format(total_time / 60) + "\n")
    output.write("----------------------------------------" + "\n")
    output.write("########################################" + "\n")
    output.write("----------------------------------------" + "\n")


# Create agents with different values of offence.
# Testing 8 values, from 1 to 3, adding 0.25 each time.
# Save the value with biggest win rate.
best_win_rate = 0
best_offensive_value = 0

starting_offensive_value = 1

for i in range(10):
    offensive_value = starting_offensive_value + (i * 0.25)

    AB_offensive = AlphaBetaPlayer(score_fn=custom_score_3, offensive_value=offensive_value, defensive_value=0.5)

    # Play NUMBER_OF_MATCHES matches matches - AB_offensive vs cpu_agent_AB_improved
    total_time = 0
    total_wins = 0

    for match2 in range(NUMBER_OF_MATCHES):
        start_match = time.time()

        game = Board(player_1=AB_offensive, player_2=cpu_agent_AB_improved)

        # First move of each player is random
        for _ in range(2):
            move = random.choice(game.get_legal_moves())
            game.apply_move(move)

        winner, _, _ = game.play()

        end_match = time.time()
        match_time = end_match - start_match

        total_time += match_time

        if winner == AB_offensive:
            total_wins += 1

    win_rate = total_wins / NUMBER_OF_MATCHES

    if win_rate > best_win_rate:
        best_win_rate = win_rate
        best_offensive_value = offensive_value

    # Print statistics
    print("AB_offensive vs cpu_agent_AB_improved")
    print("Offensive value = {}".format(offensive_value))
    print("Win rate = {}".format(total_wins / NUMBER_OF_MATCHES))
    print("Average match time = {} seconds".format(total_time / NUMBER_OF_MATCHES))
    print("Total elapsed time = {} minutes".format(total_time / 60))
    print("----------------------------------------")

    # Save statistics to results file
    with open(RESULTS, "a") as output:
        output.write("AB_offensive vs cpu_agent_AB_improved" + "\n")
        output.write("Offensive value = {}".format(offensive_value) + "\n")
        output.write("Win rate = {}".format(total_wins / NUMBER_OF_MATCHES) + "\n")
        output.write("Average match time = {} seconds".format(total_time / NUMBER_OF_MATCHES) + "\n")
        output.write("Total elapsed time = {} minutes".format(total_time / 60) + "\n")
        output.write("----------------------------------------" + "\n")

print("########################################")
print("----------------------------------------")
print("Best win rate = {}".format(best_win_rate))
print("Best offensive value = {}".format(best_offensive_value))
print("----------------------------------------")
print("########################################")
print("----------------------------------------")

# Create agents with different values of defence.
# Testing 8 values, from 1 to 3, adding 0.25 each time.
# Save the value with biggest win rate.
best_win_rate = 0
best_defensive_value = 0

starting_defensive_value = 1

for i in range(10):
    defensive_value = starting_defensive_value + (i * 0.25)

    AB_defensive = AlphaBetaPlayer(score_fn=custom_score_2, offensive_value=0.5, defensive_value=defensive_value)

    # Play NUMBER_OF_MATCHES matches matches - AB_defensive vs cpu_agent_AB_improved
    total_time = 0
    total_wins = 0

    for match3 in range(NUMBER_OF_MATCHES):
        start_match = time.time()

        game = Board(player_1=AB_defensive, player_2=cpu_agent_AB_improved)

        # First move of each player is random
        for _ in range(2):
            move = random.choice(game.get_legal_moves())
            game.apply_move(move)

        winner, _, _ = game.play()

        end_match = time.time()
        match_time = end_match - start_match

        total_time += match_time

        if winner == AB_defensive:
            total_wins += 1

    win_rate = total_wins / NUMBER_OF_MATCHES

    if win_rate > best_win_rate:
        best_win_rate = win_rate
        best_defensive_value = defensive_value

    # Print statistics
    print("AB_defensive vs cpu_agent_AB_improved")
    print("Defensive value = {}".format(defensive_value))
    print("Win rate = {}".format(total_wins / NUMBER_OF_MATCHES))
    print("Average match time = {} seconds".format(total_time / NUMBER_OF_MATCHES))
    print("Total elapsed time = {} minutes".format(total_time / 60))
    print("----------------------------------------")

    # Save statistics to results file
    with open(RESULTS, "a") as output:
        output.write("AB_defensive vs cpu_agent_AB_improved" + "\n")
        output.write("Defensive value = {}".format(defensive_value) + "\n")
        output.write("Win rate = {}".format(total_wins / NUMBER_OF_MATCHES) + "\n")
        output.write("Average match time = {} seconds".format(total_time / NUMBER_OF_MATCHES) + "\n")
        output.write("Total elapsed time = {} minutes".format(total_time / 60) + "\n")
        output.write("----------------------------------------" + "\n")

print("########################################")
print("----------------------------------------")
print("Best win rate = {}".format(best_win_rate))
print("Best defensive value = {}".format(best_defensive_value))
print("----------------------------------------")
print("########################################")
print("----------------------------------------")
