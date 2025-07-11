import random


def placeholders(tigid: int, dorw: str):
    digit: int = tigid
    word: str = dorw
    match digit:
        case 0:
            for i in range(len(word)):
                if word[i] == " ":
                    print(" ", end="")
                elif word[i] == "-":
                    print("-", end="")
                else:
                    print("_", end="")
        case 1:
            print(f"{word[0]}", end="")
            for i in range(1, len(word)):
                if word[i] == " ":
                    print(" ", end="")
                elif word[i] == "-":
                    print("-", end="")
                else:
                    print("_", end="")


def main():
    countries: list[str] = open("countries.txt", "r", encoding="UTF-8").read().splitlines()
    capitals: list[str] = open("capitals.txt", "r", encoding="UTF-8").read().splitlines()

    print("""\x1b[38;2;255;255;255m
    \x1b[1m                   CAPITLE \x1b[0m\x1b[38;2;255;255;255m
    
    
    This game is about countries and their capitals.
    
    You will either choose the country or the capital
    to be given to you and you'll have to guess its
    corresponding pair.
    """)

    game: bool = True
    fails: int = 0
    success: int = 0
    canpi: int = 0
    nextStep: bool = True

    while nextStep:
        which = input("Which is to be given? (country/capital): ").lower()
        if "p" in which:
            canpi = 1
            nextStep = False
            print("You will be given the capital\n")
        elif "n" in which:
            canpi = 0
            nextStep = False
            print("You will be given the country\n")

    while game:
        actual_num: int = random.randint(0, len(countries))
        ans: str = ""
        curr_cnt: str = countries[actual_num]
        curr_cpt: str = capitals[actual_num]

        match canpi:
            case 0:
                print(f"What is the capital of \x1b[38;2;255;0;115m{curr_cnt}\x1b[38;2;255;255;255m?")
                placeholders(0, curr_cpt)
                ans = input("\nAnswer: ").lower()
                if ans == curr_cpt.lower():
                    print("Your answer is correct!")
                    success += 1
                else:
                    print("\nWrong! Hint: ", end="")
                    placeholders(1, curr_cpt)
                    ans = input("\nAnswer: ").lower()
                    if ans == curr_cpt.lower():
                        print("Your answer is correct!")
                        success += 1
                    else:
                        print(f"Wrong! Correct answer: \x1b[38;2;0;195;255m{curr_cpt}\x1b[38;2;255;255;255m")
                        fails += 1

            case 1:
                print(f"\x1b[38;2;255;0;115m{curr_cpt}\x1b[38;2;255;255;255m is the capital of what country?")
                ans = input("\nAnswer: ").lower()
                if ans == curr_cnt.lower():
                    print("Your answer is correct!")
                    success += 1
                else:
                    print("\nWrong! Hint: ", end="")
                    placeholders(1, curr_cnt)
                    ans = input("\nAnswer: ").lower()
                    if ans == curr_cnt.lower():
                        print("Your answer is correct!")
                        success += 1
                    else:
                        print(f"Wrong! Correct answer: \x1b[38;2;0;195;255m{curr_cnt}\x1b[38;2;255;255;255m")
                        fails += 1
        print()
        again = input("Play again?(y/n): ")
        if "y" not in again:
            game = False
        else:
            continue

    rounds = success + fails
    rate = round((success / rounds) * 100)

    print("\nThanks for playing\n")
    print("  Session score")
    print(f"Number of rounds: \x1b[38;2;195;0;255m{rounds}\x1b[38;2;255;255;255m")
    print(f"Fails: \x1b[38;2;255;0;0m{fails}\x1b[38;2;255;255;255m")
    print(f"Correct answers: \x1b[38;2;0;255;0m{success}\x1b[38;2;255;255;255m")
    print(f"Succes rate: \x1b[38;2;255;255;0m{rate}%\x1b[38;2;255;255;255m")


if __name__ == "__main__":
    main()
    input("Press enter to exit...")