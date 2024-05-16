#!/usr/bin/python3
"""
module contains a script that reads stdin line by line and computes metrics
"""


import sys
import signal
import re


status_codes_count = {
    "200": 0,
    "301": 0,
    "400": 0,
    "401": 0,
    "403": 0,
    "404": 0,
    "405": 0,
    "500": 0
}
total_file_size = 0
log_pattern = re.compile(
    r'^\S+ - \[\S+ \S+\] "GET /projects/260 HTTP/1.1" (\d{3}) (\d+)$'
)
line_count = 0


def print_metrics():
    """prints of the logs"""
    """Prints the collected statistics."""
    global total_file_size, status_codes_count
    print(f"Total file size: {total_file_size}")
    for code in sorted(status_codes_count):
        if status_codes_count[code] > 0:
            print(f"{code}: {status_codes_count[code]}")


def signal_handler(sig, frame):
    """Handles the keyboard interruption signal to print statistics."""
    print_metrics()
    sys.exit(0)


if __name__ == "__main__":
    '''Read and process lines from standard input'''
    signal.signal(signal.SIGINT, signal_handler)
    for line in sys.stdin:
        match = log_pattern.match(line.strip())
        if match:
            status_code = int(match.group(1))
            file_size = int(match.group(2))

            # Update total file size and status code count
            total_file_size += file_size
            if status_code in status_codes_count:
                status_codes_count[status_code] += 1

            line_count += 1

            # Print statistics after every 10 lines
            if line_count % 10 == 0:
                print_metrics()

    print_metrics()
