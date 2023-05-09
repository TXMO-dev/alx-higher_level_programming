#!/usr/bin/python3

print("".join(chr(c) for c in range(ord('a'), ord('z') + 1) if chr(c) not in ['q', 'e']), end="")
