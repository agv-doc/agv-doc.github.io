AGV – REST API Dokumentation
============================

Allgemeines
-----------

- **API-Version:** |release|
- **Created:** Okt. 2025
- **Author:** |author|

- **Protokoll:** HTTP
- **Datenformat:** Alle **Requests** (bei POST/PUT/PATCH) und **Responses** verwenden **JSON**
- **Zeichensatz:** UTF-8
- **Content-Type:** ``application/json``
- **Fehlermodell:** Einheitliches Fehlerobjekt (siehe unten)
- **Lokalisierung:** Fehlermeldungen standardmäßig Englisch

Top-Level-Felder der API-Antworten
----------------------------------

- ``code`` *(number)* – numerischer API-Statuscode (z. B. ``200``, ``400``)
- ``status`` *(string)* – ``"success"`` oder ``"error"``
- ``data`` *(object, optional)* – Nutzlast bei **Erfolg**
- ``details`` *(object, optional)* – Zusatzinfos bei **Fehlern**

Genau **eines** der Felder ``data`` **oder** ``details`` ist in einer Antwort vorhanden.

Antwortmodelle
--------------

**Erfolg (Success Response)**

.. code-block:: json

   {
     "code": 200,
     "status": "success",
     "data": {
       "message": "pong"
     }
   }

**Fehler (Error Response)**

.. code-block:: json

   {
     "code": 400,
     "status": "error",
     "details": {
       "shortDesc": "Invalid Value",
       "longDesc": "The 'channel' value is out of range."
     }
   }

Konventionen für Requests
-------------------------

- **HTTP-Methoden:** ``GET`` (lesen), ``POST`` (Aktion), ``PUT`` (ersetzen)
- **Parameterübergabe:** **JSON-Body** für Nutzdaten (POST/PUT/PATCH)
- **Antwortcodes (Leitfaden):**
   - ``200 OK`` – Erfolg mit Inhalt
   - ``201 Created`` – Ressource erstellt
   - ``204 No Content`` – Erfolg ohne Inhalt
   - ``400 Bad Request`` – Ungültige Anfrage/Parameter
   - ``401 Unauthorized`` – Authentifizierung erforderlich/fehlgeschlagen
   - ``403 Forbidden`` – Berechtigung fehlt
   - ``404 Not Found`` – Ressource nicht vorhanden
