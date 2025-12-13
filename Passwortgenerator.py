from passwort import *

# HAUPTMENÜ
def menue():

# Hauptmenü des Passwort-Managers.

#Ablauf:
#- Das Menü läuft in einer Endlosschleife.
#- Der Benutzer wählt eine der Funktionen aus:

    while True:
        print("-" * 40)
        print("\nHerzlich Willkommen beim Passwort-Manager :)")
        print("-" * 40)
        print("Bitte wähle eine der folgenden Funktionen:")
        print("1) Neues Passwort")
        print("2) Passwort anzeigen")
        print("3) Passwort prüfen")
        print("4) Passwort ändern")
        print("5) Passwort löschen")
        print("6) CSV exportieren")
        print("7) Beenden")


        wahl = input("Option: ")

        if wahl == "1":
            neues_passwort()
        elif wahl == "2":
            passwort_anzeigen()
        elif wahl == "3":
            passwort_pruefen()
        elif wahl == "4":
            passwort_aendern()
        elif wahl == "5":
            passwort_loeschen()
        elif wahl == "6":
            exportiere_csv()
        elif wahl == "7":
            print("Auf Wiedersehen und bis bald!")
            break  # Programm wirklich beenden
        else:
            print("Ungültige Eingabe. Bitte Zahl von 1-7 ohne Leerzeichen eingeben.\n")
            continue  # Zurück zum Menü


# Programmstart
menue()
