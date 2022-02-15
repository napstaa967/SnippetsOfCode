import typing, time


def Main():
    chars = input("Charset/Base (must be chars to use, not name): ")
    lastone = input("when adding numbers, set to 2nd value (ej: 0, 1, 10, 11 instead of 0, 1, 00, 01)? True/False (default: True) ")
    delays = input("delay (default: 0.1): ")
    
    if chars is None or chars == "" or chars == " ":
        raise TypeError("chars must not be null")
    chars = ''.join(sorted(set(chars), key=chars.index))
    last1 = True
    dlay = 0.1
    if lastone == ("True" or "False"):
        last1 = bool(lastone)
    if delays is not None and delays != " " and delays != "":
        dlay = float(delays)
    Base(lastisone=last1, delay=dlay, base=list(chars))


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
