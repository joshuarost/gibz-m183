# Password
### Welche Anforderungen gibt es?
- Min. 10 Zeichen
- Min. ein klein Buchstabe
- Min. ein gross Buchstabe
- Min. eine Nummer
- Min. ein special Charakter
- Darf nicht mit der E-Mail überein stimmen
- Sollte keine persönliche Verbindung haben

Es ist 2019 und ich finde, dass 10 Zeichen eine vertretbare Länge ist für ein Passwort. Der Benutzer sollte in erster Linie
sicher sein. Das Übereinstimmen der E-Mail Adresse ist, damit der User nicht einfach gedankenlos seine Mail herein kopiert.
Die restlichen Punkte sollten aus meiner Sicht Standard sein und sind zwar ein bisschen mühsam einzuhalten aber man muss wohl
dieses Übel in kauf nehmen für ein gutes Passwort.

### Wie wird das Passwort gespeichert?
1. Das Passwort wird auf die einzuhaltenden Kriterien überprüft.
2. Der sha256 Hash wird angewendet um das Passwort immer in die selbe Länge zu bringen.
3. Der Pfeffer und der Salz werden hinzugefügt.
4. Diese Kombination wird 10x mit Bcrypt gehashed.
5. Der Hash und das Salz wird anschliessend in der Datenbank gespeichert.

**Zu beachten** Der Pfeffer (pepper) wird in einem encrypten File im Sourcecode der Userverwaltung aufbewart.
