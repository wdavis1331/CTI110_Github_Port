from combat import fight, boss_fight
from events import find_treasure, rest

def maze_path(player):
    rooms = ["enemy", "treasure", "enemy", "treasure", "rest", "boss"]

    for i, room in enumerate(rooms, start=1):
        print(f"\n--- Room {i} ---")

        if room == "enemy":
            if not fight(player):
                return
        elif room == "treasure":
            find_treasure(player)
        elif room == "rest":
            rest(player)
        elif room == "boss":
            if boss_fight(player):
                break
            else:
                return

    print("\nYour journey through the maze is complete!")
