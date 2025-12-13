# Import der benötigten Funktionen
from datei_manager import speichern, eintrag_auswaehlen, alle_speichern, exportiere_csv, lade_passwoerter
from generator import passwort_generieren, passwort_starke


# NEUES PASSWORT ERSTELLEN
def neues_passwort():
    
#Erstellt ein neues Passwort für eine Applikation und speichert es.
#Ablauf:
#   - Benutzer gibt Applikation und Benutzername ein.
#   - Benutzer wählt Passwortlänge und Zeichenoptionen.
#   - Passwort wird generiert und angezeigt.
#   - Benutzer kann Passwort speichern, neu generieren oder abbrechen.
    
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
    lower = input("Kleinbuchstaben? (j/n): ").lower() == "j"
    upper = input("Grossbuchstaben? (j/n): ").lower() == "j"
    digits = input("Zahlen? (j/n): ").lower() == "j"
    special = input("Sonderzeichen? (j/n): ").lower() == "j"
    words = input("Wörter verwenden? (j/n): ").lower() == "j"

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
        print("Stärke:", passwort_starke(pw))
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

    neue_liste = [z for z in daten if not z.startswith(applikation)]
    alle_speichern(neue_liste)
    print("Gelöscht.\n")
