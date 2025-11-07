import random
#Give the player a chance to find treasure
def find_treasure(player):
    print("You found a treasure chest!")
    reward = random.choice(["sword", "potion"])
    if reward == "sword":
        player["sword"] += 2
        print("You found a sharper sword! +2 Attack.")
    else:
        player["potion"] += 15
        print("You found a healing potion! +15 HP.")

#Give the player a chance to rest and recover health
def rest(player):
    heal = random.randint(10, 20)
    player["health"] += heal
    print(f"You take a rest and recover {heal} HP.")
