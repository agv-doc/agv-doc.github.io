Entry-Points: ESP32 System Information
=====================================

.. note::
   Eine Gesamtübersicht der API findest du unter :doc:`index`.

**EntryPoints:**

- :ref:`GET /api/agv/info/esp32/chip <get-api-agv-info-esp32-chip>`
- :ref:`GET /api/agv/info/esp32/network <get-api-agv-info-esp32-network>`
- :ref:`GET /api/agv/info/esp32/partitions <get-api-agv-info-esp32-partitions>`
- :ref:`GET /api/agv/info/esp32/tasks <get-api-agv-info-esp32-tasks>`


.. _get-api-agv-info-esp32-chip:

ESP32 Chip & System Information - /api/agv/info/esp32/chip
-----------------------------------------------------------

.. http:get:: /api/agv/info/esp32/chip

   :synopsis: Detaillierte Informationen zum ESP32 Chip, CPU, Flash und Speicher.
   :reqheader Accept: application/json
   :resheader Content-Type: application/json
   :statuscode 200: OK

**Beschreibung:**
Liefert umfassende Systeminformationen des ESP32, einschließlich Chip-Modell, CPU-Frequenz,
Heap-Speicher und Flash-Konfiguration.

**Response – Success (200):**

.. code-block:: json

   {
     "code": 200,
     "status": "success",
     "data": {
       "memory": {
         "free_heap_bytes": 102456,
         "min_free_heap_bytes": 45678,
         "max_alloc_heap_bytes": 512000,
         "total_heap": 327680
       },
       "cpu": {
         "frequency_mhz": 240,
         "core_count": 2
       },
       "flash": {
         "chip_size_bytes": 4194304,
         "chip_mode": 0,
         "chip_speed_hz": 40000000
       },
       "chip": {
         "revision": 3,
         "model": "ESP32",
         "sdk_version": "v4.4.2",
         "chip_id": "aabbccddee"
       },
       "reset": {
         "reason_id": 1,
         "reason_desc": "Power-on reset"
       }
     }
   }

**Felder (``data``)**

**``memory``** – Heap-Speicher-Informationen:

- ``free_heap_bytes`` *(integer)* – Aktuell freier Heap-Speicher in Bytes.
- ``min_free_heap_bytes`` *(integer)* – Minimale verfügbare Heap-Größe seit dem Boot.
- ``max_alloc_heap_bytes`` *(integer)* – Maximale Größe für eine einzelne Heap-Allokation.
- ``total_heap`` *(integer)* – Gesamte Heap-Größe in Bytes.

**``cpu``** – CPU-Informationen:

- ``frequency_mhz`` *(integer)* – aktuelle CPU-Frequenz in MHz.
- ``core_count`` *(integer)* – Anzahl der CPU-Kerne.

**``flash``** – Flash-Speicher-Informationen:

- ``chip_size_bytes`` *(integer)* – Gesamtgröße des Flash-Chips in Bytes.
- ``chip_mode`` *(integer)* – Flash-Betriebsmodus (0=QIO, 1=QOUT, 2=DIO, 3=DOUT).
- ``chip_speed_hz`` *(integer)* – Flash-Lesegeschwindigkeit in Hertz.

**``chip``** – Chip-Identifikationsinformationen:

- ``revision`` *(integer)* – Chip-Revisionsversion.
- ``model`` *(string)* – Chip-Modellname (z.B. ``"ESP32"``, ``"ESP32-S3"``).
- ``sdk_version`` *(string)* – ESP-IDF SDK-Versionsnummer.
- ``chip_id`` *(string)* – Eindeutige Chip-ID (Hexadezimalformat).

**``reset``** – Reset-Grund:

- ``reason_id`` *(integer)* – Numerischer Reset-Grund-Code.
- ``reason_desc`` *(string)* – Menschlich lesbare Beschreibung des Reset-Grundes.


.. _get-api-agv-info-esp32-network:

Network Information - /api/agv/info/esp32/network
--------------------------------------------------

.. http:get:: /api/agv/info/esp32/network

   :synopsis: Netzwerkkonfiguration und MAC-Adressen.
   :reqheader Accept: application/json
   :resheader Content-Type: application/json
   :statuscode 200: OK

**Beschreibung:**
Liefert Netzwerkeinstellungen einschließlich MAC-Adressen für WiFi und Bluetooth sowie
IP-Konfiguration.

**Response – Success (200):**

.. code-block:: json

   {
     "code": 200,
     "status": "success",
     "data": {
       "wifi_mac": "AA:BB:CC:DD:EE:FF",
       "bt_mac": "AA:BB:CC:DD:EE:00",
       "hostname": "AGV-Device",
       "ip_address": "192.168.1.100",
       "subnet_mask": "255.255.255.0",
       "gateway": "192.168.1.1",
       "dns_server": "192.168.1.1"
     }
   }

**Felder (``data``)**

- ``wifi_mac`` *(string)* – MAC-Adresse des WiFi-Adapters (Format: ``AA:BB:CC:DD:EE:FF``).
- ``bt_mac`` *(string)* – MAC-Adresse des Bluetooth-Adapters.
- ``hostname`` *(string)* – Netzwerk-Hostname des Geräts.
- ``ip_address`` *(string)* – Aktuelle IPv4-Adresse.
- ``subnet_mask`` *(string)* – Subnetzmaske.
- ``gateway`` *(string)* – Standard-Gateway-Adresse.
- ``dns_server`` *(string)* – Primärer DNS-Server.


.. _get-api-agv-info-esp32-partitions:

Partition Information - /api/agv/info/esp32/partitions
-------------------------------------------------------

.. http:get:: /api/agv/info/esp32/partitions

   :synopsis: Übersicht der Partitionstabelle und deren Größen.
   :reqheader Accept: application/json
   :resheader Content-Type: application/json
   :statuscode 200: OK

**Beschreibung:**
Liefert detaillierte Informationen zur Partitionstabelle des ESP32, einschließlich
Partitionstypen, Adressen und Verschlüsselungsstatus.

**Response – Success (200):**

.. code-block:: json

   {
     "code": 200,
     "status": "success",
     "data": {
       "partitions": [
         {
           "name": "nvs",
           "type": "DATA",
           "subtype": "NVS",
           "address_begin": "0x00009000",
           "address_end": "0x0000d000",
           "size_bytes": 16384,
           "size_hex_bytes": "0x00004000",
           "encrypted": "no"
         },
         {
           "name": "otadata",
           "type": "DATA",
           "subtype": "OTA",
           "address_begin": "0x0000d000",
           "address_end": "0x0000f000",
           "size_bytes": 8192,
           "size_hex_bytes": "0x00002000",
           "encrypted": "no"
         },
         {
           "name": "app0",
           "type": "APP",
           "subtype": "OTA_0",
           "address_begin": "0x00010000",
           "address_end": "0x00200000",
           "size_bytes": 1966080,
           "size_hex_bytes": "0x001f0000",
           "encrypted": "no"
         }
       ]
     }
   }

**Felder (``data.partitions``)**

Jede Partition ist ein Objekt mit:

- ``name`` *(string)* – Partitionsbezeichnung (z.B. ``"nvs"``, ``"app0"``, ``"spiffs"``).
- ``type`` *(string)* – Partitionstyp (``"APP"`` für Anwendungen, ``"DATA"`` für Daten).
- ``subtype`` *(string)* – Untertyp der Partition (z.B. ``"OTA_0"``, ``"NVS"``, ``"SPIFFS"``).
- ``address_begin`` *(string)* – Startadresse im Hexadezimalformat.
- ``address_end`` *(string)* – Endadresse im Hexadezimalformat.
- ``size_bytes`` *(integer)* – Partitionsgröße in Bytes.
- ``size_hex_bytes`` *(string)* – Partitionsgröße in Hexadezimalformat.
- ``encrypted`` *(string)* – Verschlüsselungsstatus (``"yes"`` oder ``"no"``).


.. _get-api-agv-info-esp32-tasks:

FreeRTOS Task Information - /api/agv/info/esp32/tasks
------------------------------------------------------

.. http:get:: /api/agv/info/esp32/tasks

   :synopsis: Informationen über aktuelle FreeRTOS Tasks und Reset-Grund.
   :reqheader Accept: application/json
   :resheader Content-Type: application/json
   :statuscode 200: OK

**Beschreibung:**
Liefert Informationen über aktuell laufende FreeRTOS-Tasks und den Reset-Grund des Systems.

**Response – Success (200):**

.. code-block:: json

   {
     "code": 200,
     "status": "success",
     "memory": {},
     "reset": {
       "reset_reason": 1
     }
   }

**Felder**

- ``reset.reset_reason`` *(integer)* – Numerischer Code des letzten Reset-Grundes.

**Hinweis:**
Die Task-Detailinformationen (Taskname, Stack-Größe, Priorität) sind zurzeit
kommentiert und können bei Bedarf aktiviert werden.
