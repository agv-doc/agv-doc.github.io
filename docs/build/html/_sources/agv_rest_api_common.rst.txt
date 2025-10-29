Entry-Points: Common
====================

.. note::
   Eine Gesamtübersicht der API findest du unter :doc:`index`.

**EntryPoints:**

- :ref:`GET /api/agv/common/ping <get-api-agv-common-ping>`
- :ref:`POST /api/agv/common/identify <post-api-agv-common-identify>`
- :ref:`POST /api/agv/common/restart <post-api-agv-common-restart>`


.. _get-api-agv-common-ping:

Ping - /api/agv/common/ping
---------------------------

.. http:get:: /api/agv/common/ping

   :synopsis: Health-Check (Erreichbarkeit und Verarbeitungsfähigkeit prüfen).
   :reqheader Accept: application/json
   :resheader Content-Type: application/json
   :statuscode 200: OK

**Beschreibung:**  
Prüft, ob das System erreichbar ist und Anfragen verarbeiten kann.

**Response – Success (200):**

.. code-block:: json

   {
     "code": 200,
     "status": "success",
     "data": {
       "message": "pong"
     }
   }

**Felder (``data``)**

- ``message`` *(string)* – Echo-/Status-Nachricht; bei erfolgreichem Ping ``"pong"``.


.. _post-api-agv-common-identify:

Identify - /api/agv/common/identify
-----------------------------------

.. http:post:: /api/agv/common/identify

   :synopsis: Identifikation des Fahrzeugs auslösen.
   :reqheader Content-Type: application/json
   :resheader Content-Type: application/json
   :jsonparam string mode: Auszuführende Aktion (``"beep"``, ``"flash"``, ``"beepFlash"``).
   :statuscode 200: OK
   :statuscode 400: Ungültiger Moduswert.

**Beschreibung:**  
Das Fahrzeug führt eine Identifikationssequenz aus. Es wird **5×** im Sekundentakt geblinkt oder gepiepst – abhängig vom Modus.

**Request Body – JSON:**

.. code-block:: json

   {
     "mode": "beepFlash"
   }

**Response – Success (200):**

.. code-block:: json

   {
     "code": 200,
     "status": "success",
     "data": {
       "mode": "beepFlash"
     }
   }

**Felder (``data``)**

- ``mode`` *(string)* – Der ausgeführte Modus; entspricht dem übermittelten Wert.

**Response – Error (400 Bad Request):**

.. code-block:: json

   {
     "code": 400,
     "status": "error",
     "details": {
       "shortDesc": "Invalid Value",
       "longDesc": "The 'mode' key must be one of the following values: 'beep', 'flash', 'beepFlash'."
     }
   }


.. _post-api-agv-common-restart:

Restart - /api/agv/common/restart
---------------------------------

.. http:post:: /api/agv/common/restart

   :synopsis: Neustart des Systems (ESP32) auslösen.
   :reqheader Content-Type: application/json
   :resheader Content-Type: application/json
   :statuscode 200: OK

**Beschreibung:**  
Führt einen Neustart des Systems aus. Beim Aufruf wird kurz rot blinkend signalisiert (2× 6 Hz), anschließend erfolgt der Neustart nach ca. 3,4 s.

**Request Body – JSON:**  
*leer*

**Response – Success (200):**  
Es wird **keine inhaltliche Rückmeldung** gesendet (kein Response-Body).
