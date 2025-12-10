# Projekt Passwort-Generator

## Ausführen des Programms

1. Projektordner in **Visual Studio Code** öffnen  
2. Terminal öffnen: Terminal → Neues Terminal
3. Programm starten mit:

----------------------------------------------------------------------------


## Menüfunktionen ##

### 1. Neues Passwort erstellen
   - Benutzer gibt App und Nutzernamen ein
   - Passwortlänge 12-15 Zeichen
   - Auswahl von:
      - Kleinbuchstaben
      - Grossbuchstaben
      - Zahlen
      - Sonderzeichen
      - Wörter als Passwort
   - Passwort wird generiert und Passwortstärke wird angezeigt
   - Benutzer kann Passwort speichern oder ein neues Passwort generieren

### 2. Passwort anzeigen
  - Liste aller gespeicherten Passwörter anzeigen  
  - Passwort auswählen und anzeigen lassen  
  - Anzeige der Passwort-Stärke

### 3. Passwort prüfen
   - Passwort eingeben
   - Das Programm prüft, ob es korrekt ist
  
### 4. Passwort ändern
   - Ein neues Passwort wird automatisch generiert
   - alter Eintrag wird überschrieben
  
### 5. Passwort löschen
   - Eintrag auswählen und löschen

### 6. CSV-Export
    - Exportiert alle Passwörter in passwoerter.csv
    - CSV öffnet automatisch (Windows)

### 7. Beenden
   - Programm beenden

  ----------------------------------------------------------------------------


## Passwort-Generator

Der Generator unterstützt:
- Kleinbuchstaben
- Grossbuchstaben
- Ziffern
- Sonderzeichen
- Wortbasierte Passwörter (z. B. „sternbaum123“)
- Passwortlänge: 12–15 Zeichen

----------------------------------------------------------------------------


## Passwort-Stärke-Bewertung

Ein Passwort wird anhand dieser Kriterien bewertet:
- Länge ≥ 12
- Kleinbuchstaben vorhanden
- Grossbuchstaben vorhanden
- Ziffern vorhanden
- Sonderzeichen vorhanden

----------------------------------------------------------------------------


## Speicherung von Passwörtern
passwoerter.txt

## CSV-Export
passwoerter.csv
