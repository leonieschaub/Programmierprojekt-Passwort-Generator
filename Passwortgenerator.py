import random
import string
from dateimanagement import *

DATEI = "passwoerter.txt"

# -----------------------------------------------------
# Passwort generieren (mit einfachen Optionen)
# -----------------------------------------------------
def passwort_generieren(laenge, lower=True, upper=True, digits=True, special=True, words=False):
    zeichen = ""

    if lower:
        zeichen += string.ascii_lowercase
    if upper:
        zeichen += string.ascii_uppercase
    if digits:
        zeichen += string.digits
    if special:
        zeichen += string.punctuation

    wortliste = ["sonne", "baum", "haus", "tiger", "mond", "stern"]

    # Nur Wörter
    if words and not zeichen:
        pw = random.choice(wortliste) + random.choice(wortliste)
        return pw[:laenge]

    # Wörter + Zeichen gemischt
    if words:
        pw = random.choice(wortliste)
        while len(pw) < laenge:
            pw += random.choice(zeichen)
        return pw[:laenge]

    # Standard
    pw = ""
    for i in range(laenge):
        pw += random.choice(zeichen)
    return pw


# -----------------------------------------------------
# Passwortstärke berechnen (sehr einfache Logik)
# -----------------------------------------------------
def passwort_starke(pw):
    """Passwortstärke berechnen (sehr einfache Logik)"""
    punkte = 0

    if len(pw) >= 12:
        punkte += 1
    if any(c.islower() for c in pw):
        punkte += 1
    if any(c.isupper() for c in pw):
        punkte += 1
    if any(c.isdigit() for c in pw):
        punkte += 1
    if any(c in string.punctuation for c in pw):
        punkte += 1

    if punkte <= 2:
        return "schwach (ROT)"
    elif punkte == 3:
        return "mittel (ORANGE)"
    else:
        return "stark (GRÜN)"


# -----------------------------------------------------
# Alle anzeigen
# -----------------------------------------------------
def anzeigen():
    daten = lade_passwoerter()
    if not daten:
        print("Keine Passwörter gespeichert.\n")
        return

    print("\n--- Gespeicherte Passwörter ---")
    for nr, eintrag in enumerate(daten, start=1):
        dienst, benutzer, pw = eintrag.split(" | ")
        print(f"{nr}. {dienst} | {benutzer} | (versteckt)")
    print("-------------------------------\n")


# -----------------------------------------------------
# Eintrag auswählen
# -----------------------------------------------------
def eintrag_auswaehlen():
    daten = lade_passwoerter()
    if not daten:
        print("Keine Einträge vorhanden.")
        return None, None, None, daten

    anzeigen()
    try:
        nr = int(input("Nummer auswählen: "))
        eintrag = daten[nr - 1]
        dienst, benutzer, pw = eintrag.split(" | ")
        return dienst, benutzer, pw, daten
    except:
        print("Ungültige Auswahl.")
        return None, None, None, daten

def pruefe_jn_input(input):
    if len(input):
        print("...")
# -----------------------------------------------------
# Neues Passwort erstellen
# -----------------------------------------------------
def neues_passwort():
    dienst = input("Dienst: ")
    benutzer = input("Benutzer: ")

    print("Passwortlänge 12–15:")
    laenge = int(input("Länge: "))
    if laenge < 12 or laenge > 15:
        print("Ungültig. Standard 12 genutzt.")
        laenge = 12

    print("Zeichenauswahl (j/n):")
    lower = input("Kleinbuchstaben? (j/n): ") == "j"
    while len(lower) < 1:
        print("Fehler...")
        lower = input("Kleinbuchstaben? (j/n): ") == "j"
    # Alternative:
    pruefe_jn_input(lower)
    upper = input("Großbuchstaben? (j/n): ") == "j"
    digits = input("Zahlen? (j/n): ") == "j"
    special = input("Sonderzeichen? (j/n): ") == "j"
    words = input("Wörter verwenden? (j/n): ") == "j"

    while True:
        pw = passwort_generieren(laenge, lower, upper, digits, special, words)
        print("\nGeneriertes Passwort:", pw)
        print("Passwortstärke:", passwort_starke(pw))

        wahl = input("(s) speichern, (r) erneut generieren, (a) abbrechen: ")

        if wahl == "s":
            speichern(dienst, benutzer, pw)
            print("Gespeichert!\n")
            break
        elif wahl == "a":
            break

# -----------------------------------------------------
# Menü
# -----------------------------------------------------
def menue():
    while True:
        print("=== Passwort-Manager ===")
        print("1) Neues Passwort")
        print("2) Passwörter anzeigen")

        wahl = input("Option: ")

        if wahl == "1": neues_passwort()
        elif wahl == "2": anzeigen()
        elif wahl == "3":
            print("Tschüss!")
            break
        else:
            print("Ungültige Eingabe.\n")


menue()
