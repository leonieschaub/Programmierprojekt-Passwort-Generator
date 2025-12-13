DATEI = "passwoerter.txt"
    
# Speichert einen neuen Passwort-Eintrag in der Passwortdatei.
#  Parameter:
#       applikation (str): Name der Anwendung/Website.
#       benutzer (str): Benutzername oder E-Mail.
#        pw (str): Zu speicherndes Passwort.

# Ablauf:
#        - Öffnet die Datei im Append-Modus.
#        - Fügt einen neuen Eintrag in der Form 
#         "Applikation | Benutzer | Passwort" hinzu.

#   Rückgabe:
#        None

def speichern(applikation, benutzer, pw):
    with open(DATEI, "a") as f:
        f.write(f"{applikation} | {benutzer} | {pw}\n")


#Lädt alle gespeicherten Passwörter aus der Datei.

#Ablauf:
# - Liest jede Zeile der Passwortdatei ein.
# - Entfernt Zeilenumbrüche.
# - Gibt eine Liste aller Einträge zurück.
# - Falls die Datei nicht existiert, wird eine leere Liste zurückgegeben.

#Rückgabe:
#  list[str]: Liste aller gespeicherten Passwortzeilen.

def lade_passwoerter():
    try:
        with open(DATEI, "r") as f:
            return [line.strip() for line in f.readlines()]
    except FileNotFoundError:
        return []


#Exportiert alle gespeicherten Passwörter als CSV-Datei.

#Ablauf:
#   - Lädt zuerst alle Passwörter.
#   - Erstellt eine Datei 'passwoerter.csv'
#   - Schreibt die Daten in Spalten (Applikation, Benutzer, Passwort)
#   - Öffnet die CSV-Datei automatisch unter Windows.

#Besonderheiten:
#   - Falls keine Daten vorhanden sind, wird eine Meldung ausgegeben.
#   - Die CSV wird mit UTF-8 erstellt.
# 
# Rückgabe:
#   None

def exportiere_csv():
    import os

    daten = lade_passwoerter()
    if not daten:
        print("Keine Passwörter vorhanden.")
        return

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

    os.startfile(datei)

#Überschreibt die Passwortdatei mit einer neuen Liste an Daten.

#Parameter:
# daten (list[str]): Liste der Zeilen, die gespeichert werden sollen.

# Ablauf:
# - Öffnet die Datei im Schreibmodus (löscht alte Inhalte).
# - Schreibt alle übergebenen Zeilen neu in die Datei.

#Rückgabe:
#  None

def alle_speichern(daten):
    with open(DATEI, "w") as f:
        for zeile in daten:
            f.write(zeile + "\n")

 
# Zeigt alle gespeicherten Passwortzeilen an und erlaubt dem Benutzer,
# einen Eintrag durch Eingabe einer Nummer auszuwählen.

#   Ablauf:
#       - Lädt alle gespeicherten Passwörter.
#       - Gibt sie als nummerierte Liste aus.
#       - Benutzer wählt eine Nummer.
#       - Eintrag wird in seine Bestandteile aufgeteilt:
#          (Applikation, Benutzer, Passwort)

#    Fehlerbehandlung:
#      - Falls keine Einträge existieren -> Rückgabe: (None, None, None, daten)
#      - Falls eine ungültige Nummer eingegeben wird -> ebenfalls None-Werte.

#  Rückgabe:
#           (applikation (str | None),
#            benutzer (str | None),
#            pw (str | None),
#            daten (list[str]))  vollständige Datenliste

def eintrag_auswaehlen(pw_anzeigen=False):
    daten = lade_passwoerter()

    if not daten:
        print("Keine Einträge vorhanden.")
        return None, None, None, daten

    for i, eintrag in enumerate(daten, 1):
        applikation, benutzer, pw = eintrag.split(" | ")

        if pw_anzeigen:
            print(f"{i}) {applikation} | {benutzer} | {pw}")
        else:
            print(f"{i}) {applikation} | {benutzer} | ********")

    try:
        nr = int(input("Nummer auswählen: "))
        applikation, benutzer, pw = daten[nr - 1].split(" | ")

        if pw_anzeigen:
            return applikation, benutzer, pw, daten
        else:
            return applikation, benutzer, None, daten

    except:
        print("Ungültige Auswahl.")
        return None, None, None, daten

