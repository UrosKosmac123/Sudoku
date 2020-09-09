from core import State

s = State()
s.generate()

while not s.solved():
    print(s)
    try:
        col = int(input("Izberi stolpec: ")) - 1
        row = int(input("Izberi vrstico: ")) - 1
        val = int(input("Vnesi vrednost: "))
        s = s.mutate(col, row, val)
    except Exception as e:
        print(e)
        continue;

print("Reseno")
print(s)