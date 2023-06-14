#!/usr/bin/python3
"""
this is all stats
"""
import sys

def print_stats(total_size, status_codes):
    """Print the computed statistics"""
    print("File size: {}".format(total_size))
    for code, count in sorted(status_codes.items()):
        print("{}: {}".format(code, count))

def parse_line(line):
    """Parse a line and extract file size and status code"""
    parts = line.split()
    if len(parts) >= 9:
        return int(parts[-1]), parts[-2]
    return 0, None

def update_stats(stats, size, code):
    """Update the statistics with new file size and status code"""
    stats['total_size'] += size
    if code:
        if code not in stats['status_codes']:
            stats['status_codes'][code] = 0
        stats['status_codes'][code] += 1

try:
    line_count = 0
    total_size = 0
    status_codes = {}
    for line in sys.stdin:
        line_count += 1
        size, code = parse_line(line.strip())
        total_size += size
        if code:
            if code not in status_codes:
                status_codes[code] = 0
            status_codes[code] += 1

        if line_count % 10 == 0:
            print_stats(total_size, status_codes)

except KeyboardInterrupt:
    print_stats(total_size, status_codes)
