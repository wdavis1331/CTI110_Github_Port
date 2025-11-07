import random

def fight(player):
    enemies = ["Goblin", "Skeleton", "Orc"]
    enemy = random.choice(enemies)
    enemy_health = random.randint(30, 60)
    enemy_attack = random.randint(5, 10)

    print(f"A forsaken {enemy} appears!")

    while player["health"] > 0 and enemy_health > 0:
        print(f"\n{player['name']}: {player['health']} HP | {enemy}: {enemy_health} HP")
        move = input("Do you (A)ttack or (R)un? ").lower()

        if move == "a":
            damage = random.randint(player["attack"] - 3, player["attack"] + 3)
            enemy_health -= damage
            print(f"You hit the {enemy} for {damage} damage!")

            if enemy_health <= 0:
                print(f"You defeated the {enemy}!\n")
                return True

            enemy_damage = random.randint(enemy_attack - 2, enemy_attack + 2)
            player["health"] -= enemy_damage
            print(f"The {enemy} hits you for {enemy_damage} damage!")

        elif move == "r":
            print("You run away!")
            return True
        else:
            print("Invalid choice!")

    if player["health"] <= 0:
        print("You were defeated... Game Over!")
        return False
    return True


def boss_fight(player):
    boss = {"name": "Dragon", "health": 80, "attack": 12}
    print("\n🔥 The Dragon appears! Final battle!")

    while player["health"] > 0 and boss["health"] > 0:
        print(f"\n{player['name']}: {player['health']} HP | {boss['name']}: {boss['health']} HP")
        move = input("Do you (A)ttack or (R)un? ").lower()

        if move == "a":
            dmg = random.randint(player["attack"] - 2, player["attack"] + 2)
            boss["health"] -= dmg
            print(f"You hit the Dragon for {dmg} damage!")
            if boss["health"] <= 0:
                print("You slayed the Dragon! You win!")
                return True

            boss_dmg = random.randint(boss["attack"] - 3, boss["attack"] + 3)
            player["health"] -= boss_dmg
            print(f"The Dragon hits you for {boss_dmg} damage!")

        elif move == "r":
            print("You can’t run from the Dragon!")
        else:
            print("Invalid choice!")

    if player["health"] <= 0:
        print("The Dragon has defeated you... Game Over!")
        return False
