from typing import List
import time
import random
import datetime
from isolation import Board
from sample_players import improved_score
from game_agent import AlphaBetaPlayer, custom_score, custom_score_2, custom_score_3
import statistics_utils as stats


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
NUMBER_OF_MATCHES = 1000

# Create agents to challenge cpu_agent_AB_improved
offensive_scores = [1.75, 2., 2.5, 2.75]
defensive_scores = [1., 1.5, 2.75, 3.]

# Print general data of this particular run
TITLE = """
Playing {} matches against a CPU agent using AB_improved score.
The objective of this run is to test different values of offensive 
and defensive scores.
Offensive values: {}
Defensive values: {}""".format(NUMBER_OF_MATCHES, offensive_scores, defensive_scores)

stats.print_general_statistics(RESULTS, TITLE, DATE)

# Create list with all the agents that will challenge CPU_agent
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

    offensive_score = None
    defensive_score = None

    if "Offensive" in agent_name:
        offensive_score = agent_player.offensive_score
    if "Defensive" in agent_name:
        defensive_score = agent_player.defensive_score

    # Print statistics
    stats.print_and_write_statistics(RESULTS,
                                     [agent_name, CPU_agent[0]],
                                     total_wins,
                                     total_time,
                                     NUMBER_OF_MATCHES,
                                     offensive_value=offensive_score,
                                     defensive_value=defensive_score)

    stats.print_big_separator(RESULTS)
