RED = "\033[91m"
GREEN = "\033[92m"
INVERSE = "\033[7m"
BOLD = "\033[1m"
END = "\033[0m"


def info(message):
    print(f"{GREEN}{BOLD}   INFO{END}{GREEN}: {message}{END}")


def err(message):
    print(f"{RED}{BOLD}  ERROR{END}{RED}: {message}{END}")
