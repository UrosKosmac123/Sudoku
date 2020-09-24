from model import State

def formatError(s):
    return u"\033[1;31;40m{}\033[0;0m".format(str(s))

def formatBold(s):
    return u"\033[1;37;40m{}\033[0;0m".format(str(s))

def formatUnderline(s):
    return u"\033[4;37;40m{}\033[0;0m".format(str(s))

def formatMute(s):
    return u"\033[0;33;40m{}\033[0;0m".format(str(s))

def formatValue(val: int, locked: bool):
    if locked:
        return formatBold(val)
    else:
        return formatUnderline(val or " ")

def formatState(state: State, colors: bool = True):
    out = formatMute(u"  | 1 2 3 | 4 5 6 | 7 8 9\n")

    for x, col in enumerate(state.matrix):
        if x % 3 == 0:
            out += formatMute(u"--|-------|-------|------\n")
        out += formatMute(x + 1)
        for y, val in enumerate(col):
            if y % 3 == 0:
                out += formatMute(u" |")
            lck = state.locked[x][y]
            out += " " + formatValue(val, lck)
        out += "\n"

    return out

def parseValue(val: str):
    try:
        parsed = int(val)
    except:
        raise Exception("'{}' must be a number in range from 1 to 9.".format(val))
    if parsed not in range(1, 10):
        raise Exception("Enter a value in range from 1 to 9.")
    return parsed

if __name__ == "__main__":
    st = State(True)

    while not st.solved():
        print(formatState(st))
        try:
            y = parseValue(input("Enter column:"))
            x = parseValue(input("Enter row:"))
            v = parseValue(input("Enter value:"))
            st = st.mutate(x - 1, y - 1, v)
        except Exception as e:
            print(formatError(e))

    print(formatState(st))
    print("Congratulations.")
