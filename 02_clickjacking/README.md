# M183: Demo-Projekt für Clickjacking
In diesem Projekt wird exemplarisch die Funktionsweise einer Clickjacking-Attacke aufgezeigt.

Ein (fiktiver) Angreifer versucht ahnungslose Besucher/-innen seiner manipulierten Webseite zu überlisten. Dazu wird eine "externe" Webseite (`innerPage/inner.html`) in einem `iframe` auf der Webseite des Angreifers (`outer.html`) eingebunden. Das ganze `iframe` wird anschliessend durch fingierte Inhalte des Angreifers überlagert.

Die Aufgabe der Lernenden besteht darin, als Betreiber/-in der _externen_ Webseite die hier gezeigte Clickjacking-Attacke zu unterbinden. Dazu soll eine relativ neue Strategie mit [IntersectionObserver](https://w3c.github.io/IntersectionObserver/v2/) (Version 2) angewendet werden.

Eine entsprechende Arbeitsanweisung mit verschiedenen Links ist in der Datei [innerPage/inner.html](innerPage/inner.html) (ab Zeile 53) zu finden.