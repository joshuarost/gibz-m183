# Darknet diaries (Podcast)

Darknet Diaries ist ein englischsprachiger Podcast der von Jack Rhysider geführt wird, welcher sich mit den dunklen/kriminellen Seiten des Internets befasst.
Durch den Podcast erhält auch ein Laie einen Einblick hinter die Kulissen und mag dadurch eine Vorstellung erhalten wie gross und facettenreich das Internet ist und deren Möglichkeiten und Risiken.
Auch ein Entwickler erhält viele neue und Wichtige Informationen über mögliche Exploits in seinem Code oder Applikation und kann evt. mit diesem neu erlangtem Wissen sein Produkt und arbeit verbessern.

## [Folge 2 - VTech](https://open.spotify.com/episode/4zY9kdW6lIEpe1xITgc7Kr?si=t3a266fsTfafO_zvgKRZog)
Der Internationale Kinder-Tech Hersteller VTech ignorierte auf ihrer Seite Planetvtech.com möglicherweise alle Best-Practices in den Belangen Security die es gibt. Auf dieser Seite registrieren die Eltern der Kinder die im Besitz eines VTech Gerätes ihre Kinder um alle Funktionen der Geräte freizuschalten.
Durch die nicht vorhandenen Sicherheitsmassnahmen von VTech war es einem Anonymen Whitehat Hacker mögliche an die Datenbank hinter Planetvtech zu gelangen und diese zu kopieren. Die gesammelten Daten reichte dieser Anschliessend einem Techblogger weiter damit dieser auf die Verwundbarkeit des Services hinweisen kann.
VTech reagierte mit dem Offline nehmen des Serves darauf und behob anschliessend die Mängel innerhalb von einem Monat.
Über 3 Millionen persönliche Daten über die Kinder und den Eltern waren daran betroffen.

Es ist überraschend, dass in der heutigen Zeit immer noch Webservices von Weltfirmen publiziert werden, welche wie in diesem Fall nicht HTTPS verwendet haben und ihre Passwörter mit MD5 gehashed haben.

Es soll daraus gelernt sein: Überprüft immer den Service auf welchem ihr eure Daten angibt und wenn ihr selbst entwickelt, verwendet anschändige Sicherheitsstandards.

