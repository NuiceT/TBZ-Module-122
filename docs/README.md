# LB2 - Dokumentation <!-- omit in toc -->

## Inhaltsverzeichnis <!-- omit in toc -->

- [Einführung](#einführung)
- [Beschreibung](#beschreibung)
- [Umsetzung](#umsetzung)
- [Reflexion](#reflexion)

## Einführung

In diesem Modul haben wir den Auftrag bekommen ein kleines Projekt zu programmieren, das folgendermassen aufgebaut sein soll:
![task](task.png)

## Beschreibung

Ich werde mithilfe der Coingecko API wöchentlich einen Report erstellen, die jede Woche den Bitcoin Kurs zusammenfassen. Der Report soll folgendermassen aussehen:

<h1>Wöchentlicher Bitcoin Bericht</h1>
<table>
  <tr>
    <th>Datum</th>
    <th>Preis</th>
  </tr>
  <tr>
    <th>14.06.2022</th>
    <td>CHF 22455</td>
  </tr>
  <tr>
    <th>15.06.2022</th>
    <td>CHF 22233</td>
  </tr>
  <tr>
    <th>16.06.2022</th>
    <td>CHF 22414</td>
  </tr>
  <tr>
    <th>17.06.2022</th>
    <td>CHF 19727</td>
  </tr>
  <tr>
    <th>18.06.2022</th>
    <td>CHF 19883</td>
  </tr>
  <tr>
    <th>19.06.2022</th>
    <td>CHF 18492</td>
  </tr>
  <tr>
    <th>20.06.2022</th>
    <td>CHF 19901</td>
  </tr>
  <tr>
    <th>21.06.2022</th>
    <td>CHF 19959</td>
  </tr>
</table>

## Umsetzung

Die Umsetzung ging relativ einfach, mit `python-dotenv` kann ich die .env Variablen (secrets) abrufen. Die E-Mail habe ich mit `smptlib` gesendet, den Graphen habe ich mit `matplotlib` erstellt. Mehr braucht es eigentlich nicht.

Mein Code geht folgende Schritte durch:

1. Preise von der API abrufen
2. Preise in ein Array zusammenfassen
3. Den Graph erstellen für den Kursverlauf
4. Attachment anhängen
5. E-Mail verschicken
6. ~~Über FTP hochladen~~

## Reflexion

Ich finde, dass meine LB2 gut rausgekommen ist. Ich war gut herausgefordert, aber es war auch einfach, dass ich nicht gestresst war. Ich habe aber etwas das Gefühl, dass man leicht ins kalte Wasser geschmissen wurde, weil man direkt mit einer API arbeiten muss in Python und das manche noch nicht so gut beherrschen, aber dafür war auch Herr Nussle als Unterstützung da. Das mit den Crontab hat auch nicht perfekt funktioniert, ich habe auch nie damit gearbeitet. Ansonsten kann ich nichts mehr dazu sagen.
