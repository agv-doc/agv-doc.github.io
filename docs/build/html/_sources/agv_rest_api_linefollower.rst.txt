Entry-Points: Line Follower
===========================

.. note::
   Eine Gesamtübersicht der API findest du unter :doc:`index`.

**EntryPoints:**

- :ref:`GET /api/agv/linefollower/settings <get-api-agv-line-follower-settings>`
- :ref:`GET /api/agv/linefollower/info <get-api-agv-line-follower-info>`
- :ref:`GET /api/agv/linefollower/sensors <get-api-agv-line-follower-sensors>`
- :ref:`POST /api/agv/linefollower/enable <post-api-agv-line-follower-enable>`
- :ref:`POST /api/agv/linefollower/setSampleDeltaTime <post-api-agv-line-follower-setSampleDeltaTime>`

.. _get-api-agv-line-follower-settings:

Line Follower Sensors – /api/agv/linefollower/settings
------------------------------------------------------

.. http:get:: /api/agv/linefollower/settings

   :synopsis: Liefert die aktuellen Einstellungen des Line Follower-Moduls.
   :reqheader Accept: application/json
   :resheader Content-Type: application/json
   :statuscode 200: Einstellungen erfolgreich abgerufen.

**Beschreibung:**
Liefert die aktuellen Einstellungen des Line Follower-Moduls.

**Response – Success (200):**

.. code-block:: json

    {
      "code": 200,
      "status": "success",
      "data": {
        "enabled": false,
        "sampleDeltaTime":200
      }
    }


**Felder (``data``)**

- ``enabled`` *(bool)* – Line Follower-Modul aktiv/inaktiv.
- ``sampleDeltaTime`` *(int)* – Delta Time in Millisekunden.

.. _get-api-agv-line-follower-info:

Line Follower Info – /api/agv/linefollower/info
------------------------------------------------

.. http:get:: /api/agv/linefollower/info

   :synopsis: Liefert statische Metadaten zum Line-Follower-Sensor.
   :reqheader Accept: application/json
   :resheader Content-Type: application/json
   :statuscode 200: Info erfolgreich abgerufen.

**Beschreibung:**
Liefert Sensor-Metadaten wie Name, I2C-Adresse und Anzahl der verfügbaren Sensoren.

**Response – Success (200):**

.. code-block:: json

    {
      "code": 200,
      "status": "success",
      "data": {
        "name": "Line Follower",
        "i2c_address": "0x11",
        "sensor_count": 5
      }
    }

**Felder (``data``):**

- ``name`` *(string)* – Anzeigename des Sensors.
- ``i2c_address`` *(string)* – I2C-Adresse im Hex-Format (z.B. ``"0x11"``).
- ``sensor_count`` *(int)* – Anzahl der Line-Follower-Eingangskanaele.

.. _get-api-agv-line-follower-sensors:

Line Follower Sensors – /api/agv/linefollower/sensors
-----------------------------------------------------

.. http:get:: /api/agv/linefollower/sensors

   :synopsis: Liefert die Sensorwerte des Line Followers.
   :reqheader Accept: application/json
   :resheader Content-Type: application/json; charset=utf-8
   :statuscode 200: Sensorwerte.

**Beschreibung:**
Liefert für jeden der Sensoren des Line Follower den zuletzt ausgelesenen Wert.
Die Sensorwerte des Line Followers werden intern alle 10ms aktuallisiert.



**Request Body – JSON:**

*leer*

**Response – Success (200):**

.. code-block:: json

  {
    "code": 200,
    "status": "success",
    "data": {
      "timestamp_ms": 55424,
      "sensors": [2,16,202,72,7]
    }
  }

**Felder (``data``):**

  - ``timestamp_ms`` *(unsigned long)* - Relativer Zeitpunkt des auslesesn der Sensorwerte (in Millisekunden).
  - ``sensors`` *(array of integers)* – Liste aller Sensorwerte (Array Index 0–4 entsprechen Sensor 1–5).


.. _post-api-agv-line-follower-enable:

Line Follower Sensors – /api/agv/linefollower/enable
-----------------------------------------------------

.. http:post:: /api/agv/linefollower/enable

   :synopsis: Aktiviert oder deaktiviert das Line Follower-Modul.
   :reqheader Accept: application/json
   :resheader Content-Type: application/json; charset=utf-8
   :statuscode 200: Status erfolgreich gesetzt.
   :statuscode 400: Ungültiger Datentyp oder Wert im Request.

**Beschreibung:** Schaltet das Line Follower-Modul ein/aus. Die Antwort spiegelt den aktuellen Zustand wider.


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


.. _post-api-agv-line-follower-setSampleDeltaTime:

Set Sample Delta Time – /api/agv/linefollower/setSampleDeltaTime
----------------------------------------------------------------

.. http:post:: /api/agv/linefollower/setSampleDeltaTime

   :synopsis: Setzt das Zeit zwischen zwei Anfragen der Line Follower Daten.
   :reqheader Content-Type: application/json
   :resheader Content-Type: application/json
   :jsonparam unsigned int sampleDeltaTime: Delta Time in Millisekunden.
   :statuscode 200: Wert erfolgreich gesetzt.
   :statuscode 400: Ungültiger Datentyp oder Wert im Request.

**Beschreibung:**
Legt fest, in welchem zeitlichen Abstand die Firmware die Werte des Line-Follower-Sensors per Polling abfragt.
Aus diesem Intervall ergibt sich die Frequenz, mit der die Sensordaten aktualisiert werden.

**Request Body – JSON:**

.. code-block:: json

    {
      "sampleDeltaTime": 100
    }

**Response – Success (200):**

.. code-block:: json

    {
      "code": 200,
      "status": "success",
      "data": {
        "sampleDeltaTime": 100
      }
    }

**Response – Error (400 Bad Request):**

.. code-block:: json

  {
    "code": 400,
    "status": "error",
    "details": {
      "shortDesc": "Invalid Value",
      "longDesc": "The 'sampleDeltaTime' key must be of type unsigned integer."
    }
  }