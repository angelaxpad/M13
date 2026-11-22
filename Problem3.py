def print_players(players):
    print("Player Name     Batting Average")
    print("--------------------------------")

    for name, average in players.items():
        print(f"{name:<17}{average:.3f}")


players = {}

with open("batting_averages.txt", "r") as file:
    for line in file:
        name, average = line.strip().split(",")
        players[name] = float(average)

print_players(players)
