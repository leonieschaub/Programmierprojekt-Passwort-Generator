# Hauptfunktionen.py
from datei_manager import speichern, eintrag_auswaehlen, alle_speichern, exportiere_csv, lade_passwoerter
from generator import passwort_generieren, passwort_starke

# NEUES PASSWORT ERSTELLEN
def neues_passwort():
    # Applikation abfragen
    while True:
        applikation = input("Applikation: ").strip()
        if applikation:
            break
        print("Fehler: Applikation darf nicht leer sein.")

    # Benutzer abfragen
    while True:
        benutzer = input("Benutzer: ").strip()
        if benutzer:
            break
        print("Fehler: Benutzer darf nicht leer sein.")

    # Passwortlänge validieren
    while True:
        try:
            laenge = int(input("Passwortlänge (12-15): "))
            if 12 <= laenge <= 15:
                break
            print("Bitte eine Zahl zwischen 12 und 15 eingeben.")
        except ValueError:
            print("Bitte eine gültige Zahl eingeben.")

    # Passwortoptionen abfragen
    def frage_option(text):
        while True:
            eingabe = input(text + " (j/n): ").lower()
            if eingabe in ("j", "n"):
                return eingabe == "j"
            print("Bitte nur 'j' oder 'n' eingeben.")

    lower = frage_option("Kleinbuchstaben?")
    upper = frage_option("Grossbuchstaben?")
    digits = frage_option("Zahlen?")
    special = frage_option("Sonderzeichen?")
    words = frage_option("Wörter verwenden?")

    # Prüfen, dass nicht alle Optionen False sind
    if not any([lower, upper, digits, special, words]):
        print("Fehler: Mindestens eine Zeichenoption muss ausgewählt werden.\n")
        return

    # Passwort generieren & Optionen anzeigen
    while True:
        pw = passwort_generieren(laenge, lower, upper, digits, special, words)
        print("\nPasswort:", pw)
        print("Stärke:", passwort_starke(pw))

        wahl = input("(s) speichern, (n) neu generieren, (a) abbrechen: ").lower()
        if wahl == "s":
            speichern(applikation, benutzer, pw)
            print("Passwort gespeichert.\n")
            break
        elif wahl == "a":
            print("Abgebrochen.\n")
            break

# PASSWORT ANZEIGEN
def passwort_anzeigen():
    applikation, benutzer, _, daten = eintrag_auswaehlen(pw_anzeigen=False)
    if not applikation or not benutzer:
        print("Fehler: Keine gültige Auswahl.\n")
        return

    # Passwort extrahieren
    pw = next((zeile.split(" | ")[2] for zeile in daten if zeile.startswith(applikation) and benutzer in zeile), None)

    if pw:
        print(f"\nPasswort für {applikation} ({benutzer}): {pw}")
        print()
    else:
        print("Passwort konnte nicht gefunden werden.\n")

# PASSWORTSTÄRKE PRÜFEN
def passwort_pruefen():
    applikation, benutzer, _, daten = eintrag_auswaehlen(pw_anzeigen=False)
    if not applikation or not benutzer:
        print("Fehler: Keine gültige Auswahl.\n")
        return

    pw = next((zeile.split(" | ")[2] for zeile in daten if zeile.startswith(applikation) and benutzer in zeile), None)

    if pw:
        print(f"\nPasswort für {applikation} ({benutzer}) hat folgende Stärke:")
        print(passwort_starke(pw))
        print()
    else:
        print("Passwort konnte nicht gefunden werden.\n")

# PASSWORT ÄNDERN
def passwort_aendern():
    applikation, benutzer, _, daten = eintrag_auswaehlen(pw_anzeigen=False)
    if not applikation or not benutzer:
        print("Fehler: Keine gültige Auswahl.\n")
        return

    neues_pw = passwort_generieren(12)
    print("Neues Passwort:", neues_pw)

    neue_liste = []
    for zeile in daten:
        app, ben, _ = zeile.split(" | ")
        if app == applikation and ben == benutzer:
            neue_liste.append(f"{app} | {ben} | {neues_pw}")
        else:
            neue_liste.append(zeile)

    alle_speichern(neue_liste)
    print("Passwort geändert.\n")

# PASSWORT LÖSCHEN
def passwort_loeschen():
    applikation, benutzer, _, daten = eintrag_auswaehlen(pw_anzeigen=False)
    if not applikation or not benutzer:
        print("Fehler: Keine gültige Auswahl.\n")
        return

    # Bestätigung j/n
    while True:
        bestaetigung = input(f"Willst du das Passwort für '{applikation}' wirklich löschen? (j/n): ").strip().lower()
        if bestaetigung == 'j':
            # Passwort löschen
            neue_liste = [z for z in daten if not (z.startswith(applikation) and benutzer in z)]
            alle_speichern(neue_liste)
            print("Das Passwort wurde gelöscht.\n")

            # Nachfragen, ob ein neues Passwort generiert werden soll
            while True:
                neu_pw = input(f"Willst du ein neues Passwort für '{applikation}' generieren? (j/n): ").strip().lower()
                if neu_pw == 'j':
                    # Neues Passwort generieren (Standardoptionen, können angepasst werden)
                    neues_pw = passwort_generieren(12)
                    speichern(applikation, benutzer, neues_pw)
                    print(f"Neues Passwort für '{applikation}': {neues_pw}\n")
                    break
                elif neu_pw == 'n':
                    print("Kein neues Passwort generiert.\n")
                    break
                else:
                    print("Ungültige Eingabe. Bitte gib 'j' für Ja oder 'n' für Nein ein.")
            break

        elif bestaetigung == 'n':
            print("Löschen abgebrochen.\n")
            break
        else:
            print("Ungültige Eingabe. Bitte gib 'j' für Ja oder 'n' für Nein ein.")

