# M183 Projektarbeit

## Setup
```bash
# Clone repository
git clone

# build environment
make build

# start the application
make serve
```

## Credentials:
Beide User besitzen meine (Josh Rost) Telefonnummer. Um die Applikation korrekt verwenden zu können, muss die Nummer in der Datenbank geändert werden. Am besten eignet sich der [Sqllitebrowser](https://sqlitebrowser.org/) für das editieren.

**Admin**
- Username: Admin
- Password: Pa$$word2000

**User**
- Username: Mock
- Password: $ecreT3000

## Getroffene Entscheidungen
### Passwort
Zur Sicherung der Passwörter wurde der Bcrypt Algorithmus mithilfe dem gleichnamigen Python Package genutzt.
Bevor der Bcrypt hashing Algorithmus angewendet wird, werden noch folgende Schritte in chronologischer Reihenfolge durchgeführt. Diese tragen zur weiteren Sicherheit bei.
1. Gepepperd, zum Schutz bei einer geleakten Datenbank.
2. Sha256 hashing, um eine einheitliche länge pro Passwort zu erreichen um eine Overflow Attacke von zu langen passwörter zu verhindern.
3. Gesalted, um rainbow table attacken zu verhindern.

Nach diesen Schritten, wird dieses vorbereitete Passwort mit dem Bcrypt Algorithmus gehashed und anschliessend in der Datenbank gespeichert. Dank Bcrypt ist der verwendete Salt zu diesem Zeitpunkt im Passwort vorhanden und ausles bar. Dadurch kann eine spalte für den Salt weggelassen werden.

### Externe Pakete

[Bcrypt](https://pypi.org/project/bcrypt/) wurde wie bereits vorhin erklärt, eingesetzt für die Passwortspeicherung. Dieses Paket ist nur ein Python Wrapper für den eigentlichen Algorithmus geschrieben in C.

[Talisman](https://github.com/GoogleCloudPlatform/flask-talisman) ist eine von Google unterhaltene leichte Erweiterung die das setzten der HTTP Headers übernimmt und somit einfach die häufgigsten Web Angriffe blocken kann.
Durch die von Talisman zur verfügung stehenden Optionen, ist die Applikation auf viele Angriffsarten immun. Zum Beispiel kommen die X-Frame-Options gegen Clickjacking zum einsatz und vieles mehr. Auf dem verlinkten Git Repo, findet man schnell eine übersicht über alle Optionen.
Zudem ist meine Applikation durch die Content Security Policy die gesetzt wird auf fast alle XSS Attacken sicher.

[Flask](https://pypi.org/project/Flask/) ist ein Webframework für Python und kann mit einer Lightweight Variante vom ASP.NET Framework verglichen werden. Dies wurde eingesetzt um die entwicklung zu vereinfachen und auf Python zu ermöglichen.

[Flask-sqlalchemy](https://pypi.org/project/Flask-SQLAlchemy/) ist eine Ergenzung zum Flask Framework und übernimmt die Schnittstelle zwischen Python Code und SQL und lässt den Entwickler einfach und sicher auf die SQL Datenbank zugreifen.

[Flask-login](https://pypi.org/project/Flask-Login/) ist eine Erweiterung die sich um das Session management kümmert.

[Requests](https://pypi.org/project/requests/) ist eine HTTP Python Libary um einfach Requests zu erstellen.

[Gunicorn](https://pypi.org/project/gunicorn/) Ist ein Unix HTTP Server um die Applikation zu “hosten”

### XSS-Attacken
Wie bereits im Talisman Teil der Pakete erwähnt, setze ich mithilfe von Talisman eine Content Security Policy die jegliche Request von ausserhalb unterbindet, da ich auf keine Externen Libraries angewiesen bin. Dadurch bin fast von jeglichen XSS Attacken geschützt.
Zudem Escaped Flask default mässig JavaScript Tags, was eine zusätzliche sicherheit bietet.

### Clickjacking
Die Seite ist wie bereits im Abschnitt Talisman beschrieben durch das Setzen der X-Frame-Options auf Clickjacking geschützt. Zudem werden keine requests von anderen Seiten zugelassen und somit Clickjacking unterbunden.
