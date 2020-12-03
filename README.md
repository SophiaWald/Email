# Email

Dieser Code holt sich, wenn ausgeführt, die aktuellen Wetterdaten von dem Ort der angegebenen Koordinaten, in meinem Fall Basel, mit der Hilfe der Openweathermap API.
Je nach Temperatur wird mithilfe einer If-Schleife ein anderer Text in eine Email eingefügt. Die Email wird in meinem Fall von einer Gmail-Email versendet.
Ist das nicht der Fall müsste der Port geändert werden. Die Email wird mit einer sicheren smtp Verbindung verschickt.
Das Passwort für den Email Acoount des Senders muss in einer Textdatei namens "password.txt" geschrieben stehen.
