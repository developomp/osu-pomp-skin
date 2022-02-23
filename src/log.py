RED = "\033[91m"
GREEN = "\033[92m"
INVERSE = "\033[7m"
BOLD = "\033[1m"
END = "\033[0m"


def info(message):
    print(f"{message}{END}")


def err(message):
    print(f"{RED}{message}{END}")
