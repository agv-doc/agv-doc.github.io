Entry-Points: Common
====================

.. note::
   Eine Gesamtübersicht der API findest du unter :doc:`index`.

**EntryPoints:**

- :ref:`GET /api/agv/common/ping <get-api-agv-common-ping>`
- :ref:`POST /api/agv/common/identify <get-api-agv-common-identify>`
- :ref:`POST /api/agv/common/restart <get-api-agv-common-restart>`



.. _get-api-agv-common-ping:

Ping - /api/agv/common/ping
---------------------------

.. http:get:: /api/agv/common/ping

   :synopsis: Health-Check (Erreichbarkeit und Verarbeitungsfähigkeit prüfen)
   :reqheader Accept: application/json
   :resheader Content-Type: application/json; charset=utf-8
   :statuscode 200: OK

   **Beschreibung**

   Prüft, ob das System erreichbar ist und Anfragen verarbeiten kann. Keine Authentifizierung erforderlich.

   **Erfolg (200)**

   .. code-block:: json

      {
        "code": 200,
        "status": "success",
        "data": {
          "message": "pong"
        }
      }

   **Felder (`data`)**

   - ``message`` *(string)* – Echo-/Status-Nachricht; bei erfolgreichem Ping ``"pong"``.

.. _get-api-agv-common-identify:

Identify - /api/agv/common/identify
-----------------------------------

.. http:post:: /api/agv/common/identify

   :synopsis: Sicht-/hörbare Identifikationssequenz ausführen (Beep, Flash oder beides)
   :reqheader Content-Type: application/json
   :resheader Content-Type: application/json; charset=utf-8
   :statuscode 200: OK
   :statuscode 400: Ungültiger Moduswert

   **Beschreibung**

   Das Fahrzeug führt eine Identifikationssequenz aus. Es wird **5×** im Sekundentakt
   geblinkt oder gepiepst – abhängig vom Modus. Keine Authentifizierung erforderlich.

----------------

**Request Body - JSON:**

   .. code-block:: json

      {
        "mode": "beepFlash"
      }

   **Parameter**

   - ``mode`` *(string, required)* – Auszuführende Aktion:
        - ``"beep"`` (5× Beepen), 
        - ``"flash"`` (5× Blinken), 
        - ``"beepFlash"`` (Kombination).

----------------

**Success (200):**

    .. code-block:: json

      {
        "code": 200,
        "status": "success",
        "data": {
          "mode": "beepFlash"
        }
      }

   **Felder (`data`)**

   - ``mode`` *(string)* – Der ausgeführte Modus; entspricht dem übermittelten Wert.

----------------


**Example: Error (400 Bad Request)**

.. code-block:: json

      {
        "code": 400,
        "status": "error",
        "details": {
          "shortDesc": "Invalid Value",
          "longDesc": "The 'mode' key must be one of the following values: 'beep', 'flash', 'beepFlash'."
        }
      }

.. _get-api-agv-common-restart:

Restart - /api/agv/common/restart
---------------------------------

.. http:post:: /api/agv/common/restart

   :synopsis: Neustart des Systems (ESP32) auslösen
   :reqheader Content-Type: application/json
   :statuscode 200: OK

   **Beschreibung**

   Führt einen Neustart des Systems aus. Beim Aufruf wird kurz rot blinkend signalisiert (2× 6 Hz),
   anschließend erfolgt der Neustart nach ca. 3,4 s.

   **Authentifizierung:**  

   Nicht erforderlich.

   **Request-Body**

   *leer*

   **Response**

   Es wird **keine inhaltliche Rückmeldung** gesendet (kein Response-Body).
