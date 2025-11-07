def create_character():
    name = input("Enter your hero's name: ")
    print("Choose your class:")
    print("1. Warrior (High Health)")
    print("2. Rogue (High Attack)")
    print("3. Mage (Balanced)")

    choice = input("> ")

    if choice == "1":
        health, attack = 100, 10
    elif choice == "2":
        health, attack = 80, 14
    elif choice == "3":
        health, attack = 90, 12

    print(f"\nWelcome, {name}! May the odds be in your favor!...\n")
    return {"name": name, "health": health, "attack": attack}

