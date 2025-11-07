from character import create_character
from enviroment import maze_path

def main():
    player = create_character()
    maze_path(player)

    #ask the player if they want to play again
    replay = input("\nDo you want to play again? (Yes/No) ").lower()
    if replay == "yes":
        main() 
    print("\nThanks for playing!")

if __name__ == "__main__":
    main()
