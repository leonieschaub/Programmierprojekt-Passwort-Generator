
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