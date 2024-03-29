# Darknet diaries
Darknet Diaries ist ein englischsprachiger Podcast von Jack Rhysider. Dieser handelt von der dunklen und kriminellen Seiten des Internets.

Durch den Podcast hat jeder die spannende Möglichkeit einen facettenreichen Einblick in die unzähligen Gefahren und Tücken des Internets zu erhalten. Als Entwickler enthalten die Geschichten viele wichtige und neue Informationen über Angriffsmöglichkeiten, Bedrohungen, Exploits und vieles mehr.

## [Folge 2 - VTech](https://open.spotify.com/episode/4zY9kdW6lIEpe1xITgc7Kr?si=t3a266fsTfafO_zvgKRZog)
Der Internationale Kinder-Tech Hersteller VTech ignorierte auf ihrer Seite Planetvtech.com sämmtliche Security Best-Practices. Diese Seite musste von den Eltern der Kinder genutzt werden um die VTech Geräte und deren Nutzer (die Kinder) zu registrieren.

Durch die massiven Sicherheitslücken von VTech war es einem anonymen Whitehat Hacker gelungen mit XSS und SQL Injections in nur wenigen Minuten an Adminrechte zu gelangen. Anschliessend verwendete er diese um die Daten hinter Planetvtech zu kopieren.

Um auf die Schwachstellen aufmerksam zu machen, reichte er die gesammelten Daten einem vertrauenswürdigen Techblogger weiter. Dieser prüfte die Daten auf ihre echtheit und publizierte einen Artikel nach bestätigung darüber. 
VTech reagierte schnell mit dem Offline nehmen des Servers und einem nichtssagenden Presse Statement. Das Beheben der Mängel dauerte mehrere Monate und kostete das Unternehmen Millionen.
Über 3 Millionen Name, Adressen, Alter und Kreditkarteninformationen der Eltern und deren Kinder  waren daran betroffen. Zusätzlich enthielten die geklauten Daten Tausende Fotos, Sprachnachrichten und Videos der Kinder, welche über die Geräte aufgenommen wurde. 

### Fazit
Es ist erschreckend, dass in der heutigen Zeit immer noch Webservices von Weltfirmen wie VTech online sind, welche nahezu keine Sicherheitsstandards enthalten. In diesem Fall wurde ohne HTTPS und mit MD5 hashes gearbeitet.

Es soll daraus gelernt sein: Überprüft wem ihr eure persönlichen und sensiblen Daten anvertraut. An die Entwickler unter uns: Reisst euch zusammen und implementiert solide Security!

# MELANI Report
Die schweizer Bundes-Organisation MELANI - Melde- und Analysestelle Informationssicherung ist für den Schutz von nationale wichtige IT Infrastrukturen zuständig.
Diese Stelle veröffentlicht pro Halbjahr einen Bericht über die aktuellen und akuten Gefahren des Internets.
Dieser kann von Unternehmen und Privatpersonen genutzt werden um Informationen zu sammeln und wenn nötig anhand von diesen Vorkehrungen in ihren Systemen vorzunehmen.

## [Ryuk - 1. Halbjahresbericht 2019 ](https://www.melani.admin.ch/melani/de/home/dokumentation/berichte/lageberichte/halbjahresbericht-2019-1.html)
Ryuk ist eine Ransomware die seit mitte 2018 aktiv ist und bereits von MELANI thematisiert worden ist. Ransomware ist eine Art von Malware die per Phishing Mail gezielt an Firmen verschickt wird und bei infizierung alle Daten und Zugänge ins und im Netzwerk verschlüsseln. Die verbreiter der Ransomware fordern anschliessend Lösegeld um ihre Systeme wieder zu entschlüsseln. Wenn man nicht zahlt, kann man die Daten nie mehr wiederherstellen.

### Fazit
Da jeder und jede einfach und schnell ein Opfer von Ransomware durch Phishing Mails wird soll vor dem anklicken von Links oder herunterladen von Dokumenten gewarnt sein. Doch das sollte eigentlich schon jeder wissen, deshalb ist es Sinnvoll ein entkoppeltes Backup des PC’s zu erstellen und aufzubewahren. Dadurch ist man bei einem Befall abgesichert. 

# Heise
Auf Heise.de/ct findet man eine Onlineausgabe des berühmnten Computermagazins Ct.
Die Seite bietet aktuelle News rund um Computer und natürlich auch Security für Interessierte aber auch leihen.
Natürlich sollten auch die hier neu gewonnenen Informationen im Privaten und Beruflichen Alltag wenn möglich umgesetzt werden.

## [Arztpraxis im Netz](https://www.heise.de/ct/artikel/Warum-eine-komplette-Arztpraxis-offen-im-Netz-stand-4590103.html)
Durch einen fatalen Bug im Telekom Produkt “Digitalisierungsbox Premium” für Unternehmen war für einen gewissen Zeitraum sämtliche Kundendaten einer Gemeinschaftspraxis im Internet frei zugänglich für jeden.
Wenn das Port-forwarding im Router aktiviert worden ist, wurde anstelle vom Port 443, alle Ports zwischen 440 und 449 freigegeben. Darunter auch der Standard Port für Windows Server Dateifreigaben.

Als Ct die Telekom über diese Lücke informierte, bestätigte diese den Fehler und sie wussten bereits seit Mai 2019 von dem Fehler und es würde jetzt ein Patch kommen, Unglaublich.

### Fazit
Es ist erschreckend zu Wissen, dass möglicherweise meine persönlichen Krankheitsdaten im Internet sind und ein Internetanbieter darüber bescheid weiss und fast für ein Jahr nichts unternimmt.
