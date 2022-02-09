from colorama import init, Fore, Back, Style
import random, re, pyperclip


# Making Wordl

def Game():
    with open(".\words.txt", "r") as words:
        wordlist = words.read().split("\n")
        init()
        global done
        done = False
        global won
        won = False
        attempt = 0
        attempts = []
        moji_attempts = ""
        the_word = dict(zip(['1', '2', '3', '4', '5'], list(pick_word())))
        while done is not True:
            if attempt == 6:
                done = True
                won = False
                break
            print(f"Attempts: {attempt}/6")
            if attempts is not None:
                for item in attempts:
                    print(f"{item['1']}{item['2']}{item['3']}{item['4']}{item['5']}")
            get_next = input("\n")
            if len(get_next) != 5:
                print(f"{Back.LIGHTRED_EX}Wrong Lenght{Back.RESET}")
                continue

            if get_next not in wordlist:
                print(f"{Back.LIGHTRED_EX}Not in Word List{Back.RESET}")
                continue

            # UNCLE BEN WHAT HAPPENED
            # REGEX!!
            is_az = re.compile("[A-Za-z]+")
            if is_az.fullmatch(get_next) is None:
                print(f"{Back.LIGHTRED_EX}Must Be A-Z a-z{Back.RESET}")
                continue
            word_as_dict = dict(zip(['1', '2', '3', '4', '5'], list(get_next)))
            temp_attempt = {}
            global valuecheck
            valuecheck = list(the_word.values())
            for i in range(5):
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
                if i+1 == 5:
                    moji_attempts += "\n"
                    attempts.append(temp_attempt)
                    if ''.join(the_word.values()) == ''.join(word_as_dict.values()):
                        done = True
                        won = True
                        break
            attempt += 1
        if done is True:
            print(f"Attempts: {attempt}/6")
            if attempts is not None:
                for item in attempts:

                    print(f"{item['1']}{item['2']}{item['3']}{item['4']}{item['5']}")
            if won is False:
                print(f"{Back.RED}Major L{Back.RESET}")
            if won is True:
                print(f"{Back.GREEN}Major W{Back.RESET}")
            stuff = input("Share (Y/N): ")
            if stuff.upper() == "Y":
                pyperclip.copy(f'KWordle {attempt}/6\n\n{moji_attempts}')
        return


def pick_word():
    with open(".\words.txt", "r") as words:
        wordsp2 = words.read().split("\n")
        print(f"dictionary: {wordsp2}")
        stuff = random.choice(wordsp2)
        print(stuff)
    return stuff


if __name__ == '__main__':
    Game()
