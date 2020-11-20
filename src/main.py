# Forked from https://github.com/mrgretwon/fut_sniping_bot.git

from bot import Bot
from config import USER, PLAYER, LOGIN_MANUALLY


bot = Bot()


def init(auto):
    print(f"#########\n"
          f"|WELCOME|\n"
          f"#########")

    # Buy player
    if auto:
        # Login
        if LOGIN_MANUALLY:
            bot.login_manually("playstationgame245@gmail.com", "Children1")
        else:
            bot.login(USER)

        bot.buy_player(PLAYER["name"], PLAYER["cost"])
    else:
        player_name = input("Enter the player's name: ")
        player_cost = int(input("What is the max price for the player: "))

        # Login
        if LOGIN_MANUALLY:
            bot.login_manually("playstationgame245@gmail.com", "Children1")
        else:
            bot.login(USER)

        bot.buy_player(player_name, player_cost)


init(False)
