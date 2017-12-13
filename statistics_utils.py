from typing import List

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