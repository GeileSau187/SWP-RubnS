import random

def _getrand(n: int) -> int:
    return random.randrange(n)

random.getrand = _getrand


def ziehung_6_ohne_wdh():
    zahlen = list(range(1, 46))
    n = 45
    gezogen = []

    for _ in range(6):
        idx = random.getrand(n)
        gezogen.append(zahlen[idx])
        zahlen[idx], zahlen[n - 1] = zahlen[n - 1], zahlen[idx]
        n -= 1

    return gezogen


def statistik_update(stats: dict, gezogene_liste):
    for z in gezogene_liste:
        stats[z] += 1


def statistik_1000_ziehungen():
    stats = {i: 0 for i in range(1, 46)}
    for _ in range(1000):
        zahlen = ziehung_6_ohne_wdh()
        statistik_update(stats, zahlen)
    return stats


if __name__ == "__main__":
    einmal = ziehung_6_ohne_wdh()
    print("Ziehung (6 Zahlen):", " ".join(map(str, sorted(einmal))))

    stats = statistik_1000_ziehungen()
    print("\nStatistik nach 1000 Ziehungen (Zahl: Häufigkeit):")
    for i in range(1, 46):
        print(f"{i:2d}: {stats[i]}")
