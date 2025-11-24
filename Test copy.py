import random
import string

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
# Passwort speichern
# -----------------------------------------------------
def speichern(dienst, benutzer, pw):
    with open(DATEI, "a") as f:
        f.write(f"{dienst} | {benutzer} | {pw}\n")


# -----------------------------------------------------
# Alle Passwörter laden
# -----------------------------------------------------
def lade_passwoerter():
    try:
        with open(DATEI, "r") as f:
            return [line.strip() for line in f.readlines()]
    except FileNotFoundError:
        return []


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
# Passwort prüfen
# -----------------------------------------------------
def passwort_pruefen():
    dienst, benutzer, pw, daten = eintrag_auswaehlen()
    if not dienst:
        return

    eingabe = input("Passwort eingeben: ")
    if eingabe == pw:
        print("Stimmt überein!\n")
    else:
        print("FALSCH.\n")


# -----------------------------------------------------
# Passwort anzeigen
# -----------------------------------------------------
def passwort_anzeigen():
    dienst, benutzer, pw, daten = eintrag_auswaehlen()
    if dienst:
        print(f"Passwort für {dienst}: {pw}")
        print("Stärke:", passwort_starke(pw))
        print()


# -----------------------------------------------------
# Passwort ändern
# -----------------------------------------------------
def passwort_aendern():
    dienst, benutzer, pw_alt, daten = eintrag_auswaehlen()
    if not dienst:
        return

    print("Passwort wird geändert. Generieren oder eingeben?")
    wahl = input("(g) generieren, (e) eingeben: ")

    if wahl == "e":
        neues_pw = input("Neues Passwort: ")
    else:
        neues_pw = passwort_generieren(12)

    print("Neues Passwort:", neues_pw)

    bestaetigung = input("Änderung übernehmen? (j/n): ")
    if bestaetigung != "j":
        print("Abgebrochen.")
        return

    neue_liste = []
    for zeile in daten:
        if zeile.startswith(dienst):
            neue_liste.append(f"{dienst} | {benutzer} | {neues_pw}")
        else:
            neue_liste.append(zeile)

    with open(DATEI, "w") as f:
        for z in neue_liste:
            f.write(z + "\n")

    print("Passwort geändert!\n")


# -----------------------------------------------------
# Passwort löschen
# -----------------------------------------------------
def passwort_loeschen():
    dienst, benutzer, pw, daten = eintrag_auswaehlen()
    if not dienst:
        return

    if input("Wirklich löschen? (j/n): ") != "j":
        return
    if input("Sicher? 'JA' eingeben: ") != "JA":
        print("Abgebrochen.")
        return

    neue_liste = [z for z in daten if not z.startswith(dienst)]

    with open(DATEI, "w") as f:
        for z in neue_liste:
            f.write(z + "\n")

    print("Eintrag gelöscht.\n")

    if input("Neues Passwort für diesen Dienst generieren? (j/n): ") == "j":
        neues_passwort()


# -----------------------------------------------------
# Menü
# -----------------------------------------------------
def menue():
    while True:
        print("=== Passwort-Manager ===")
        print("1) Neues Passwort")
        print("2) Passwörter anzeigen")
        print("3) Passwort anzeigen")
        print("4) Passwort prüfen")
        print("5) Passwort ändern")
        print("6) Passwort löschen")
        print("7) Beenden")

        wahl = input("Option: ")

        if wahl == "1": neues_passwort()
        elif wahl == "2": anzeigen()
        elif wahl == "3": passwort_anzeigen()
        elif wahl == "4": passwort_pruefen()
        elif wahl == "5": passwort_aendern()
        elif wahl == "6": passwort_loeschen()
        elif wahl == "7":
            print("Tschüss!")
            break
        else:
            print("Ungültige Eingabe.\n")


menue()
