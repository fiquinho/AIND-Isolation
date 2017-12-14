from typing import List


def print_simple_separator(results_file: str) -> None:
    print("----------------------------------------")

    with open(results_file, 'a') as output:
        output.write("----------------------------------------" + "\n")


def print_big_separator(results_file: str) -> None:
    print_simple_separator(results_file)

    print("########################################")

    with open(results_file, 'a') as output:
        output.write("########################################" + "\n")

    print_simple_separator(results_file)


def print_and_write_statistics(results_file: str,
                               player_names: List[str],
                               total_wins: int,
                               total_time: float,
                               number_of_matches: int,
                               offensive_value: float = None,
                               defensive_value: float = None) -> None:

    title = "{} vs {}".format(player_names[0], player_names[1])
    win_rate = "Win rate = {}".format(total_wins / number_of_matches)
    avg_match_time = "Average match time = {} seconds".format(total_time / number_of_matches)
    elapsed_time = "Total elapsed time = {} minutes".format(total_time / 60)

    offensive = "Offensive value = {}".format(offensive_value)
    defensive = "Defensive value = {}".format(defensive_value)

    print(title)

    if offensive_value is not None:
        print(offensive)
    if defensive_value is not None:
        print(defensive)

    print(win_rate)
    print(avg_match_time)
    print(elapsed_time)

    # Save statistics to results file
    with open(results_file, "a") as output:

        output.write(title + "\n")

        if offensive_value is not None:
            output.write(offensive + "\n")
        if defensive_value is not None:
            output.write(defensive + "\n")

        output.write(win_rate + "\n")
        output.write(avg_match_time + "\n")
        output.write(elapsed_time + "\n")
