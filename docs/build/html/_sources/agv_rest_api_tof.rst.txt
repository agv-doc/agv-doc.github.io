Entry-Points: ToF Sensor
========================

.. note::
   Eine Gesamtuebersicht der API findest du unter :doc:`index`.

**EntryPoints:**

- :ref:`GET /api/agv/tof/distance <get-api-agv-tof-distance>`
- :ref:`GET /api/agv/tof/enable <get-api-agv-tof-enable>`
- :ref:`POST /api/agv/tof/enable <post-api-agv-tof-enable>`
- :ref:`GET /api/agv/tof/info <get-api-agv-tof-info>`


.. _get-api-agv-tof-distance:

ToF Distance - /api/agv/tof/distance
-------------------------------------

.. http:get:: /api/agv/tof/distance

   :synopsis: Liefert die aktuelle Distanzmessung des ToF-Sensors.
   :reqheader Accept: application/json
   :resheader Content-Type: application/json
   :statuscode 200: Messwert erfolgreich gelesen.

**Beschreibung:**
Liefert die zuletzt gemessene Distanz in Millimetern inklusive Zeitstempel und Sensorstatus.

**Response - Success (200):**

.. code-block:: json

    {
      "code": 200,
      "status": "success",
      "data": {
        "distance_mm": 384,
        "timestamp_ms": 92144,
        "enabled": true,
        "status": "ok"
      }
    }

**Response - Sensorfehler (200):**

.. code-block:: json

    {
      "code": 200,
      "status": "success",
      "data": {
        "distance_mm": null,
        "enabled": true,
        "status": "error"
      }
    }

**Felder (``data``):**

- ``distance_mm`` *(int|null)* - Gemessene Distanz in mm oder ``null`` bei Fehler.
- ``timestamp_ms`` *(unsigned long)* - Relativer Zeitstempel der Messung (nur bei ``status = "ok"``).
- ``enabled`` *(bool)* - Aktueller Enable-Status des ToF-Moduls.
- ``status`` *(string)* - ``"ok"`` oder ``"error"``.


.. _get-api-agv-tof-enable:

ToF Enable Status - /api/agv/tof/enable
----------------------------------------

.. http:get:: /api/agv/tof/enable

   :synopsis: Liefert den aktuellen Enable-Status des ToF-Moduls.
   :reqheader Accept: application/json
   :resheader Content-Type: application/json
   :statuscode 200: Status erfolgreich abgerufen.

**Response - Success (200):**

.. code-block:: json

    {
      "code": 200,
      "status": "success",
      "data": {
        "enabled": true
      }
    }

**Felder (``data``):**

- ``enabled`` *(bool)* - Aktueller Enable-Status.


.. _post-api-agv-tof-enable:

ToF Enable Set - /api/agv/tof/enable
-------------------------------------

.. http:post:: /api/agv/tof/enable

   :synopsis: Aktiviert oder deaktiviert den ToF-Sensor logisch.
   :reqheader Content-Type: application/json
   :resheader Content-Type: application/json
   :jsonparam bool enable: ``true`` zum Aktivieren, ``false`` zum Deaktivieren.
   :statuscode 200: Status erfolgreich gesetzt.
   :statuscode 400: Ungueltiger Datentyp im Request.

**Beschreibung:**
Setzt den Enable-Status des ToF-Moduls. Die Antwort spiegelt den aktuellen Zustand wider.

**Request Body - JSON:**

.. code-block:: json

    {
      "enable": true
    }

**Response - Success (200):**

.. code-block:: json

    {
      "code": 200,
      "status": "success",
      "data": {
        "enabled": true
      }
    }

**Response - Error (400 Bad Request):**

.. code-block:: json

    {
      "code": 400,
      "status": "error",
      "details": {
        "shortDesc": "Invalid Value",
        "longDesc": "The 'enable' key must be of type bool."
      }
    }


.. _get-api-agv-tof-info:

ToF Info - /api/agv/tof/info
-----------------------------

.. http:get:: /api/agv/tof/info

   :synopsis: Liefert statische Metadaten zum ToF-Sensor.
   :reqheader Accept: application/json
   :resheader Content-Type: application/json
   :statuscode 200: Info erfolgreich abgerufen.

**Response - Success (200):**

.. code-block:: json

    {
      "code": 200,
      "status": "success",
      "data": {
        "name": "ToF Distance",
        "i2c_address": "0x29",
        "type": "VL53L0X"
      }
    }

**Felder (``data``):**

- ``name`` *(string)* - Anzeigename des Sensors.
- ``i2c_address`` *(string)* - I2C-Adresse im Hex-Format.
- ``type`` *(string)* - Sensorbezeichnung/Modell.
