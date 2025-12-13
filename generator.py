import random
import string

# Generiert ein Passwort anhand der angegebenen Kriterien.

# Parameter:
#  laenge (int): Länge des zu erzeugenden Passworts.
#  lower (bool): Kleinbuchstaben verwenden.
#  upper (bool): Grossbuchstaben verwenden.
#  digits (bool): Ziffern verwenden.
#  special (bool): Sonderzeichen verwenden.
#  words (bool): Wörter aus einer Wortliste einbauen.

# Ablauf:
#  - Baut zunächst einen Zeichenmix basierend auf den Optionen auf.
#  - Falls 'words' aktiviert ist, wird ein zufälliges Wort verwendet
#    (oder zwei, wenn keine weiteren Zeichen erlaubt sind).
#  - Bei normaler Erzeugung wird das Passwort vollständig aus dem 
#    Zeichenmix gebaut.

#    Rückgabe:
#        str: Das generierte Passwort.

def passwort_generieren(laenge, lower=True, upper=True, digits=True, special=True, words=True):
    zeichen = ""

    if lower:
        zeichen += string.ascii_lowercase
    if upper:
        zeichen += string.ascii_uppercase
    if digits:
        zeichen += string.digits
    if special:
        zeichen += string.punctuation

    wortliste = ["sonne", "baum", "haus", "tiger", "mond", "stern", "strasse", "stuhl", "tisch", "wasser"]

    # Wörter-only Passwort
    if words and not zeichen:
        pw = random.choice(wortliste) + random.choice(wortliste)
        return pw[:laenge]

    # Wort + normale Zeichen
    if words:
        pw = random.choice(wortliste)
        while len(pw) < laenge:
            pw += random.choice(zeichen)
        return pw[:laenge]

    # Normale Passwortgenerierung
    return "".join(random.choice(zeichen) for _ in range(laenge))

#Bewertet die Stärke eines Passworts anhand verschiedener Kriterien.
#   Parameter:
#     pw (str): Das zu bewertende Passwort.
#  Kriterien:
#     - Länge mindestens 12 Zeichen
#     - Enthält Kleinbuchstaben
#     - Enthält Grossbuchstaben
#     - Enthält Ziffern
#     - Enthält Sonderzeichen

def passwort_starke(pw):
    punkte = 0

    if len(pw) >= 12:
        punkte += 1
    if any(c.islower() for c in pw):
        punkte += 1
    if any(c.isupper() for c in pw):
        punkte += 1
    if any(c.isdigit() for c in pw):
        punkte += 1
    if any(c in string.punctuation for c in pw):
        punkte += 1

    if punkte <= 2:
        return "schwach"
    elif punkte == 3:
        return "mittel"
    else:
        return "stark"
