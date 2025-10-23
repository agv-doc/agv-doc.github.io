Entry-Points: Buzzer
====================

.. note::
   Eine Gesamtübersicht der API findest du unter :doc:`index`.

**EntryPoints:**

- :ref:`GET /api/agv/buzzer/off <get-api-agv-buzzer-off>`
- :ref:`POST /api/agv/buzzer/on <post-api-agv-buzzer-on>`
- :ref:`POST /api/agv/buzzer/beepOnce <post-api-agv-buzzer-beeponce>`
- :ref:`POST /api/agv/buzzer/beepInifinite <post-api-agv-buzzer-beepinifinite>`
- :ref:`POST /api/agv/buzzer/beepNTimes <post-api-agv-buzzer-beepntimes>`


.. _get-api-agv-buzzer-off:

Buzzer Off -  /api/agv/buzzer/off
---------------------------------

.. http:get:: /api/agv/buzzer/off

   :synopsis: Schaltet den Buzzer aus.
   
   :noindex:

   :reqheader Content-Type: application/json
   :reqheader Authorization: API key
   :resheader Content-Type: application/json

   :queryparam bool silent: Falls gesetzt, deaktiviert den Ton ohne LED-Signal.
   :statuscode 200: Buzzer wurde erfolgreich ausgeschaltet.
   :statuscode 400: Ungültige Anfrageparameter.
   :statuscode 401: Nicht autorisiert.
   :statuscode 500: Interner Serverfehler.


**Authentifizierung:**  
Nicht erforderlich.

**Request**

- **Methode:** ``GET``
- **Headers:**
  - ``Accept: application/json``
- **Query-Parameter:** *keine*

----------------

**Request Body - JSON:**

 *keiner*

----------------

**Erfolg (200):**

.. code-block:: json

   {
     "code": 200,
     "status": "success",
     "data": {
       "status": "off"
     }
   }

**Beschreibung der Felder (``data``):**

- ``status`` *(string)* – Aktueller Zustand des Buzzers.  
  Gibt an, ob der Buzzer ausgeschaltet (``"off"``) ist.


.. _post-api-agv-buzzer-on:

Buzzer On -  /api/agv/buzzer/on
-------------------------------

**Zweck:**  
Schaltet den Buzzer ein und aktiviert einen Dauerton mit der angegebenen Frequenz.

**Authentifizierung:**  
Nicht erforderlich.

**Request**

- **Methode:** ``POST``
- **Headers:**
  - ``Accept: application/json``
- **Query-Parameter:** *keine*

----------------

**Request Body - JSON:**

.. code-block:: json

   {
     "toneFrequency_Hz": 2000
   }

**Parameter**

   - ``toneFrequency_Hz`` *(int, required)* – Tonfrequenz in Hz.

----------------

**Response - Success (200):**

.. code-block:: json

   {
     "code": 200,
     "status": "success",
     "data": {
       "toneFrequency_Hz": 2000
     }
   }

**Beschreibung der Felder (``data``):**

- ``toneFrequency_Hz`` *(integer)* – Tatsächlich aktivierte Frequenz des Buzzers in Hertz.  
  Wird in der Antwort zurückgegeben, um zu bestätigen, dass der Buzzer mit diesem Wert eingeschaltet wurde.

----------------


**Response - Error (400 Bad Request):**


.. code-block:: json

    {
    "code": 400,
    "status": "error",
    "details": {
        "shortDesc": "Invalid Value",
        "longDesc": "The 'toneFrequency_Hz' value must be between 200 and 2000 Hz."
        }
    }



.. _post-api-agv-buzzer-beeponce:

Beep Once - /api/agv/buzzer/beepOnce
------------------------------------

**Zweck:**  
Löst einen einzelnen Piepton mit der angegebenen Frequenz für die angegebene Dauer aus.

**Request**

- **Methode:** ``POST``
- **Headers:** ``Accept: application/json``
- **Body (optional):**

.. code-block:: json

    {
    "toneFrequency_Hz": 200,
    "duration_ms": 5000
    }


**Response - Success (200):**

.. code-block:: json

    {
        "code": 200,
        "status": "success",
        "data": {
            "toneFrequency_Hz": 200,
            "duration_ms": 5000
        }
    }

**Parameter**

   - ``toneFrequency_Hz`` *(int, required)* – Tonfrequenz in Hz.
   - ``duration_ms`` *(int, required)* – Tondauer in Millisekunden.

----------------


**Response - Error (400 Bad Request):**


.. code-block:: json

    {
    "code": 400,
    "status": "error",
    "details": {
        "shortDesc": "Invalid Value",
        "longDesc": "The 'toneFrequency_Hz' value must be between 200 and 2000 Hz."
      }
    }


.. _post-api-agv-buzzer-beepinifinite:

Beep Inifinite -  /api/agv/buzzer/beepInifinite
-----------------------------------------------

**Zweck:**  
Startet einen Dauerton, der erst durch `/off` beendet wird.

**Request**

- **Methode:** ``POST``
- **Headers:** ``Accept: application/json``

**Erfolg (200)**

.. code-block:: json

   {
     "code": 200,
     "status": "success",
     "data": {
       "message": "beep infinite started"
     }
   }



.. _post-api-agv-buzzer-beepntimes:

Beep N-times -  /api/agv/buzzer/beepNTimes
------------------------------------------

**Zweck:**  
Löst mehrere Pieptöne hintereinander aus.

**Request**

- **Methode:** ``POST``
- **Headers:** ``Accept: application/json``
- **Body:**

.. code-block:: json

   {
     "count": 3,
     "intervalMs": 300,
     "durationMs": 150
   }

**Erfolg (200)**

.. code-block:: json

   {
     "code": 200,
     "status": "success",
     "data": {
       "message": "beep 3 times"
     }
   }


