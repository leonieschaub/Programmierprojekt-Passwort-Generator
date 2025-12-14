import os

# Datei, in der Passwörter gespeichert werden
DATEI = "passwoerter.txt"

# ==========================
# Funktion: speichern
# ==========================
# Speichert einen neuen Passwort-Eintrag in der Datei.
# Parameter:
#   - applikation: Name der Anwendung/Website
#   - benutzer: Benutzername oder E-Mail
#   - pw: Passwort
def speichern(applikation, benutzer, pw):
    # Öffnet die Datei im Anhangmodus und schreibt den neuen Eintrag
    with open(DATEI, "a", encoding="utf-8") as f:
        f.write(f"{applikation} | {benutzer} | {pw}\n")

# ==========================
# Funktion: lade_passwoerter
# ==========================
# Lädt alle gespeicherten Passwörter aus der Datei.
# Rückgabe: Liste von Einträgen (str)
def lade_passwoerter():
    try:
        # Datei lesen und Zeilen in Liste speichern
        with open(DATEI, "r", encoding="utf-8") as f:
            return [line.strip() for line in f.readlines()]
    except FileNotFoundError:
        # Falls Datei nicht existiert, leere Liste zurückgeben
        return []

# ==========================
# Funktion: exportiere_csv
# ==========================
# Exportiert alle Passwörter als CSV-Datei
def exportiere_csv():
    # Alle Passwörter laden
    daten = lade_passwoerter()
    if not daten:
        print("Keine Passwörter vorhanden.")
        return

    # Speicherort der CSV-Datei ermitteln
    basis = os.path.dirname(os.path.abspath(__file__))
    datei = os.path.join(basis, "passwoerter.csv")

    # CSV-Datei erstellen
    with open(datei, "w", encoding="utf-8") as f:
        f.write("Applikation,Benutzer,Passwort\n")
        for eintrag in daten:
            try:
                applikation, benutzer, pw = eintrag.split(" | ")
            except ValueError:
                # Ungültige Zeilen überspringen
                continue
            f.write(f"{applikation},{benutzer},{pw}\n")

    print("CSV erfolgreich erstellt!")
    print("Gespeichert unter:", datei)

    # Datei unter Windows automatisch öffnen
    if os.name == 'nt':
        os.startfile(datei)

# ==========================
# Funktion: alle_speichern
# ==========================
# Überschreibt die Passwortdatei mit einer neuen Liste von Einträgen
# Parameter:
#   - daten: Liste von Strings im Format "Applikation | Benutzer | Passwort"
def alle_speichern(daten):
    with open(DATEI, "w", encoding="utf-8") as f:
        for zeile in daten:
            f.write(zeile + "\n")

# ==========================
# Funktion: eintrag_auswaehlen
# ==========================
# Zeigt alle gespeicherten Einträge nummeriert an und gibt den gewählten zurück
# Parameter:
#   - pw_anzeigen: bool, ob das Passwort in der Liste sichtbar sein soll
# Rückgabe:
#   - applikation (str | None)
#   - benutzer (str | None)
#   - pw (str | None)
#   - daten (list[str])
def eintrag_auswaehlen(pw_anzeigen=False):
    # Alle Passwörter laden
    daten = lade_passwoerter()
    if not daten:
        print("Keine Einträge vorhanden.")
        return None, None, None, daten

    # Alle Einträge nummeriert ausgeben
    for i, eintrag in enumerate(daten, 1):
        try:
            applikation, benutzer, pw = eintrag.split(" | ")
        except ValueError:
            # Ungültige Zeilen überspringen
            continue
        if pw_anzeigen:
            print(f"{i}) {applikation} | {benutzer} | {pw}")
        else:
            print(f"{i}) {applikation} | {benutzer} | ********")

    # Benutzer wählt einen Eintrag
    try:
        nr = int(input("Nummer auswählen: "))
        if nr < 1 or nr > len(daten):
            raise ValueError
        applikation, benutzer, pw = daten[nr - 1].split(" | ")
        if pw_anzeigen:
            return applikation, benutzer, pw, daten
        else:
            return applikation, benutzer, None, daten
    except (ValueError, IndexError):
        print("Ungültige Auswahl.")
        return None, None, None, daten
