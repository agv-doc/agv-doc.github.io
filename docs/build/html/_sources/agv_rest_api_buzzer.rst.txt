Entry-Points: Buzzer
====================

.. note::
   Eine Gesamtübersicht der API findest du unter :doc:`index`.

**EntryPoints:**

- :ref:`GET /api/agv/buzzer/off <get-api-agv-buzzer-off>`
- :ref:`POST /api/agv/buzzer/on <post-api-agv-buzzer-on>`
- :ref:`POST /api/agv/buzzer/beepOnce <post-api-agv-buzzer-beeponce>`
- :ref:`POST /api/agv/buzzer/beepInfinite <post-api-agv-buzzer-beepinfinite>`
- :ref:`POST /api/agv/buzzer/beepNTimes <post-api-agv-buzzer-beepntimes>`


.. _get-api-agv-buzzer-off:

Buzzer Off - /api/agv/buzzer/off
--------------------------------

.. http:get:: /api/agv/buzzer/off

   :synopsis: Schaltet den Buzzer aus.
   :reqheader Content-Type: application/json
   :resheader Content-Type: application/json; charset=utf-8
   :statuscode 200: Buzzer wurde erfolgreich ausgeschaltet.
   :statuscode 400: Ungültige Anfrageparameter.

**Beschreibung:**  
Schaltet den Buzzer aus und beendet alle aktiven Töne.

**Response – Success (200):**

.. code-block:: json

   {
     "code": 200,
     "status": "success",
     "data": {
       "status": "off"
     }
   }

**Felder (``data``)**

- ``status`` *(string)* – Aktueller Zustand des Buzzers (``"off"``).


.. _post-api-agv-buzzer-on:

Buzzer On - /api/agv/buzzer/on
------------------------------

.. http:post:: /api/agv/buzzer/on

   :synopsis: Schaltet den Buzzer ein.
   :reqheader Content-Type: application/json
   :resheader Content-Type: application/json; charset=utf-8
   :jsonparam int toneFrequency_Hz: Tonfrequenz in Hz.
   :statuscode 200: Buzzer wurde erfolgreich eingeschaltet.
   :statuscode 400: Ungültige Anfrageparameter.

**Beschreibung:**  
Schaltet den Buzzer ein und aktiviert einen Dauerton mit der angegebenen Frequenz.

**Request Body – JSON:**

.. code-block:: json

   {
     "toneFrequency_Hz": 2000
   }

**Response – Success (200):**

.. code-block:: json

   {
     "code": 200,
     "status": "success",
     "data": {
       "toneFrequency_Hz": 2000
     }
   }

**Felder (``data``):**

- ``toneFrequency_Hz`` *(integer)* – Tatsächlich aktivierte Frequenz des Buzzers in Hertz.

**Response – Error (400 Bad Request):**

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

.. http:post:: /api/agv/buzzer/beepOnce

   :synopsis: Löst einen einzelnen Piepton aus.
   :reqheader Content-Type: application/json
   :resheader Content-Type: application/json; charset=utf-8
   :jsonparam int toneFrequency_Hz: Tonfrequenz in Hz.
   :jsonparam int duration_ms: Tondauer in Millisekunden.
   :statuscode 200: Piepton ausgelöst.
   :statuscode 400: Ungültige Anfrageparameter.

**Beschreibung:**  
Löst einen einzelnen Piepton mit der angegebenen Frequenz für die angegebene Dauer aus.

**Request Body – JSON:**

.. code-block:: json

   {
     "toneFrequency_Hz": 200,
     "duration_ms": 5000
   }

**Response – Success (200):**

.. code-block:: json

   {
     "code": 200,
     "status": "success",
     "data": {
       "toneFrequency_Hz": 200,
       "duration_ms": 5000
     }
   }

**Response – Error (400 Bad Request):**

.. code-block:: json

   {
     "code": 400,
     "status": "error",
     "details": {
       "shortDesc": "Invalid Value",
       "longDesc": "The 'toneFrequency_Hz' value must be between 200 and 2000 Hz."
     }
   }


.. _post-api-agv-buzzer-beepinfinite:

Beep Infinite - /api/agv/buzzer/beepInfinite
--------------------------------------------

.. http:post:: /api/agv/buzzer/beepInfinite

   :synopsis: Löst ein dauerhaftes Piepen aus (Stop per ``/off``).
   :reqheader Content-Type: application/json
   :resheader Content-Type: application/json; charset=utf-8
   :jsonparam int toneFrequency_Hz: Tonfrequenz in Hz.
   :jsonparam float beepFrequency_Hz: Piepton-Frequenz in Hz (Beep-Zyklen pro Sekunde).
   :statuscode 200: Dauerpiepen gestartet.
   :statuscode 400: Ungültige Anfrageparameter.

**Beschreibung:**  
Startet ein dauerhaftes Piepen mit der angegebenen Frequenz, das erst durch ``/off`` beendet wird.

**Request Body – JSON:**

.. code-block:: json

   {
     "toneFrequency_Hz": 200,
     "beepFrequency_Hz": 0.1
   }

**Response – Success (200):**

.. code-block:: json

   {
     "code": 200,
     "status": "success",
     "data": {
       "toneFrequency_Hz": 200,
       "beepFrequency_Hz": 0.1
     }
   }

**Felder (``data``)**

- ``toneFrequency_Hz`` *(integer)* – Tatsächlich aktivierte Frequenz des Buzzers in Hertz.
- ``beepFrequency_Hz`` *(float)* – Tatsächlich aktivierte Piepton-Frequenz in Hz.


.. _post-api-agv-buzzer-beepntimes:

Beep N-times - /api/agv/buzzer/beepNTimes
-----------------------------------------

.. http:post:: /api/agv/buzzer/beepNTimes

   :synopsis: Löst mehrere Pieptöne hintereinander aus.
   :reqheader Content-Type: application/json
   :resheader Content-Type: application/json; charset=utf-8
   :jsonparam int numOfBeeps:   Anzahl der Pieptöne.
   :jsonparam int toneFrequency_Hz: Tonfrequenz in Hz.
   :jsonparam int beepFrequency_Hz: Piepton-Frequenz in Hz (Beep-Zyklen pro Sekunde).
   :statuscode 200: Sequenz ausgelöst.
   :statuscode 400: Ungültige Anfrageparameter.

**Beschreibung:**  
Löst mehrere Pieptöne hintereinander aus.

**Request Body – JSON:**

.. code-block:: json

  {
    "toneFrequency_Hz": 200,
    "beepFrequency_Hz": 0.5,
    "numOfBeeps": 4
  }


**Response – Success (200):**

.. code-block:: json

  {
    "code": 200,
    "status": "success",
    "data": {
      "toneFrequency_Hz": 200,
      "beepFrequency_Hz": 0.5,
      "numOfBeeps": 4
    }
  }
