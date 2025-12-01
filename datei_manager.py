DATEI = "passwoerter.txt"


def speichern(applikation, benutzer, pw):
    with open(DATEI, "a") as f:
        f.write(f"{applikation} | {benutzer} | {pw}\n")


def lade_passwoerter():
    try:
        with open(DATEI, "r") as f:
            return [line.strip() for line in f.readlines()]
    except FileNotFoundError:
        return []


def exportiere_csv():
    import os

    daten = lade_passwoerter()
    if not daten:
        print("Keine Passwörter vorhanden.")
        return

    # Ordner, in dem DEINE Python-Datei liegt
    basis = os.path.dirname(os.path.abspath(__file__))
    datei = os.path.join(basis, "passwoerter.csv")

    with open(datei, "w", encoding="utf-8") as f:
        f.write("Applikation,Benutzer,Passwort\n")
        for eintrag in daten:
            applikation, benutzer, pw = eintrag.split(" | ")
            f.write(f"{applikation},{benutzer},{pw}\n")

    print("CSV erfolgreich erstellt!")
    print("Gespeichert unter:")
    print(datei)

    # Datei automatisch öffnen (Windows)
    os.startfile(datei)


def alle_speichern(daten):
    with open(DATEI, "w") as f:
        for zeile in daten:
            f.write(zeile + "\n")


def eintrag_auswaehlen():
    daten = lade_passwoerter()

    if not daten:
        print("Keine Einträge vorhanden.")
        return None, None, None, daten

    for i, eintrag in enumerate(daten, 1):
        print(f"{i}) {eintrag}")

    try:
        nr = int(input("Nummer auswählen: "))
        applikation, benutzer, pw = daten[nr - 1].split(" | ")
        return applikation, benutzer, pw, daten
    except:
        print("Ungültige Auswahl.")
        return None, None, None, daten



