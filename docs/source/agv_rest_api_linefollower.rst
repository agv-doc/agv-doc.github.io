Entry-Points: Line Follower
===========================

.. note::
   Eine Gesamtübersicht der API findest du unter :doc:`index`.

**EntryPoints:**

- :ref:`GET /api/agv/linefollower/sensors <get-api-agv-line-follower-sensors>`

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


