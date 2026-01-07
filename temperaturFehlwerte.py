# gegeben ist eine loste von temperaturen in clesius.
# schreib ein python programm:
# - eine funktion, welcher fehlwerte aus dieser liste rausfiltert (fehlwerte zwischen -60 und +60); rückgabe: bereinigte liste und anzahl der fehlwerte
# - durchschnittstemperatur einer datenreihe berechnet und retoruniert
# die funktion so gestalten, dass sie auch mit leeren listen umgehen können
# beispiel main, dass dies sinnvoll aufruft
import sys


# Funktion 1: Fehlwerte filtern
def filter_temperature_errors(values):
    cleaned = []
    error_count = 0

    for v in values:
        if -60 <= v <= 60:
            cleaned.append(v)
        else:
            error_count += 1

    return cleaned, error_count


# Funktion 2: Durchschnittstemperatur berechnen
def average_temperature(values):
    if len(values) == 0:
        return None

    return sum(values) / len(values)


def main():
    temps = [12, 15, -100, 5, 8, 200, -5, 60, -61]

    cleaned, removed = filter_temperature_errors(temps)
    print("Bereinigte Liste:", cleaned)
    print("Entfernte Fehlwerte:", removed)

    avg = average_temperature(cleaned)
    if avg is None:
        print("Keine gültigen Temperaturen vorhanden.")
    else:
        print("Durchschnittstemperatur:", avg)

if __name__ == "__main__":
    try:
        main()
    except:
        print("Fehler")
        sys.exit(1)