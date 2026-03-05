Entry-Points: Info
==================

.. note::
   Eine Gesamtübersicht der API findest du unter :doc:`index`.

**EntryPoints:**

- :ref:`GET /api/info/agv <get-api-info-agv>`
- :ref:`GET /api/info/esp32/chip <get-api-info-esp32-chip>`
- :ref:`GET /api/info/esp32/network <get-api-info-esp32-network>`
- :ref:`GET /api/info/esp32/partitions <get-api-info-esp32-partitions>`
- :ref:`GET /api/info/esp32/tasks <get-api-info-esp32-tasks>`


.. _get-api-info-agv:

AGV Info – /api/info/agv
-------------------------

.. http:get:: /api/info/agv

   :synopsis: Liefert allgemeine Informationen zum AGV-System.
   :reqheader Accept: application/json
   :resheader Content-Type: application/json
   :statuscode 200: Informationen erfolgreich abgerufen.

**Beschreibung:**
Dieser Endpunkt liefert allgemeine Systeminformationen über das AGV,
darunter Betriebszeit, Name, eindeutige ID und Firmware-Details.

**Response – Success (200):**

.. code-block:: json

   {
     "code": 200,
     "status": "success",
     "data": {
       "uptime_sec": 2845.399,
       "agv_name": "agv_WIUEuh",
       "agv_uniqueID": "unused--",
       "firmware": {
         "compile_date": "25-10-24",
         "compile_time": "16:37",
         "compile_datetime": "25-10-24 16:37",
         "version": "1.1.154"
       }
     }
   }

**Felder (``data``)**

- ``uptime_sec`` *(float)* – Laufzeit des Systems in Sekunden.
- ``agv_name`` *(string)* – Aktuell konfigurierter Name des AGV.
- ``agv_uniqueID`` *(string)* – Eindeutige Identifikationsnummer des AGV (optional).

- **firmware** *(object)* – Firmware-Informationen
   - ``compile_date`` *(string)* – Kompilierungsdatum (TT-MM-JJ).
   - ``compile_time`` *(string)* – Kompilierungszeit (HH:MM).
   - ``compile_datetime`` *(string)* – Kombination aus Datum und Zeit.
   - ``version`` *(string)* – Firmware-Versionsnummer.



.. _get-api-info-esp32-chip:

ESP32 Chip Info – /api/info/esp32/chip
--------------------------------------

.. http:get:: /api/info/esp32/chip

   :synopsis: Liefert Systeminformationen über den ESP32-Chip.
   :reqheader Accept: application/json
   :resheader Content-Type: application/json
   :statuscode 200: Informationen erfolgreich abgerufen.

**Beschreibung:**
Dieser Endpunkt liefert detaillierte Hardware- und Systeminformationen über den ESP32-Chip,
einschließlich Speicher, CPU, Flash-Parameter, Chip-Details und des letzten Reset-Grundes.
Er dient primär zu Diagnose- und Monitoring-Zwecken.

**Response – Success (200):**

.. code-block:: json

   {
     "code": 200,
     "status": "success",
     "data": {
       "memory": {
         "free_heap_bytes": 166548,
         "min_free_heap_bytes": 100408,
         "max_alloc_heap_bytes": 110580,
         "total_heap": 306156
       },
       "cpu": {
         "frequency_mhz": 240,
         "core_count": 2
       },
       "flash": {
         "chip_size_bytes": 4194304,
         "chip_mode": 2,
         "chip_speed_hz": 40000000
       },
       "chip": {
         "revision": 3,
         "model": "ESP32-D0WD-V3",
         "sdk_version": "v4.4.7-dirty",
         "chip_id": "cdf9d108"
       },
       "reset": {
         "reason_id": 1,
         "reason_desc": "Power-on Reset"
       }
     }
   }

**Felder (``data``)**

- **memory** *(object)* – Speicherinformationen
   - ``free_heap_bytes`` *(int)* – Aktuell verfügbarer Heap-Speicher.
   - ``min_free_heap_bytes`` *(int)* – Minimaler Heap-Speicher während der Laufzeit.
   - ``max_alloc_heap_bytes`` *(int)* – Größter zusammenhängender Heap-Block.
   - ``total_heap`` *(int)* – Gesamter verfügbarer Heap.

- **cpu** *(object)* – Prozessorinformationen
   - ``frequency_mhz`` *(int)* – CPU-Frequenz in MHz.
   - ``core_count`` *(int)* – Anzahl der CPU-Kerne.

- **flash** *(object)* – Flash-Speicherparameter
   - ``chip_size_bytes`` *(int)* – Gesamtkapazität des Flash-Chips.
   - ``chip_mode`` *(int)* – Betriebsmodus des Flash (z. B. QIO/DIO).
   - ``chip_speed_hz`` *(int)* – Taktfrequenz des Flash-Speichers.

- **chip** *(object)* – Chip-spezifische Details
   - ``revision`` *(int)* – Hardware-Revision.
   - ``model`` *(string)* – Modellbezeichnung des ESP32-Chips.
   - ``sdk_version`` *(string)* – Version der verwendeten ESP-IDF.
   - ``chip_id`` *(string)* – Eindeutige Chip-ID.

- **reset** *(object)* – Informationen zum letzten Reset
   - ``reason_id`` *(int)* – Reset-Code.
   - ``reason_desc`` *(string)* – Textbeschreibung des Reset-Grundes (z. B. „Power-on Reset“).






.. _get-api-info-esp32-network:

ESP32 Network Info – /api/info/esp32/network
--------------------------------------------

.. http:get:: /api/info/esp32/network

   :synopsis: Liefert Netzwerk- und WLAN-Informationen des ESP32.
   :reqheader Accept: application/json
   :resheader Content-Type: application/json
   :statuscode 200: Informationen erfolgreich abgerufen.

**Beschreibung:**
Dieser Endpunkt liefert aktuelle Netzwerk- und WLAN-Parameter des ESP32,
einschließlich IP-Konfiguration, MAC-Adresse, Hostname, WLAN-SSID, RSSI und Kanal.

**Response – Success (200):**

.. code-block:: json

   {
     "code": 200,
     "status": "success",
     "data": {
       "network": {
         "mac_address": "08:D1:F9:CD:5F:5C",
         "ip_address": "192.168.1.132",
         "subnet_mask": "255.255.255.0",
         "ip_gateway": "192.168.1.254",
         "ip_dns": "8.8.8.8",
         "hostname": "esp32-agv",
         "ipv6": "0000:0000:0000:0000:0000:0000:0000:0000"
       },
       "wifi": {
         "rssi_dBm": -52,
         "ssid": "dd-wrt",
         "bssid": "F4:4D:5C:FB:BD:EC",
         "connection_status": 3,
         "wifi_mode": 1,
         "channel": 1
       }
     }
   }

**Felder (``data``)**

- **network** *(object)* – Netzwerkparameter
   - ``mac_address`` *(string)* – MAC-Adresse des ESP32.
   - ``ip_address`` *(string)* – Aktuelle IPv4-Adresse.
   - ``subnet_mask`` *(string)* – Subnetzmaske.
   - ``ip_gateway`` *(string)* – Standard-Gateway.
   - ``ip_dns`` *(string)* – DNS-Server-Adresse.
   - ``hostname`` *(string)* – Gerätename im Netzwerk.
   - ``ipv6`` *(string)* – IPv6-Adresse (falls konfiguriert).

- **wifi** *(object)* – WLAN-Statusinformationen
   - ``rssi_dBm`` *(int)* – Empfangsfeldstärke in dBm.
   - ``ssid`` *(string)* – Aktuell verbundene WLAN-SSID.
   - ``bssid`` *(string)* – MAC-Adresse des Access Points.
   - ``connection_status`` *(int)* – WLAN-Verbindungsstatuscode.
   - ``wifi_mode`` *(int)* – WLAN-Betriebsmodus (z. B. Station, AP, etc.).
   - ``channel`` *(int)* – Aktueller WLAN-Kanal.






.. _get-api-info-esp32-partitions:

ESP32 Partition Info – /api/info/esp32/partitions
-------------------------------------------------

.. http:get:: /api/info/esp32/partitions

   :synopsis: Liefert Informationen über die Partitionstabelle des ESP32.
   :reqheader Accept: application/json
   :resheader Content-Type: application/json
   :statuscode 200: Informationen erfolgreich abgerufen.

**Beschreibung:**
Dieser Endpunkt gibt eine Liste aller Partitionen des Flash-Speichers zurück,
einschließlich Start- und Endadressen, Typ, Größe und Verschlüsselungsstatus.

**Response – Success (200):**

.. code-block:: json

   {
     "code": 200,
     "status": "success",
     "data": {
       "partitions": [
         {
           "name": "nvs",
           "type": "data",
           "subtype": "nvs",
           "address_begin": "0x00009000",
           "address_end": "0x0000e000",
           "size_bytes": 20480,
           "size_hex_bytes": "0x00005000",
           "encrypted": "no"
         },
         {
           "name": "otadata",
           "type": "data",
           "subtype": "ota",
           "address_begin": "0x0000e000",
           "address_end": "0x00010000",
           "size_bytes": 8192,
           "size_hex_bytes": "0x00002000",
           "encrypted": "no"
         },
         {
           "name": "app0",
           "type": "app",
           "subtype": "ota_0",
           "address_begin": "0x00010000",
           "address_end": "0x00210000",
           "size_bytes": 2097152,
           "size_hex_bytes": "0x00200000",
           "encrypted": "no"
         },
         {
           "name": "spiffs",
           "type": "data",
           "subtype": "spiffs",
           "address_begin": "0x00210000",
           "address_end": "0x003f0000",
           "size_bytes": 1966080,
           "size_hex_bytes": "0x001e0000",
           "encrypted": "no"
         },
         {
           "name": "coredump",
           "type": "data",
           "subtype": "coredump",
           "address_begin": "0x003f0000",
           "address_end": "0x00400000",
           "size_bytes": 65536,
           "size_hex_bytes": "0x00010000",
           "encrypted": "no"
         }
       ]
     }
   }

**Felder (``data``)**

- **partitions** *(array)* – Liste der Partitionseinträge.
  Jeder Eintrag enthält folgende Felder:

   - ``name`` *(string)* – Name der Partition.
   - ``type`` *(string)* – Typ der Partition (z. B. ``app`` oder ``data``).
   - ``subtype`` *(string)* – Untertyp der Partition (z. B. ``nvs``, ``spiffs``).
   - ``address_begin`` *(string)* – Startadresse im Flash.
   - ``address_end`` *(string)* – Endadresse im Flash.
   - ``size_bytes`` *(int)* – Größe der Partition in Bytes.
   - ``size_hex_bytes`` *(string)* – Größe in hexadezimaler Schreibweise.
   - ``encrypted`` *(string)* – Gibt an, ob die Partition verschlüsselt ist (``"yes"``/``"no"``).


.. _get-api-info-esp32-tasks:

ESP32 Tasks Information – /api/info/esp32/tasks
-----------------------------------------------

.. http:get:: /api/info/esp32/tasks

   :synopsis: Liefert FreeRTOS-Task- und Reset-Informationen des ESP32.
   :reqheader Accept: application/json
   :resheader Content-Type: application/json
   :statuscode 200: Informationen erfolgreich abgerufen.

**Beschreibung:**
Dieser Endpunkt liefert Informationen über FreeRTOS-Tasks und den letzten Reset-Grund des ESP32.

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

**Reset-Gründe-Referenz:**

Die möglichen Reset-Grund-Codes sind:

- ``0`` – Power-on Reset
- ``1`` – External Reset
- ``2`` – Watchdog Reset
- ``3`` – Software Reset
- ``4`` – RTC Reset
- ``5`` – Deep Sleep Reset

**Hinweis:**
Die detaillierten Task-Informationen (Taskname, Stack-Größe, Priorität) sind derzeit nicht aktiviert
und können bei Bedarf im Backend freigeschaltet werden.
