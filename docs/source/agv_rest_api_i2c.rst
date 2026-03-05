Entry-Points: I2C Scanner
==========================

.. note::
   Eine Gesamtübersicht der API findest du unter :doc:`index`.

**EntryPoints:**

- :ref:`GET /api/agv/i2c/scan <get-api-agv-i2c-scan>`


.. _get-api-agv-i2c-scan:

I2C Device Scanner - /api/agv/i2c/scan
---------------------------------------

.. http:get:: /api/agv/i2c/scan

   :synopsis: Scannt den I2C-Bus und liefert eine Liste aller angeschlossenen Geräte.
   :reqheader Accept: application/json
   :resheader Content-Type: application/json
   :statuscode 200: OK

**Beschreibung:**
Führt einen Scan des I2C-Busses durch und gibt alle erkannten Geräte zurück.
Der Scanner testet die Adressen 0x01 bis 0x7E und kann bis zu 4 Geräte speichern.

**Response – Success (200):**

.. code-block:: json

   {
     "code": 200,
     "status": "success",
     "data": {
       "devicesFound": 2,
       "devices": [
         {
           "index": 1,
           "address_dec": 32,
           "address_hex": "0x20",
           "name": "-"
         },
         {
           "index": 2,
           "address_dec": 104,
           "address_hex": "0x68",
           "name": "-"
         }
       ]
     }
   }

**Felder (``data``)**

- ``devicesFound`` *(integer)* – Anzahl der auf dem Bus erkannten Geräte (0–4).
- ``devices`` *(array)* – Liste der erkannten Geräte mit folgenden Eigenschaften:

  - ``index`` *(integer)* – Laufende Nummer des Geräts (1-basiert).
  - ``address_dec`` *(integer)* – I2C-Adresse in dezimaler Notation (1–126).
  - ``address_hex`` *(string)* – I2C-Adresse in hexadezimaler Notation (z.B. ``"0x20"``).
  - ``name`` *(string)* – Name/Beschreibung des Geräts (derzeit ``"-"``; für zukünftige Erweiterung reserviert).

**Response – No Devices Found (200):**

.. code-block:: json

   {
     "code": 200,
     "status": "success",
     "data": {
       "devicesFound": 0,
       "devices": []
     }
   }

**Technische Details:**

- Die Scan-Funktion prüft die Präsenz von Geräten über ``Wire.beginTransmission()`` und ``Wire.endTransmission()``.
- Maximal 4 Geräte werden in der Antwort aufgelistet (``I2C_ADDRESSBUFFERSIZE = 4``).
- Der Scan berücksichtigt nur Standard-Adressen (0x01–0x7E); reservierte Adressen (0x00, 0x7F) werden ignoriert.
- Weitere Details zur Geräte-Identifikation (z.B. Gerätetypenerkennung) sind für zukünftige Versionen geplant.
