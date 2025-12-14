# NEUES PASSWORT ERSTELLEN
    
#Erstellt ein neues Passwort für eine Applikation und speichert es.
#Ablauf:
#   - Benutzer gibt Applikation und Benutzername ein.
#   - Benutzer wählt Passwortlänge und Zeichenoptionen.
#   - Passwort wird generiert und angezeigt.
#   - Benutzer kann Passwort speichern, neu generieren oder abbrechen.
    
 # Import der benötigten Funktionen
from datei_manager import speichern, eintrag_auswaehlen, alle_speichern, exportiere_csv, lade_passwoerter
from generator import passwort_generieren, passwort_starke


# NEUES PASSWORT ERSTELLEN
def neues_passwort():
    # Applikation abfragen, darf nicht leer sein
    while True:
        applikation = input("Applikation: ").strip()
        if applikation:
            break
        print("Fehler: Applikation darf nicht leer sein.")

    # Benutzer abfragen, darf nicht leer sein
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
            else:
                print("Bitte eine Zahl zwischen 12 und 15 eingeben.")
        except ValueError:
            print("Bitte eine gültige Zahl eingeben.")

    # Passwortoptionen
    while True:
        lower_input = input("Kleinbuchstaben? (j/n): ").lower()
        if lower_input in ("j", "n"):
            lower = lower_input == "j"
            break
        print("Bitte nur 'j' oder 'n' eingeben.")

    while True:
        upper_input = input("Grossbuchstaben? (j/n): ").lower()
        if upper_input in ("j", "n"):
            upper = upper_input == "j"
            break
        print("Bitte nur 'j' oder 'n' eingeben.")

    while True:
        digits_input = input("Zahlen? (j/n): ").lower()
        if digits_input in ("j", "n"):
            digits = digits_input == "j"
            break
        print("Bitte nur 'j' oder 'n' eingeben.")

    while True:
        special_input = input("Sonderzeichen? (j/n): ").lower()
        if special_input in ("j", "n"):
            special = special_input == "j"
            break
        print("Bitte nur 'j' oder 'n' eingeben.")

    while True:
        words_input = input("Wörter verwenden? (j/n): ").lower()
        if words_input in ("j", "n"):
            words = words_input == "j"
            break
        print("Bitte nur 'j' oder 'n' eingeben.")

    # Passwort generieren & wiederholen
    while True:
        pw = passwort_generieren(laenge, lower, upper, digits, special, words)
        print("\nPasswort:", pw)
        print("Stärke:", passwort_starke(pw))

        wahl = input("(s) speichern, (n) neu generieren, (a) abbrechen: ").lower()

        if wahl == "s":
            speichern(applikation, benutzer, pw)
            print("Passwort gespeichert.\n")
            return
        elif wahl == "a":
            print("Abgebrochen.\n")
            return


# Passwort generieren & wiederholen
    while True:
        pw = passwort_generieren(laenge, lower, upper, digits, special, words)
        print("\nPasswort:", pw)
        print("Stärke:", passwort_starke(pw))

        wahl = input("(s) speichern, (r) neu generieren, (a) abbrechen: ").lower()

        if wahl == "s":
            speichern(applikation, benutzer, pw)
            print("Gespeichert.\n")
            break
        elif wahl == "a":
            print("Abgebrochen.\n")
            break


# PASSWORT ANZEIGEN

#Zeigt das Passwort für eine gewählte Applikation an.
#Ablauf:
#        - Benutzer wählt einen Eintrag aus.
#        - Passwort wird angezeigt.
#        - Passwortstärke wird angezeigt.

    # Passwort beim Anzeigen sichtbar

def passwort_anzeigen():
    # Eintrag auswählen, Passwörter zunächst nicht sichtbar
    applikation, benutzer, _, daten = eintrag_auswaehlen(pw_anzeigen=False)
    if not applikation:
        return

    # Das ausgewählte Passwort aus den Daten extrahieren
    pw = None
    for zeile in daten:
        app, ben, passwort = zeile.split(" | ")
        if app == applikation and ben == benutzer:
            pw = passwort
            break

    if pw:
        print(f"\nPasswort für {applikation} ({benutzer}): {pw}")
        print()
    else:
        print("Passwort konnte nicht gefunden werden.\n")


# PASSWORT PRÜFEN

#    Prüft, ob ein eingegebenes Passwort 
#    Ablauf:
#        - Benutzer wählt einen Eintrag aus.
#        - Passwort wird NICHT angezeigt.
#        - Stärke des Passwortes wird angezeigt

def passwort_pruefen():
    # Eintrag auswählen, Passwort wird nicht in der Liste angezeigt
    applikation, benutzer, _, daten = eintrag_auswaehlen(pw_anzeigen=False)
    if not applikation:
        return

    # Das gespeicherte Passwort aus den Daten extrahieren
    pw = None
    for zeile in daten:
        app, ben, passwort = zeile.split(" | ")
        if app == applikation and ben == benutzer:
            pw = passwort
            break

    if pw:
        # Statt Passwortprüfung: Stärke anzeigen
        print(f"\nPasswort für {applikation} ({benutzer}) hat folgende Stärke:")
        print(passwort_starke(pw))
        print()
    else:
        print("Passwort konnte nicht gefunden werden.\n")



# PASSWORT ÄNDERN
#Ändert das Passwort für einen gewählten Eintrag.
#    Ablauf:
#        - Benutzer wählt einen Eintrag aus.
#        - Neues Passwort wird automatisch generiert.
#        - Passwort wird aktualisiert und gespeichert.
#        - Passwort wird NICHT automatisch angezeigt (optional kann man es printen).

def passwort_aendern():
    applikation, benutzer, _, daten = eintrag_auswaehlen(pw_anzeigen=False)
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
    print("Geändert.\n")

# PASSWORT LÖSCHEN
#Löscht einen gewählten Passwort-Eintrag.

#Ablauf:
#    - Benutzer wählt einen Eintrag aus.
#    - Eintrag wird gelöscht und Datei gespeichert.

def passwort_loeschen():
    applikation, benutzer, _, daten = eintrag_auswaehlen(pw_anzeigen=False)
    if not applikation:
        return

    # Bestätigung, ob wirklich gelöscht werden soll
    while True:
        bestaetigung = input(f"Willst du das Passwort für '{applikation}' wirklich löschen? (j/n): ").strip().lower()
        if bestaetigung == 'j':
            # Passwort löschen
            neue_liste = [z for z in daten if not (z.startswith(applikation) and benutzer in z)]
            alle_speichern(neue_liste)
            print("Das Passwort wurde gelöscht.\n")
            break
        elif bestaetigung == 'n':
            print("Löschen abgebrochen.\n")
            break
        else:
            print("Ungültige Eingabe. Bitte gib 'j' für Ja oder 'n' für Nein ein.")
