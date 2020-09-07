
rowKey = "ABCDEFGHI"

def parseInt(val):
    try:
        return int(val)
    except:
        print(str(val) + " ni veljavna koordinata")
        return None

def parseRow(val):
    coor = rowKey.find(val)
    if coor < 0:
        return None
    return coor

raw = input("Naslednja poteza:\n")
spl = raw.split(" ")


rawKoordinataX = spl[0]
rawKoordinataY = spl[1]
rawVrednost = spl[2]

print(parseRow(rawKoordinataX))

