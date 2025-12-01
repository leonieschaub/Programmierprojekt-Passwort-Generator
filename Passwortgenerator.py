from passwort import *


def menue():
    while True:
        print("\nPasswort-Manager")
        print("-" * 17)
        print("1) Neues Passwort")
        print("2) Passwort anzeigen")
        print("3) Passwort prüfen")
        print("4) Passwort ändern")
        print("5) Passwort löschen")
        print("6) CSV exportieren")
        print("7) Beenden")


        wahl = input("Option: ")

        if wahl == "1": neues_passwort()
        elif wahl == "2": passwort_anzeigen()
        elif wahl == "3": passwort_pruefen()
        elif wahl == "4": passwort_aendern()
        elif wahl == "5": passwort_loeschen()
        elif wahl == "6": exportiere_csv()
        elif wahl == "7": 
            print("Auf Wiedersehen!")
            break
        else:
            print("Ungültige Eingabe. Bitte gültige Wahl eingeben. ")


menue()
