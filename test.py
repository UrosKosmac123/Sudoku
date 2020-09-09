

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

#aw = input("Naslednja poteza:\n")
#spl = raw.split(" ")


#rawKoordinataX = spl[0]
#rawKoordinataY = spl[1]
#rawVrednost = spl[2]

#print(parseRow(rawKoordinataX))
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

print(f"{bcolors.WARNING}Warning: No active frommets remain. Continue?{bcolors.ENDC}")
HEADER = '\033[95m'

print(f"{HEADER}Hello{HEADER}")

string = "How are you?" 
print("\033[34m" + string + "\033[0m")

variable = 3
print ('%sI know I can be green var: %s %s' % ("\033[92m", variable,"\033[0m"))