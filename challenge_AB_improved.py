from typing import List
import time
import random
import datetime
from isolation import Board
from sample_players import improved_score
from game_agent import AlphaBetaPlayer, custom_score, custom_score_2, custom_score_3


# TODO: Put this function in a separated file
def print_and_write_statistics(player_names: List[str],
                               wins: int,
                               elapsed_time: float,
                               number_of_matches: int) -> None:

    title = "{} vs {}".format(player_names[0], player_names[1])
    win_rate = "Win rate = {}".format(wins / NUMBER_OF_MATCHES)
    avg_match_time = "Average match time = {} seconds".format(total_time / NUMBER_OF_MATCHES)
    total

    print(title)
    print("Win rate = {}".format(total_wins / NUMBER_OF_MATCHES))
    print("Average match time = {} seconds".format(total_time / NUMBER_OF_MATCHES))
    print("Total elapsed time = {} minutes".format(total_time / 60))

    # Save statistics to results file
    with open(RESULTS, "w") as output:
        output.write("AB_normal vs cpu_agent_AB_improved" + "\n")
        output.write("Win rate = {}".format(total_wins / NUMBER_OF_MATCHES) + "\n")
        output.write("Average match time = {} seconds".format(total_time / NUMBER_OF_MATCHES) + "\n")
        output.write("Total elapsed time = {} minutes".format(total_time / 60) + "\n")
        output.write("----------------------------------------" + "\n")
        output.write("########################################" + "\n")
        output.write("----------------------------------------" + "\n")


def create_players(offensive_values: List[float] = None, defensive_values: List[float] = None) -> List[tuple]:
    players = []

    if offensive_values is not None:
        for offensive_value in offensive_values:
            player_name = "Offensive_{}".format(offensive_value)
            player_agent = AlphaBetaPlayer(score_fn=custom_score_3,
                                           offensive_value=offensive_value,
                                           defensive_value=0.5)
            players.append((player_name, player_agent))

    if defensive_values is not None:
        for defensive_value in defensive_values:
            player_name = "Defensive_{}".format(defensive_value)
            player_agent = AlphaBetaPlayer(score_fn=custom_score_2,
                                           offensive_value=0.5,
                                           defensive_value=defensive_value)
            players.append((player_name, player_agent))

    return players


# CPU agent (the opponent)
CPU_agent = ("CPU_agent", AlphaBetaPlayer(score_fn=improved_score))

# Create global variables
DATE = datetime.datetime.now()
RESULTS = "/output/1v1-results - {}-{}-{} - {}.{}hs.txt".format(DATE.day, DATE.month, DATE.year, DATE.hour, DATE.minute)
NUMBER_OF_MATCHES = 1

# Create agents to challenge cpu_agent_AB_improved
offensive_scores = [1., 2., 3.]
defensive_scores = [1., 2., 3.]

# TODO: Print general data of this particular run (DATE?, NUMBER_OF_MATCHES, offensive_scores, defensive_scores)

agent_players = create_players(offensive_scores, defensive_scores)
agent_players.append(("Normal_player", AlphaBetaPlayer(score_fn=custom_score)))

# Play NUMBER_OF_MATCHES matches for each agent, and store the results
for agent in agent_players:
    agent_name = agent[0]
    agent_player = agent[1]

    total_time = 0
    total_wins = 0

    for i in range(NUMBER_OF_MATCHES):
        start_match = time.time()

        game = Board(player_1=agent_player, player_2=CPU_agent[1])

        # First move of each player is random
        for _ in range(2):
            move = random.choice(game.get_legal_moves())
            game.apply_move(move)

        winner, _, _ = game.play()

        end_match = time.time()
        match_time = end_match - start_match

        total_time += match_time

        if winner == agent_player:
            total_wins += 1

    # Print statistics
    print("AB_normal vs cpu_agent_AB_improved")
    print("Win rate = {}".format(total_wins / NUMBER_OF_MATCHES))
    print("Average match time = {} seconds".format(total_time / NUMBER_OF_MATCHES))
    print("Total elapsed time = {} minutes".format(total_time / 60))
    print("----------------------------------------")
    print("########################################")
    print("----------------------------------------")

