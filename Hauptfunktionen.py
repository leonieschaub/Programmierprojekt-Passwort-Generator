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
    applikation = input("Applikation: ")
    benutzer = input("Benutzer: ")

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
    applikation, benutzer, pw, _ = eintrag_auswaehlen(pw_anzeigen=True)
    if applikation:
        print(f"\nPasswort für {applikation} ({benutzer}): {pw}")
        print()

# PASSWORT PRÜFEN

#    Prüft, ob ein eingegebenes Passwort mit dem gespeicherten Passwort übereinstimmt.
#    Ablauf:
#        - Benutzer wählt einen Eintrag aus.
#        - Passwort wird NICHT angezeigt.
#        - Benutzer gibt Passwort ein.
#        - Ausgabe OK! oder FALSCH.

def passwort_pruefen():
    applikation, benutzer, _, daten = eintrag_auswaehlen(pw_anzeigen=False)
    if not applikation:
        return

    # Alle passenden Passwörter sammeln
    treffer = []
    for zeile in daten:
        app, ben, pw = zeile.split(" | ")
        if app == applikation and ben == benutzer:
            treffer.append(pw)

    # Fehlerfälle
    if len(treffer) == 0:
        print("Kein Passwort für diesen Account gefunden.\n")
        return

    if len(treffer) > 1:
        print("FEHLER: Für diesen Account existieren mehrere Passwörter!")
        print("Bitte bereinige die Einträge, bevor du das Passwort prüfst.\n")
        return

    # Genau ein Passwort → prüfen
    eingabe = input(f"Passwort für {applikation} eingeben: ")

    if eingabe == treffer[0]:
        print("Stärke:", passwort_starke(pw))
        print("OK!\n")
    else:
        print("FALSCH!\n")


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
    bestaetigung = input(f"Willst du das Passwort für '{applikation}' wirklich löschen? (j/n): ").strip().lower()
    if bestaetigung != 'j':
        print("Löschen abgebrochen.\n")
        return

    # Passwort löschen
    neue_liste = [z for z in daten if not z.startswith(applikation)]
    alle_speichern(neue_liste)
    print("Das Passwort wurde gelöscht.\n")

# Frage, ob ein neues Passwort generiert werden soll
    while True:
        neues_pw = input(
            f"Willst du ein neues Passwort für '{applikation}' generieren? (j/n): "
        ).strip().lower()

        if neues_pw == 'j':
            # Hier kannst du deine Passwort-Generierungsfunktion aufrufen
            generiertes_passwort = passwort_generieren()
            print(f"Neues Passwort für '{applikation}': {generiertes_passwort}\n")
            break
        elif neues_pw == 'n':
            print("Kein neues Passwort generiert.\n")
            break
        else:
            print("Ungültige Eingabe. Bitte gib 'j' für Ja oder 'n' für Nein ein.")
