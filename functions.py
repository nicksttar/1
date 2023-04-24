from time import sleep
from sys import exit


def exit_func() -> None:
    """
    Function which makes system exit.
    """
    print("See you soon!")
    sleep(1)
    exit()


def validator(question: str) -> str:
    """
    Basic anti-dump validator.
    """
    user_input = input(question)
    while user_input not in ["y", "n", "q"]:
        user_input = input(question)
    if user_input == "q":
        exit_func()
    return user_input


def bet_validator(question: str, amount_money: int) -> int:
    """
    Bet anti-dump validator.
    """
    while True:
        user_input = input(question)
        if user_input == "q":
            exit_func()
        elif user_input.isdigit() and int(user_input) <= amount_money:
            return int(user_input)
        else:
            print("Bet number should be less or equal to your cash!")


def dashboard(dashboard_data: str) -> None:
    """
    Function which shows dashboard if it is available.
    """
    try:
        with open(dashboard_data) as f:
            file2 = [line.strip() for line in f.readlines()]
    except FileNotFoundError:
        print("There are no scores right now.")
    else:
        results_t = []
        for word in file2:
            temp = word.split("-")
            results_t.append([temp[0].strip(), int(temp[1].strip())])
        results = sorted(results_t, key=lambda x:x[1], reverse=True)
        for ind, num in enumerate(results, 1):
            print(f"{ind}.", " - ".join([str(n) for n in num]))


def results(user_cash: int, enemy_cash: int, bet: int) -> int:
    """
    Function which counts results of each black jack round.
    """
    if user_cash > enemy_cash and user_cash <= 21:
        return bet 
    elif user_cash > enemy_cash and user_cash > 21:
        return -bet
    elif user_cash < enemy_cash and enemy_cash <= 21:
        return -bet
    elif user_cash < enemy_cash and enemy_cash > 21 and user_cash <=21:
        return bet
    elif user_cash < enemy_cash and enemy_cash > 21 and user_cash > 21:
        return -bet
    elif user_cash == enemy_cash:
        return 0
    elif user_cash > 21 and enemy_cash > 21:
        return 0
    

def show_scores() -> None:
    """
    Function which asks user to show scores and shows dashboard.
    """
    user_input = validator("Show scores? y/n: ")
    if user_input == "y":
        dashboard("dashboard.txt")


def show_cards(your_c: list, enemy_c: list, result: str = "one") -> list:
    """
    Function which shows user's and dealer's cards.
    """
    for card_u in your_c:
        print(card_u, end=" ")
    print("\n")
    for card_e in enemy_c:
        print(card_e, end=" ")
    print("\n")

    if result == "one":
        return [card_e]
    elif result == "two":
        return [card_u, card_e]
