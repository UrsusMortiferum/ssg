import random

COLORS = [
    "\x1b[91m",
    "\x1b[92m",
    "\x1b[93m",
    "\x1b[94m",
    "\x1b[95m",
]
BOLD = "\x1b[1m"
RESET = "\x1b[0m"


def debug_helper(name, obj, should_print=True):
    color = random.choice(COLORS)
    out = f"{BOLD}{color}{name}{RESET}:\n{obj}\n"
    if should_print:
        print(out)
        return
    return out
