
def gerade(i):
    if i % 2 == 0:
        return i
    else:
        return False

def ungerade(i):
    if i % 2 == 1:
        return i
    else:
        return False

for i in range(10):
    if gerade(i):
        print(i)
    else:
        continue

for i in range(10):
    if ungerade(i):
        print(i)
    else:
        continue