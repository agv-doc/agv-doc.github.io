Entry-Points: LED
=================

.. note::
   Eine Gesamtübersicht der API findest du unter :doc:`index`.

**EntryPoints:**

- :ref:`POST /api/agv/led/off <get-api-agv-led-off>`
- :ref:`POST /api/agv/led/on <post-api-agv-led-on>`
- :ref:`POST /api/agv/led/flashOnce <post-api-agv-led-flashonce>`
- :ref:`POST /api/agv/led/flashInfinite <post-api-agv-led-flashinfinite>`
- :ref:`POST /api/agv/led/flashNTimes <post-api-agv-led-flashntimes>`


.. _get-api-agv-led-off:

LED Off – /api/agv/led/off
--------------------------

.. http:post:: /api/agv/led/off

   :synopsis: Schaltet die LED aus.
   :reqheader Accept: application/json
   :resheader Content-Type: application/json
   :statuscode 200: LED ausgeschaltet.

**Beschreibung:**  
Schaltet die LED sofort aus.

**Request Body – JSON:**  

*leer*

**Response – Success (200):**

.. code-block:: json

   {
     "code": 200,
     "status": "success",
     "data": { "status": "off" }
   }


.. _post-api-agv-led-on:

LED On – /api/agv/led/on
------------------------

.. http:post:: /api/agv/led/on

   :synopsis: Schaltet die LED in einer bestimmten Farbe ein.
   :reqheader Content-Type: application/json
   :resheader Content-Type: application/json
   :jsonparam string color: Eine der Farben ``red``, ``green``, ``blue``, ``yellow``, ``magenta``, ``cyan``, ``white``.
   :statuscode 200: LED eingeschaltet.
   :statuscode 400: Ungültiger Wert/Typ.

**Beschreibung:**  
Schaltet die LED dauerhaft in der angegebenen Farbe ein.

**Request Body – JSON:**

.. code-block:: json

    { 
      "color": "red" 
    }

**Response – Success (200):**

.. code-block:: json

   {
     "code": 200,
     "status": "success",
     "data": { "ledColor": "red" }
   }

**Response – Error (400 Bad Request):**

.. code-block:: json

   {
     "code": 400,
     "status": "error",
     "details": {
       "shortDesc": "Invalid Value",
       "longDesc": "The 'color' value must be one of the following: 'red', 'green', 'blue', 'yellow', 'magenta', 'cyan', 'white'."
     }
   }


.. _post-api-agv-led-flashonce:

LED Flash Once – /api/agv/led/flashOnce
---------------------------------------

.. http:post:: /api/agv/led/flashOnce

   :synopsis: Lässt die LED einmalig in der gewünschten Farbe für eine bestimmte Dauer leuchten.
   :reqheader Content-Type: application/json
   :resheader Content-Type: application/json
   :jsonparam string color: Eine der Farben ``red``, ``green``, ``blue``, ``yellow``, ``magenta``, ``cyan``, ``white``.
   :jsonparam int duration_ms: Leuchtdauer in Millisekunden (> 0).
   :statuscode 200: Flash ausgeführt.
   :statuscode 400: Ungültige Werte/Typen.

**Beschreibung:**  
Schaltet die LED für die angegebene Zeit ein und danach wieder aus.

**Request Body – JSON:**

.. code-block:: json

    { 
      "color": "yellow", 
      "duration_ms": 750 
    }

**Response – Success (200):**

.. code-block:: json

   {
     "code": 200,
     "status": "success",
     "data": { "color": "yellow", "duration_ms": 750 }
   }

**Response – Error (400 Bad Request):**

.. code-block:: json

   {
     "code": 400,
     "status": "error",
     "details": {
       "shortDesc": "Invalid Value",
       "longDesc": "The 'color' value must be one of the following: 'red', 'green', 'blue', 'yellow', 'magenta', 'cyan', 'white'."
     }
   }


.. _post-api-agv-led-flashinfinite:

LED Flash Infinite – /api/agv/led/flashInfinite
-----------------------------------------------

.. http:post:: /api/agv/led/flashInfinite

   :synopsis: Lässt die LED unbegrenzt mit einer bestimmten Frequenz blinken.
   :reqheader Content-Type: application/json
   :resheader Content-Type: application/json
   :jsonparam string color: Eine der Farben ``red``, ``green``, ``blue``, ``yellow``, ``magenta``, ``cyan``, ``white``.
   :jsonparam float flashFrequency_Hz: Blinkfrequenz in Hz (``LED_MIN_FREQUENCY``..``LED_MAX_FREQUENCY``).
   :statuscode 200: Blinksequenz gestartet.
   :statuscode 400: Ungültige Werte/Typen.

**Beschreibung:**  
Startet ein endloses Blinken in der gewählten Farbe und Frequenz.  
Zum Stoppen kann z. B. :ref:`/api/agv/led/off <get-api-agv-led-off>` genutzt werden.

**Request Body – JSON:**

.. code-block:: json

    { 
      "color": "cyan", 
      "flashFrequency_Hz": 2.5 
    }

**Response – Success (200):**

.. code-block:: json

   {
     "code": 200,
     "status": "success",
     "data": { "color": "cyan", "flashFrequency_Hz": 2.5 }
   }

**Response – Error (400 Bad Request):**

.. code-block:: json

   {
     "code": 400,
     "status": "error",
     "details": {
       "shortDesc": "Invalid Value",
       "longDesc": "The 'flashFrequency_Hz' value must be between LED_MIN_FREQUENCY and LED_MAX_FREQUENCY Hz."
     }
   }


.. _post-api-agv-led-flashntimes:

LED Flash N-times – /api/agv/led/flashNTimes
--------------------------------------------

.. http:post:: /api/agv/led/flashNTimes

   :synopsis: Lässt die LED eine endliche Anzahl von Malen blinken.
   :reqheader Content-Type: application/json
   :resheader Content-Type: application/json
   :jsonparam int flashFrequency_Hz: Blinkfrequenz in Hz (``LED_MIN_FREQUENCY``..``LED_MAX_FREQUENCY``).
   :jsonparam int numOfFlashes: Anzahl der Blinkvorgänge (> 0).
   :jsonparam string color: Eine der Farben ``red``, ``green``, ``blue``, ``yellow``, ``magenta``, ``cyan``, ``white``.
   :statuscode 200: Blinksequenz gestartet.
   :statuscode 400: Ungültige Werte/Typen.

**Beschreibung:**  
Blinkt die LED genau ``numOfFlashes``-mal in der angegebenen Farbe mit der gewünschten Frequenz.

**Request Body – JSON:**

.. code-block:: json

    { 
      "flashFrequency_Hz": 4, 
      "numOfFlashes": 6, 
      "color": "magenta" 
    }

**Response – Success (200):**

.. code-block:: json

   {
     "code": 200,
     "status": "success",
     "data": {
       "flashFrequency_Hz": 4,
       "numOfFlashes": 6,
       "color": "magenta"
     }
   }

**Response – Error (400 Bad Request):**

.. code-block:: json

   {
     "code": 400,
     "status": "error",
     "details": {
       "shortDesc": "Invalid Value",
       "longDesc": "The 'flashFrequency_Hz' value must be between LED_MIN_FREQUENCY and LED_MAX_FREQUENCY Hz."
     }
   }
