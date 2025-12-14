import random
import string

import random
import string

# Generiert ein Passwort anhand der angegebenen Kriterien
# Parameter:
#  laenge (int)   : gewünschte Länge des Passworts
#  lower (bool)   : Kleinbuchstaben verwenden
#  upper (bool)   : Großbuchstaben verwenden
#  digits (bool)  : Zahlen verwenden
#  special (bool) : Sonderzeichen verwenden
#  words (bool)   : Wörter aus Wortliste einbauen
# Rückgabe:
#  str : generiertes Passwort

def passwort_generieren(laenge, lower=True, upper=True, digits=True, special=True, words=True):
    # Basis-Zeichensatz aufbauen
    zeichen = ""
    if lower:
        zeichen += string.ascii_lowercase        # Kleinbuchstaben hinzufügen
    if upper:
        zeichen += string.ascii_uppercase        # Grossbuchstaben hinzufügen
    if digits:
        zeichen += string.digits                 # Zahlen hinzufügen
    if special:
        # Sonderzeichen ohne '|'
        zeichen += ''.join(c for c in string.punctuation if c != '|')

    # Wortliste für Wörter-Option
    wortliste = ["sonne", "baum", "haus", "tiger", "mond", "stern", "strasse", "stuhl", "tisch", "wasser"]

    # Prüfen, ob mindestens ein Zeichensatz oder Wörter ausgewählt wurden
    if not zeichen and not words:
        raise ValueError("Keine Zeichen zum Generieren ausgewählt!")

    pw = ""

    # Wörter-only Passwort (kein anderes Zeichen erlaubt)
    if words and not zeichen:
        while len(pw) < laenge:
            pw += random.choice(wortliste)       # Zufällige Wörter aneinanderhängen
        return pw[:laenge]                       # Länge genau zuschneiden

    # Kombination aus Wort + normale Zeichen
    if words and zeichen:
        while len(pw) < laenge:
            # 50% Chance, ein Wort oder ein Zeichen zu wählen
            if random.random() < 0.5:
                pw += random.choice(wortliste)  # Wort einfügen
            else:
                pw += random.choice(zeichen)    # Zeichen einfügen
        pw = pw.replace('|', '')                 # Sicherstellen, dass '|' nicht vorkommt
        return pw[:laenge]                       # Länge genau zuschneiden

    # Normale Passwortgenerierung ohne Wörter
    while len(pw) < laenge:
        pw += random.choice(zeichen)            # Zufällige Zeichen hinzufügen
    return pw[:laenge]                          # Länge genau zuschneiden

    # Wort + normale Zeichen
    if words and zeichen:
        while True:
            pw = random.choice(wortliste)
            while len(pw) < laenge:
                pw += random.choice(zeichen)
            # Sicherstellen, dass kein '|' im Passwort ist
            if '|' not in pw:
                return pw[:laenge]
            # sonst erneut generieren
            pw = ""

    # Normale Passwortgenerierung
    if not zeichen:
        raise ValueError("Keine Zeichen zum Generieren ausgewählt!")
    
    # Passwort generieren und '|' ausschließen
    while True:
        pw = ''.join(random.choice(zeichen) for _ in range(laenge))
        if '|' not in pw:
            return pw

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
    elif punkte >= 4:
        return "stark"
