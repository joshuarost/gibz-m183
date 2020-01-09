# Projektarbeit

## Setup
```bash
```

## Credentials:
**Admin**
- Username: Admin
- Password: Pa$$word2000

**User**
- Username: Mock
- Password: $ecreT3000

## Getroffene Entscheidungen
### Passwort
Zur Sicherung der Passwörter wurde der Bcrypt Algorithmus mithilfe dem gleichnamigen Python Package genutzt. Bevor der Bcrypt hashing Algorithmus angewendet wird, werden noch folgende Schritte in chronologischer Reihenfolge durchgeführt. Diese tragen zur weiteren Sicherheit bei.
1. Gepepperd, zum Schutz bei einer geleakten Datenbank.
2. Sha256 hashing, um eine einheitliche länge pro Passwort zu erreichen um eine Overflow Attacke von zu langen passwörter zu verhindern.
3. Gesalted, um rainbow table attacken zu verhindern.
Nach diesen Schritten, wird das Passwort mit dem Bcrypt Algorythmus gehashed und anschliessend in der Datenbank gespeichert.

### Externe Pakete
**Bcrypt** wie bereits vorher erklärt, wurde für die Passwortspeicherung eingesetzt. Dieses Packet ist der Pyhton Wrapper für den Algorithmus. [Talisman](https://github.com/GoogleCloudPlatform/flask-talisman).
**Flask-sqlalchemy** wird verwendet um eine vereinfachte schnittstelle zwischen Python Code und SQL zu erhalten. Dadurch ist es möglich direkt im code aus der Datenbank zu lesen.
**Requets** ist ein Python Haus eigenes Paket das für HTML request verwendet wird, wie zum beispiel beim verschicken des SMS.
Flask ist das Python Framework für Webapplimatien ändlich wie ASP.NET. Mit **flask-restplus** wird das erstellen der Rest API vereinfacht.

### XSS-Attacken
Die XSS-Attacken werden mithilfe von Cross-Origin Resource Sharing ( kurz CORS) verhindert.
