from bj_class import Deck, Game
from functions import validator, bet_validator, results, exit_func, show_cards
from database import BJ_users, BJ_dashboard


def play_blackjack():
    """
    Main function that plays a round of blackjack game
    """
    game = Game()
    game.introduction()

    new_user = input("Write your name, dude: ")
    db = BJ_users(new_user)
    db.check_user()

    money = 5000
    deck = Deck()

    new_user = validator("Do you want to see rules? y/n: ")
    if new_user=='y':
        game.get_user()

    while True:
        enemy_cards, your_cards = [], []
        enemy_points, your_points = 0, 0
        new_deck = deck.get_deck()
        print(f"Cash balance is {money}\n")

        bet = bet_validator("Your bet: ", money)
        print(f"{new_user} is betting {bet}\n")

        while enemy_points <= 18 and your_points <= 21:
            enemy_cards.append(deck.get_card(new_deck))
            your_cards.append(deck.get_card(new_deck))

            res = show_cards(your_cards, enemy_cards, result="two")
            enemy_points += deck.get_card_value(res[1])
            your_points += deck.get_card_value(res[0])

            print(f"Your points: {your_points}", f"Enemy points: {enemy_points}", sep="\n")

            if enemy_points == 18 or enemy_points >= 21 or your_points >= 21:
                break

            user_input = validator("Take more? y/n: ")
            if user_input == "y":
                continue
            elif user_input == "n":
                if enemy_points <= 18:
                    while enemy_points <= 18:
                        enemy_cards.append(deck.get_card(new_deck))

                        res = show_cards(your_cards, enemy_cards, result="one")
                        enemy_points += deck.get_card_value(res[0])

                        print(f"Your points: {your_points}", f"Enemy points: {enemy_points}", sep="\n")
                elif enemy_points >= 18:
                    break

        money += results(your_points, enemy_points, bet)
        print(f"Now you have {money}")

        user_input = validator("Countinue? y/n: ")
        if user_input == "n":
            user_input = validator("Save your score? y/n: ")
            if user_input == "y":
                bjd = BJ_dashboard(name=new_user, score=money)
                bjd.add_user_score()

                user_input = validator("Do you want to see dashboard? y/n: ")
                if user_input == "y":
                    bjd.check_dashboard()

                    user_input = validator("Do you want to clear dashboard? y/n: ")
                    if user_input == "y":
                        bjd.clear_dashboard()
                    elif user_input == "n":
                        exit_func()
            elif user_input == "n":
                continue
        elif user_input == "y":
            continue


if __name__ == "__main__":
    play_blackjack()
