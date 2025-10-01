import random

def ziehung():
    zahlen = list(range(1, 46))
    n, gezogen = 45, []
    for _ in range(6):
        idx = random.getrand(n)
        gezogen.append(zahlen[idx])
        zahlen[idx], zahlen[n-1] = zahlen[n-1], zahlen[idx]
        n -= 1
    return gezogen

def statistik(anzahl=1000):
    stats = {i: 0 for i in range(1, 46)}
    for _ in range(anzahl):
        for z in ziehung():
            stats[z] += 1
    return stats

if __name__ == "__main__":
    random.getrand = lambda n: random.randrange(n)

    einmal = ziehung()
    print("Ziehung (6 Zahlen):", " ".join(map(str, sorted(einmal))))

    stats = statistik()
    print("\nStatistik nach 1000 Ziehungen:")
    for i in range(1, 46):
        print(f"{i:2d}: {stats[i]}")
