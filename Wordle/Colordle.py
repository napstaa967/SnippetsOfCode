from colorama import init, Fore, Back, Style
import random, re, pyperclip


# Making Wordl

def Game():
    init()
    global done
    done = False
    global won
    won = False
    attempt = 0
    attempts = []
    moji_attempts = ""
    the_word = dict(zip(['1', '2', '3', '4', '5', '6'], list(pick_word())))
    while done is not True:
        if attempt == 6:
            done = True
            won = False
            break
        print(f"Attempts: {attempt}/16777216")
        if attempts is not None:
            for item in attempts:
                print(f"{item['1']}{item['2']}{item['3']}{item['4']}{item['5']}{item['6']}")
        get_next = input("\n").upper()
        if len(get_next) != 6:
            print(f"{Back.LIGHTRED_EX}Wrong Lenght{Back.RESET}")
            continue

        # UNCLE BEN WHAT HAPPENED
        # REGEX!!
        is_az = re.compile("[A-Fa-f0-9]+")
        if is_az.fullmatch(get_next) is None:
            print(f"{Back.LIGHTRED_EX}Must Be Hexadecimal{Back.RESET}")
            continue
        word_as_dict = dict(zip(['1', '2', '3', '4', '5', '6'], list(get_next)))
        temp_attempt = {}
        global valuecheck
        valuecheck = list(the_word.values())
        for i in range(6):
            if i == 0:
                valuecheck = list(the_word.values())
            if word_as_dict[str(i + 1)] in valuecheck:
                valuecheck.remove(word_as_dict[str(i + 1)])
                if word_as_dict[str(i + 1)] == the_word[str(i + 1)]:
                    moji_attempts += "🟩"
                    temp_attempt[str(i + 1)] = f"{Back.GREEN}{Fore.LIGHTWHITE_EX}{word_as_dict[str(i + 1)]}{Style.RESET_ALL}"
                else:
                    moji_attempts += "🟨"
                    temp_attempt[str(i + 1)] = f"{Back.YELLOW}{Fore.LIGHTWHITE_EX}{word_as_dict[str(i + 1)]}{Style.RESET_ALL}"
            else:
                moji_attempts += "⬛"
                temp_attempt[str(i + 1)] = f"{Back.LIGHTBLACK_EX}{Fore.LIGHTWHITE_EX}{word_as_dict[str(i + 1)]}{Style.RESET_ALL}"
            if i+1 == 6:
                moji_attempts += "\n"
                attempts.append(temp_attempt)
                if ''.join(the_word.values()) == ''.join(word_as_dict.values()):
                    done = True
                    won = True
                    break
        attempt += 1
    if done is True:
        print(f"Attempts: {attempt}/16777216")
        if attempts is not None:
            for item in attempts:
                print(f"{item['1']}{item['2']}{item['3']}{item['4']}{item['5']}{item['6']}")
        if won is False:
            print(f"{Back.RED}Major L{Back.RESET}")
        if won is True:
            print(f"{Back.GREEN}Major W{Back.RESET}")
        stuff = input("Share (Y/N): ")
        if stuff == "Y":
            pyperclip.copy(f'Colordle {attempt}/16777216\n\n{moji_attempts}')
    return


def pick_word():
    stuff = "%02X" % random.randint(0, 16777215)
    print(stuff)
    return stuff


if __name__ == '__main__':
    Game()
