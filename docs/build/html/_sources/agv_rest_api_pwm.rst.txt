Entry-Points: PWM
=================

.. note::
   Eine Gesamtübersicht der API findest du unter :doc:`index`.

**EntryPoints:**

- :ref:`GET /api/agv/pwm/settings <get-api-agv-pwm-settings>`
- :ref:`POST /api/agv/pwm/enable <post-api-agv-pwm-enable>`
- :ref:`POST /api/agv/pwm/setActiveServos <post-api-agv-pwm-setactiveservos>`
- :ref:`POST /api/agv/pwm/channel/setPosition <post-api-agv-pwm-channel-setposition>`
- :ref:`POST /api/agv/pwm/channel/setLimits <post-api-agv-pwm-channel-setlimits>`
- :ref:`POST /api/agv/pwm/channel/setStartPosition <post-api-agv-pwm-channel-setstartposition>`
- :ref:`POST /api/agv/pwm/channel/setFullSweepTime <post-api-agv-pwm-channel-setfullsweeptime>`


.. _get-api-agv-pwm-settings:

PWM Settings – /api/agv/pwm/settings
------------------------------------

.. http:get:: /api/agv/pwm/settings

   :synopsis: Liefert den aktuellen PWM-Status, Limits und Kanal-Einstellungen.
   :reqheader Accept: application/json
   :resheader Content-Type: application/json
   :statuscode 200: Einstellungen erfolgreich abgerufen.

**Beschreibung:**  
Gibt den PWM-Gesamtstatus (aktiviert, Anzahl aktiver Servos, Maximalanzahl), Default-Werte, globale Limits
sowie eine Liste der aktiven Servo-Kanäle mit deren Limits/Positionen und `fullSweepTime_ms` zurück.

**Response – Success (200):**

.. code-block:: json

   {
     "code": 200,
     "status": "success",
     "data": {
       "enabled": true,
       "activeServos": 4,
       "maxServos": 8,
       "servoDefaults": {
         "min": 500,
         "max": 2500,
         "startPos": 90,
         "fullSweepTime_ms": 1000
       },
       "limits": {
         "minPos": 0,
         "maxPos": 180,
         "min_fullSweepTime_ms": 1,
         "max_fullSweepTime_ms": 5000
       },
       "servos": [
         {
           "channel": 0,
           "min": 500,
           "max": 2500,
           "startPos": 90,
           "currentPos": 90,
           "fullSweepTime_ms": 1000
         }
       ]
     }
   }

**Felder (``data``)**

- ``enabled`` *(bool)* – PWM-Modul aktiv.  
- ``activeServos`` *(int)* – Anzahl aktuell aktiver Servo-Kanäle.  
- ``maxServos`` *(int)* – Maximale Kanalanzahl (Konstante `SERVO_MAX_CHANNELS`).  
- **servoDefaults** *(object)* – Standardwerte für neue/Reset-Konfiguration:  
   - ``min`` *(int)* – Standard-Minimalpuls.  
   - ``max`` *(int)* – Standard-Maximalpuls.  
   - ``startPos`` *(int)* – Standard-Startposition (Grad).  
   - ``fullSweepTime_ms`` *(int)* – Standard-Zeit für 0↔180°-Vollausschlag.  
- **limits** *(object)* – Globale Grenzen:  
   - ``minPos`` *(int)* – Minimal erlaubte Gradposition (`SERVO_MIN_LIMIT`).  
   - ``maxPos`` *(int)* – Maximal erlaubte Gradposition (`SERVO_MAX_LIMIT`).  
   - ``min_fullSweepTime_ms`` *(int)* – Minimal erlaubte Vollausschlag-Zeit (ms).  
   - ``max_fullSweepTime_ms`` *(int)* – Maximal erlaubte Vollausschlag-Zeit (ms).  
- **servos** *(array)* – Liste aktiver Kanäle mit individuellen Werten:  
   - ``channel`` *(int)* – Kanalindex.  
   - ``min`` *(int)*, ``max`` *(int)* – Kanalbezogene Pulsgrenzen.  
   - ``startPos`` *(int)* – Startposition in Grad.  
   - ``currentPos`` *(int)* – Aktuelle Position in Grad.  
   - ``fullSweepTime_ms`` *(int)* – Vollausschlag-Zeit in ms.


.. _post-api-agv-pwm-enable:

PWM Enable – /api/agv/pwm/enable
--------------------------------

.. http:post:: /api/agv/pwm/enable

   :synopsis: Aktiviert oder deaktiviert das PWM-Modul.
   :reqheader Content-Type: application/json
   :resheader Content-Type: application/json
   :jsonparam bool enable: `true` zum Aktivieren, `false` zum Deaktivieren.
   :statuscode 200: Status erfolgreich gesetzt.
   :statuscode 400: Ungültiger Datentyp im Request.

**Beschreibung:**  
Schaltet das PWM-Modul ein/aus. Die Antwort spiegelt den aktuellen Zustand wider.

**Request Body – JSON:**

.. code-block:: json

    { 
     "enable": true 
    }

**Response – Success (200):**

.. code-block:: json

   {
     "code": 200,
     "status": "success",
     "data": { "enabled": true }
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


.. _post-api-agv-pwm-setactiveservos:

Set Active Servos – /api/agv/pwm/setActiveServos
------------------------------------------------

.. http:post:: /api/agv/pwm/setActiveServos

   :synopsis: Setzt die Anzahl der aktiven Servo-Kanäle.
   :reqheader Content-Type: application/json
   :resheader Content-Type: application/json
   :jsonparam int activeServos: Anzahl aktiver Kanäle (1..`SERVO_MAX_CHANNELS`).
   :statuscode 200: Anzahl erfolgreich gesetzt.
   :statuscode 400: Ungültiger Wert/Typ.
   :statuscode 403: PWM-Modul ist nicht aktiviert.

**Beschreibung:**  
Setzt die Zahl der nutzbaren Kanäle. Erfordert aktiviertes PWM-Modul.

**Request Body – JSON:**

.. code-block:: json

    { 
     "activeServos": 4 
    }

**Response – Success (200):**

.. code-block:: json

   {
     "code": 200,
     "status": "success",
     "data": { "activeServos": 4 }
   }


.. _post-api-agv-pwm-channel-setposition:

Set Channel Position – /api/agv/pwm/channel/setPosition
-------------------------------------------------------

.. http:post:: /api/agv/pwm/channel/setPosition

   :synopsis: Setzt die Position eines Servo-Kanals (Grad).
   :reqheader Content-Type: application/json
   :resheader Content-Type: application/json
   :jsonparam int channel: Kanalindex (0..`activeServos-1`).
   :jsonparam int newPosition: Zielposition in Grad (0..180). Wird innerhalb der Kanal-Limits geklemmt.
   :statuscode 200: Position gesetzt.
   :statuscode 400: Ungültige Werte/Typen oder Bereichsverletzung.
   :statuscode 403: PWM-Modul ist nicht aktiviert.

**Beschreibung:**  
Setzt die Zielposition. Liegt `newPosition` außerhalb der kanalbezogenen Limits, wird sie auf den erlaubten Bereich
geklemmt. Die Antwort enthält `coerced=true`, wenn korrigiert wurde.

**Request Body – JSON:**

.. code-block:: json

    { 
     "channel": 0, 
     "newPosition": 135 
    }

**Response – Success (200):**

.. code-block:: json

   {
     "code": 200,
     "status": "success",
     "data": {
       "channel": 0,
       "newPosition": 135,
       "coerced": false
     }
   }


.. _post-api-agv-pwm-channel-setlimits:

Set Channel Limits – /api/agv/pwm/channel/setLimits
---------------------------------------------------

.. http:post:: /api/agv/pwm/channel/setLimits

   :synopsis: Setzt Min-/Max-Grenzen eines Servo-Kanals (Grad).
   :reqheader Content-Type: application/json
   :resheader Content-Type: application/json
   :jsonparam int channel: Kanalindex (0..`activeServos-1`).
   :jsonparam int min: Untere Positionsgrenze (``SERVO_MIN_LIMIT``..``SERVO_MAX_LIMIT``).
   :jsonparam int max: Obere Positionsgrenze (``SERVO_MIN_LIMIT``..``SERVO_MAX_LIMIT``, > ``min``).
   :statuscode 200: Limits gesetzt.
   :statuscode 400: Ungültige Werte/Bereiche.
   :statuscode 403: PWM-Modul ist nicht aktiviert.

**Beschreibung:**  
Setzt die Positionsgrenzen des Kanals. Falls die bisherige `startPos` außerhalb der neuen Grenzen liegt,
wird sie in den Bereich gezwungen. Die Antwort enthält `coerced_startPos=true`, wenn eine Korrektur erfolgte.

**Request Body – JSON:**

.. code-block:: json

    { 
     "channel": 0, 
      "min": 10, 
      "max": 170 
    }

**Response – Success (200):**

.. code-block:: json

   {
     "code": 200,
     "status": "success",
     "data": {
       "channel": 0,
       "min": 10,
       "max": 170,
       "startPos": 90,
       "coerced_startPos": false
     }
   }


.. _post-api-agv-pwm-channel-setstartposition:

Set Channel Start Position – /api/agv/pwm/channel/setStartPosition
------------------------------------------------------------------

.. http:post:: /api/agv/pwm/channel/setStartPosition

   :synopsis: Setzt die Startposition eines Servo-Kanals (Grad).
   :reqheader Content-Type: application/json
   :resheader Content-Type: application/json
   :jsonparam int channel: Kanalindex (0..`activeServos-1`).
   :jsonparam int startPos: Startposition in Grad (innerhalb der kanalbezogenen Limits).
   :statuscode 200: Startposition gesetzt.
   :statuscode 400: Ungültige Werte/Bereiche.
   :statuscode 403: PWM-Modul ist nicht aktiviert.

**Beschreibung:**  
Legt die Startposition fest. Der Wert muss zwischen den aktuellen Kanal-Limits liegen.

**Request Body – JSON:**

.. code-block:: json

    { 
     "channel": 0, 
     "startPos": 90 
    }

**Response – Success (200):**

.. code-block:: json

   {
     "code": 200,
     "status": "success",
     "data": { "channel": 0, "startPos": 90 }
   }


.. _post-api-agv-pwm-channel-setfullsweeptime:

Set Channel Full Sweep Time – /api/agv/pwm/channel/setFullSweepTime
-------------------------------------------------------------------

.. http:post:: /api/agv/pwm/channel/setFullSweepTime

   :synopsis: Setzt die Vollausschlag-Zeit (0↔180°) eines Servo-Kanals in Millisekunden.
   :reqheader Content-Type: application/json
   :resheader Content-Type: application/json
   :jsonparam int channel: Kanalindex (0..`activeServos-1`).
   :jsonparam int fullSweepTime_ms: Vollausschlag-Zeit in ms (``SERVO_MIN_FULL_SWEEP_TIME_MS``..``SERVO_MAX_FULL_SWEEP_TIME_MS``).
   :statuscode 200: Zeit gesetzt.
   :statuscode 400: Ungültige Werte/Bereiche.
   :statuscode 403: PWM-Modul ist nicht aktiviert.

**Beschreibung:**  
Konfiguriert, wie lange der Servo von 0° auf 180° (bzw. umgekehrt) benötigt.

**Request Body – JSON:**

.. code-block:: json

    {
      "channel": 0, 
      "fullSweepTime_ms": 1000 
    }

**Response – Success (200):**

.. code-block:: json

   {
     "code": 200,
     "status": "success",
     "data": { "channel": 0, "fullSweepTime_ms": 1000 }
   }
