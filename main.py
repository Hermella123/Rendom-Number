import random
result = []
for i in range(10):
    result.append(0)

n = 100000
xorshift_seed = 10 ** 5


def nextlcg(minValue: int, maxValue: int) -> int:
    NextRandom = random.randint(0, 10 ** 10)
    rand = (minValue + NextRandom) % (maxValue - minValue)
    return rand


def xorshift():
    global xorshift_seed
    xorshift_seed **= xorshift_seed << 13
    xorshift_seed **= xorshift_seed >> 17
    xorshift_seed **= xorshift_seed << 5

    return xorshift_seed % 10


def cal(rand):
    global result
    if rand == 0:
        i = 0
    elif rand == 1:
        i = 1
    elif rand == 2:
        i = 2
    elif rand == 3:
        i = 3
    elif rand == 4:
        i = 4
    elif rand == 5:
        i = 5
    elif rand == 6:
        i = 6
    elif rand == 7:
        i = 7
    elif rand == 8:
        i = 8
    elif rand == 9:
        i = 9
    result[i] += 1


if __name__ == "__main__":
    for i in range(n):
        rand = nextlcg(0, 10)
        cal(rand)
    for i in range(10):
        print(f"{i}: ###############################   {round((result[i] / n) * 100, 2)}%")

    for i in range(10):
        result[i] = 0

    for i in range(n):
        rand = xorshift()
        cal(rand)
    print("\n\n")
    for i in range(10):
        print(f"{i}: ###############################   {round((result[i] / n) * 100, 2)}%")
