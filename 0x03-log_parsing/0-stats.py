#!/usr/bin/python3
"""
Module to present log parsing functionality
"""
import re
import sys


def print_stats(stats: dict, total_size: int) -> None:
    """
    Prints the statistics of the log file.

    Arguments:
        stats (dict[int, int]): A dictionary where the keys are status codes
            and the values are the number of times that status code was
            encountered.
        total_size (int): The total size of each 10 log files.
    """
    print("File size: {:d}".format(total_size))
    for key, value in sorted(stats.items()):
        if value:
            print("{}: {}".format(key, value))


if __name__ == "__main__":
    rgx_ex = (
        r"^\b(?:\d{1,2}|1\d{2}|2[0-4]\d|25[0-5])\."
        r"\b(?:\d{1,2}|1\d{2}|2[0-4]\d|25[0-5])\."
        r"\b(?:\d{1,2}|1\d{2}|2[0-4]\d|25[0-5])\."
        r"\b(?:\d{1,2}|1\d{2}|2[0-4]\d|25[0-5])\b\s-\s"
        r"\[(\d{4}-\d{2}-\d{2}\s\d{2}:\d{2}:\d{2}\.\d{6})\]\s"
        r"\"GET\s/projects/260\sHTTP\/1\.1\"\s(\d{3})\s(\d+)\s*$"
    )

    files_total_size = 0
    count = 0
    status_codes = ["200", "301", "400", "401", "403", "404", "405", "500"]
    stats = {key: 0 for key in status_codes}

    try:
        for line in sys.stdin:
            count += 1
            rgx_match = re.match(rgx_ex, line)
            if rgx_match and rgx_match.group(2) in status_codes:
                try:
                    stats[rgx_match.group(2)] += 1
                except BaseException as e:
                    pass

                try:
                    files_total_size += int(rgx_match.group(3))
                except BaseException as e:
                    pass

                if count % 10 == 0:
                    print_stats(stats, files_total_size)
        print_stats(stats, files_total_size)
    except KeyboardInterrupt:
        print_stats(stats, files_total_size)
        raise