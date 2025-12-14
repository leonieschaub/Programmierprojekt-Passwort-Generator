# Projekt Passwort-Generator
Dieses Projekt ist ein Passwort-Generator und Passwort-Manager, der sichere Passwörter erstellt, speichert und verwaltet.

## Dateiübersicht
- `hauptfunktionen.py` – enthält alle Hauptfunktionen des Programms
- `hauptmenü.py` – Steuerung des Menüs
- `generator.py` – Passwortgenerierung
- `datei_manager.py` – Verwaltung der gespeicherten Passwörter
- `passwoerter.txt` – Speicherung der Passwörter
- `passwoerter.csv` – Export der Passwörter



## Ausführen des Programms

1. Projektordner in Visual Studio Code öffnen  
2. Terminal öffnen: Terminal → Neues Terminal
3. Programm starten mit:
```
python menue.py
```

----------------------------------------------------------------------------


## Menü

### 1. Neues Passwort erstellen
   - Benutzer gibt App und Nutzernamen ein
   - Passwortlänge 12-15 Zeichen
   - Auswahl von:
      - Kleinbuchstaben
      - Grossbuchstaben
      - Zahlen
      - Sonderzeichen
      - Wörter
   - Passwort wird generiert und Passwortstärke wird angezeigt
   - Benutzer kann das Passwort speichern, generieren oder das Programm abbrechen

### 2. Passwort anzeigen
  - Liste aller gespeicherten Passwörter anzeigen  
  - Passwort auswählen und anzeigen lassen  

### 3. Passwort prüfen
   - Passwort auswählen
   - Das Programm prüft Passwort auf Stärke
  
### 4. Passwort ändern
   - Ein neues Passwort wird automatisch generiert
   - alter Eintrag wird überschrieben
  
### 5. Passwort löschen
   - Eintrag auswählen und löschen
   - Vor Löschung: Abfrage, ob User dieses Passwort löschen will

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
- Wortbasierte Passwörter aus vorgegebener Wörterliste
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
`passwoerter.txt`

## CSV-Export
`passwoerter.csv`
