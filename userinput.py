from colorama import Fore


def ask_for_interval() -> int:
    while True:
        interval_input = input("Give time interval in seconds (default: 5): ")

        if not interval_input or interval_input is None:
            return 5

        try:
            interval = int(interval_input)
            break
        except ValueError:
            print(Fore.RED + "Invalid value. Please enter an integer\n")

    return interval


def ask_for_restart() -> bool:
    choice = input("Restart?(y/N): ")

    if choice.lower() == "y":
        return True

    return False
