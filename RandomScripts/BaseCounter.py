import typing, time


def Main():
    print("Charset/Base, type all the characters you'll use, type 2 characters to exit:")
    final_chars = []
    stuff = True
    while stuff is True:
        tmp = input()
        if tmp != "\\n" and len(tmp) >= 2:
            stuff = False
            final_chars = list(dict.fromkeys(final_chars))
            if "\\n" in final_chars:
                final_chars[final_chars.index("\\n")] = "\n"
            print(final_chars)
            break
        final_chars.append(tmp)
    lastone = input("when adding numbers, set to 2nd value (ej: 0, 1, 10, 11 instead of 0, 1, 00, 01)? True/False (default: True) ")
    delays = input("delay (default: 0.1): ")
    last1 = True
    dlay = 0.1
    if lastone == ("True" or "False"):
        last1 = bool(lastone)
    if delays is not None and delays != " " and delays != "":
        dlay = float(delays)
    Base(lastisone=last1, delay=dlay, base=final_chars)


def Base(lastisone: typing.Optional = True, delay: typing.Optional = 0.1, base: typing.Optional = ["0", "1"]):
    def Convert(target):
        list1 = []
        list1[:0] = target
        return list1
    global string
    string = Convert(base[0])
    cur = 0
    print(base[0])
    time.sleep(delay)
    while (True):
        cur += 1
        global shouldskip
        shouldskip = False
        stringindex = len(string) - 1
        while string[stringindex] == base[-1]:
            string[stringindex] = base[0]
            if stringindex != 0:
                stringindex -= 1
            else:
                shouldskip = True
                string.insert(0, base[int(lastisone)])
                stringindex = int(lastisone)
        if shouldskip is False:
            string[stringindex] = base[base.index(string[stringindex]) + 1]
        print("".join(string))
        if cur == 2141833:
            print("Loss")
            break
        time.sleep(delay)


if __name__ == '__main__':
    Main()
