from datei_manager import exportiere_csv

from generator import passwort_generieren, passwort_starke
from datei_manager import speichern, eintrag_auswaehlen, alle_speichern


def neues_passwort():
    applikation = input("Applikation: ")
    benutzer = input("Benutzer: ")

    laenge = int(input("Passwortlänge (12-15): "))
    if laenge < 12 or laenge > 15:
        laenge = 12

    lower = input("Kleinbuchstaben? (j/n): ") == "j"
    upper = input("Großbuchstaben? (j/n): ") == "j"
    digits = input("Zahlen? (j/n): ") == "j"
    special = input("Sonderzeichen? (j/n): ") == "j"
    words = input("Wörter verwenden? (j/n): ") == "j"

    while True:
        pw = passwort_generieren(laenge, lower, upper, digits, special, words)
        print("\nPasswort:", pw)
        print("Stärke:", passwort_starke(pw))

        wahl = input("(s) speichern, (r) neu, (a) abbrechen: ")
        if wahl == "s":
            speichern(applikation, benutzer, pw)
            break
        elif wahl == "a":
            break

def passwort_anzeigen():
    applikation, benutzer, pw, _ = eintrag_auswaehlen()
    if applikation:
        print(f"Passwort für {applikation}: {pw}")
        print("Stärke:", passwort_starke(pw))


def passwort_pruefen():
    applikation, benutzer, pw, _ = eintrag_auswaehlen()
    if not applikation:
        return

    eingabe = input("Passwort eingeben: ")
    print("OK!" if eingabe == pw else "FALSCH")


def passwort_aendern():
    applikation, benutzer, pw_alt, daten = eintrag_auswaehlen()
    if not applikation:
        return

    neues_pw = passwort_generieren(12)
    print("Neues Passwort:", neues_pw)

    neue_liste = []
    for zeile in daten:
        if zeile.startswith(applikation):
            neue_liste.append(f"{applikation} | {benutzer} | {neues_pw}")
        else:
            neue_liste.append(zeile)

    alle_speichern(neue_liste)
    print("Geändert.")


def passwort_loeschen():
    applikation, benutzer, pw, daten = eintrag_auswaehlen()
    if not applikation:
        return

    neue_liste = [z for z in daten if not z.startswith(applikation)]
    alle_speichern(neue_liste)
    print("Gelöscht.")


