# ==================== Recomendação de Jogo ====================
def main():
    difficulty = input("Difficult or Casual? ").capitalize()
    if difficulty not in ("Difficult", "Casual"):
        print("Enter a valid difficulty")
        return

    players = input("Multiplayer or Single-player? ").capitalize()
    if players not in ("Multiplayer", "Single-player"):
        print("Enter a valid number of players")
        return

    if difficulty == "Difficult" and players == "Multiplayer":
        recommend("Poker")
    elif difficulty == "Difficult" and players == "Single-player":
        recommend("Klondike")
    elif difficulty == "Casual" and players == "Multiplayer":
        recommend("Hearts")
    elif difficulty == "Casual" and players == "Single-player":
        recommend("Clock")


def recommend(game):
    print("You might like", game)


main()
