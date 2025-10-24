Entry-Points: WhereIsMyAGV
==========================

.. note::
   Eine Gesamtübersicht der API findest du unter :doc:`index`.

**EntryPoints:**

- :ref:`GET /api/agv/whereIsMyAGV/status <get-api-agv-wima-status>`
- :ref:`POST /api/agv/whereIsMyAGV/enable <post-api-agv-wima-enable>`
- :ref:`POST /api/agv/whereIsMyAGV/settings <post-api-agv-wima-settings>`


.. _get-api-agv-wima-status:

WhereIsMyAGV Status – /api/agv/whereIsMyAGV/status
--------------------------------------------------

.. http:get:: /api/agv/whereIsMyAGV/status

   :synopsis: Liefert den aktuellen Status der "WhereIsMyAGV"-Funktion.
   :reqheader Accept: application/json
   :resheader Content-Type: application/json; charset=utf-8
   :statuscode 200: Status erfolgreich abgerufen.
   :statuscode 403: Zugriff verweigert.

**Beschreibung:**  
Zeigt an, ob die „WhereIsMyAGV“-Funktion aktiviert ist, und gibt die aktuell gespeicherte Gruppenzugehörigkeit
sowie das Secret-Token zurück.

**Response – Success (200):**

.. code-block:: json

   {
     "code": 200,
     "status": "success",
     "data": {
       "enable": true,
       "group": "AGV-TEAM-01",
       "secret": "mySecretToken123"
     }
   }

**Felder (``data``):**

- ``enable`` *(bool)* – Gibt an, ob die Funktion aktiviert ist.  
- ``group`` *(string)* – Gruppenname, mindestens 3 Zeichen.  
- ``secret`` *(string)* – Geheimes Token zur Identifikation.


.. _post-api-agv-wima-enable:

WhereIsMyAGV Enable – /api/agv/whereIsMyAGV/enable
--------------------------------------------------

.. http:post:: /api/agv/whereIsMyAGV/enable

   :synopsis: Aktiviert oder deaktiviert die „WhereIsMyAGV“-Funktion.
   :reqheader Content-Type: application/json
   :resheader Content-Type: application/json; charset=utf-8
   :jsonparam bool enable: ``true`` zum Aktivieren, ``false`` zum Deaktivieren.
   :statuscode 200: Status geändert.
   :statuscode 400: Ungültiger Wert/Typ.
   :statuscode 403: Zugriff verweigert.

**Beschreibung:**  
Schaltet die „WhereIsMyAGV“-Funktion ein oder aus.

**Request Body – JSON:**

.. code-block:: json

   { "enable": true }

**Response – Success (200):**

.. code-block:: json

   {
     "code": 200,
     "status": "success",
     "data": { "enable": true }
   }

**Response – Error (400 Bad Request):**

.. code-block:: json

   {
     "code": 400,
     "status": "error",
     "details": {
       "shortDesc": "Invalid Value",
       "longDesc": "The 'enable' key must be of type bool."
     }
   }


.. _post-api-agv-wima-settings:

WhereIsMyAGV Settings – /api/agv/whereIsMyAGV/settings
------------------------------------------------------

.. http:post:: /api/agv/whereIsMyAGV/settings

   :synopsis: Legt die Gruppen- und Secret-Daten für die „WhereIsMyAGV“-Funktion fest.
   :reqheader Content-Type: application/json
   :resheader Content-Type: application/json; charset=utf-8
   :jsonparam string group: Gruppenname (mind. 3 Zeichen).
   :jsonparam string secret: Geheimschlüssel zur Authentifizierung.
   :statuscode 200: Einstellungen erfolgreich übernommen.
   :statuscode 400: Ungültige Werte/Typen.
   :statuscode 403: Zugriff verweigert.

**Beschreibung:**  
Aktualisiert die Gruppen-ID und das Secret für den „WhereIsMyAGV“-Service.  
Ungültige Werte (z. B. zu kurze Gruppennamen) führen zu einem 400-Fehler.

**Request Body – JSON:**

.. code-block:: json

   {
     "group": "AGV-TEAM-01",
     "secret": "mySecretToken123"
   }

**Response – Success (200):**

.. code-block:: json

   {
     "code": 200,
     "status": "success",
     "data": {
       "group": "AGV-TEAM-01",
       "secret": "mySecretToken123"
     }
   }

**Response – Error (400 Bad Request):**

.. code-block:: json

   {
     "code": 400,
     "status": "error",
     "details": {
       "shortDesc": "Invalid Value",
       "longDesc": "The 'group' value must be at least 3 characters long."
     }
   }
