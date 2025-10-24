Entry-Points: WiFi
==================

.. note::
   Eine Gesamtübersicht der API findest du unter :doc:`index`.

**EntryPoints:**

- :ref:`GET /api/agv/wifi/getWifiSettings <get-api-agv-wifi-settings>`
- :ref:`POST /api/agv/wifi/setActiveMode <post-api-agv-wifi-setactivemode>`
- :ref:`POST /api/agv/wifi/setModeData <post-api-agv-wifi-setmodedata>`


.. _get-api-agv-wifi-settings:

WiFi Settings – /api/agv/wifi/getWifiSettings
---------------------------------------------

.. http:get:: /api/agv/wifi/getWifiSettings

   :synopsis: Liefert den aktiven WiFi-Modus und gespeicherte Zugangsdaten (AP, WiFi-01, WiFi-02).
   :reqheader Accept: application/json
   :resheader Content-Type: application/json; charset=utf-8
   :statuscode 200: Einstellungen erfolgreich abgerufen.

**Beschreibung:**  
Gibt den aktuell gesetzten WiFi-Modus sowie die aus dem NVS gespeicherten SSIDs und Passwörter
für die Profile **AP**, **wifi-01** und **wifi-02** zurück.

**Response – Success (200):**

.. code-block:: json

   {
     "code": 200,
     "status": "success",
     "data": {
       "wifiMode": "wifi-01",
       "ap":   { "ssid": "agv-ap", "passwd": "ap-password" },
       "wifi_01": { "ssid": "home-wifi", "passwd": "secret-123" },
       "wifi_02": { "ssid": "lab-wifi",  "passwd": "lab-secret" }
     }
   }

**Felder (``data``)**

- ``wifiMode`` *(string)* – Aktiver Modus: ``"ap"``, ``"wifi-01"`` oder ``"wifi-02"``.  
- **ap** *(object)* – Zugangsdaten für Access-Point-Modus.  
  - ``ssid`` *(string)*, ``passwd`` *(string)*  
- **wifi_01** *(object)* – Zugangsdaten Profil 1.  
  - ``ssid`` *(string)*, ``passwd`` *(string)*  
- **wifi_02** *(object)* – Zugangsdaten Profil 2.  
  - ``ssid`` *(string)*, ``passwd`` *(string)*


.. _post-api-agv-wifi-setactivemode:

Set Active WiFi Mode – /api/agv/wifi/setActiveMode
--------------------------------------------------

.. http:post:: /api/agv/wifi/setActiveMode

   :synopsis: Setzt den aktiven WiFi-Modus.
   :reqheader Content-Type: application/json
   :resheader Content-Type: application/json; charset=utf-8
   :jsonparam string newMode: Neuer Modus, einer von ``"ap"``, ``"wifi-01"``, ``"wifi-02"``.
   :statuscode 200: Modus erfolgreich gesetzt.
   :statuscode 400: Ungültiger Wert/Typ.
   :statuscode 403: Zugriff verweigert.

**Beschreibung:**  
Aktiviert den angegebenen WiFi-Modus. Die Antwort spiegelt den tatsächlich gesetzten Modus wider.

**Request Body – JSON:**

.. code-block:: json

    { 
      "newMode": "wifi-02" 
    }

**Response – Success (200):**

.. code-block:: json

   {
     "code": 200,
     "status": "success",
     "data": { "newMode": "wifi-02" }
   }

**Response – Error (400 Bad Request):**

.. code-block:: json

   {
     "code": 400,
     "status": "error",
     "details": {
       "shortDesc": "Bad Request",
       "longDesc": "The key 'newMode' can only have the values 'ap', 'wifi-01' or 'wifi-02'."
     }
   }


.. _post-api-agv-wifi-setmodedata:

Set WiFi Mode Data – /api/agv/wifi/setModeData
-----------------------------------------------

.. http:post:: /api/agv/wifi/setModeData

   :synopsis: Hinterlegt SSID und Passwort für ein WiFi-Profil (AP, wifi-01 oder wifi-02).
   :reqheader Content-Type: application/json
   :resheader Content-Type: application/json; charset=utf-8
   :jsonparam string mode: Zielprofil: ``"ap"``, ``"wifi-01"``, ``"wifi-02"``.
   :jsonparam string ssid: SSID (Länge 1..32 Zeichen).
   :jsonparam string passwd: Passwort (Länge 8..63 Zeichen).
   :statuscode 200: Zugangsdaten erfolgreich gespeichert.
   :statuscode 400: Ungültige Werte/Typen.
   :statuscode 403: Zugriff verweigert.

**Beschreibung:**  
Speichert SSID und Passwort für das gewählte Profil im NVS. Die Antwort enthält die
soeben gesetzten Werte.

**Request Body – JSON:**

.. code-block:: json

   {
     "mode": "wifi-01",
     "ssid": "home-wifi",
     "passwd": "secret-123"
   }

**Response – Success (200):**

.. code-block:: json

   {
     "code": 200,
     "status": "success",
     "data": {
       "mode": "wifi-01",
       "ssid": "home-wifi",
       "passwd": "secret-123"
     }
   }

**Response – Error (400 Bad Request):**

.. code-block:: json

   {
     "code": 400,
     "status": "error",
     "details": {
       "shortDesc": "Bad Request",
       "longDesc": "The key 'mode' can only have the values 'ap', 'wifi-01' or 'wifi-02'."
     }
   }
