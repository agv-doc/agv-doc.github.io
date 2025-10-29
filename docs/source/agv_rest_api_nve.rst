Entry-Points: NVS (Non-Volatile Storage)
========================================

.. note::
   Eine Gesamtübersicht der API findest du unter :doc:`index`.

**EntryPoints:**

- :ref:`GET /api/nve/namespaces <get-api-nve-namespaces>`
- :ref:`POST /api/nve/listKeysAndValues <post-api-nve-listkeysandvalues>`


.. _get-api-nve-namespaces:

List NVS Namespaces – /api/nve/namespaces
-----------------------------------------

.. http:get:: /api/nve/namespaces

   :synopsis: Gibt alle in der NVS-Partition vorhandenen Namespaces zurück.
   :reqheader Accept: application/json
   :resheader Content-Type: application/json
   :statuscode 200: Erfolgreich.
   :statuscode 403: Zugriff verweigert.

**Beschreibung:**  
Liest die NVS-Partition des ESP32 aus und listet alle vorhandenen Namespaces (z. B. Module, Konfigurationsbereiche) auf.

**Response – Success (200):**

.. code-block:: json

   {
     "code": 200,
     "status": "success",
     "data": {
       "namespaces": [
         "wifi",
         "system",
         "agv_settings",
         "sensors"
       ]
     }
   }

**Felder (``data``):**

- ``namespaces`` *(array of string)* – Liste aller vorhandenen Namespace-Namen in der NVS-Partition.


.. _post-api-nve-listkeysandvalues:

List Keys and Values – /api/nve/listKeysAndValues
-------------------------------------------------

.. http:post:: /api/nve/listKeysAndValues

   :synopsis: Listet alle Schlüssel und deren Werte innerhalb eines gegebenen NVS-Namespaces.
   :reqheader Content-Type: application/json
   :resheader Content-Type: application/json
   :jsonparam string namespace: Name des auszulesenden Namespaces.
   :statuscode 200: Erfolgreich.
   :statuscode 400: Ungültiger Wert/Typ.
   :statuscode 403: Zugriff verweigert.
   :statuscode 500: Interner Fehler beim Zugriff auf NVS.

**Beschreibung:**  
Öffnet den angegebenen NVS-Namespace und liest alle enthaltenen Schlüssel, Datentypen und Werte aus.  
Unterstützt werden alle NVS-Typen (z. B. ``int32``, ``string``, ``blob``).

**Request Body – JSON:**

.. code-block:: json

    { 
      "namespace": "agv" 
    }

**Response – Success (200):**

.. code-block:: json

   {
     "code": 200,
     "status": "success",
     "data": {
       "namespace": "wifi",
       "items": [
         { "key": "ssid", "typeId": 33, "typeName": "string", "value": "MyWiFi" },
         { "key": "pw", "typeId": 33, "typeName": "string", "value": "12345678" },
         { "key": "channel", "typeId": 4, "typeName": "int32", "value": 6 }
       ]
     }
   }

**Felder (``data``):**

- ``namespace`` *(string)* – Der angefragte Namespace.  
- ``items`` *(array of object)* – Schlüssel-Wert-Paare des Namespaces.
  - ``key`` *(string)* – Schlüsselname  
  - ``typeId`` *(int)* – NVS-interne Typ-ID  
  - ``typeName`` *(string)* – Menschlich lesbarer Typ (z. B. ``int32``, ``string``, ``blob``)  
  - ``value`` *(mixed)* – Wert (je nach Typ Zahl, String oder Byte-Array)

**Response – Error (400 Bad Request):**

.. code-block:: json

   {
     "code": 400,
     "status": "error",
     "details": {
       "shortDesc": "Invalid Value",
       "longDesc": "The 'namespace' key must be of type string."
     }
   }

**Response – Error (500 Internal Server Error):**

.. code-block:: json

   {
     "code": 500,
     "status": "error",
     "details": {
       "shortDesc": "NVS Error",
       "longDesc": "Failed to open NVS namespace: wifi"
     }
   }
