import random
import string

def passwort_generieren(laenge, lower=True, upper=True, digits=True, special=True, words=False):
    zeichen = ""

    if lower:
        zeichen += string.ascii_lowercase
    if upper:
        zeichen += string.ascii_uppercase
    if digits:
        zeichen += string.digits
    if special:
        zeichen += string.punctuation

    wortliste = ["sonne", "baum", "haus", "tiger", "mond", "stern", "strasse"]

    if words and not zeichen:
        pw = random.choice(wortliste) + random.choice(wortliste)
        return pw[:laenge]

    if words:
        pw = random.choice(wortliste)
        while len(pw) < laenge:
            pw += random.choice(zeichen)
        return pw[:laenge]

    return "".join(random.choice(zeichen) for _ in range(laenge))


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
        return "schwach (ROT)"
    elif punkte == 3:
        return "mittel (ORANGE)"
    else:
        return "stark (GRÜN)"
 