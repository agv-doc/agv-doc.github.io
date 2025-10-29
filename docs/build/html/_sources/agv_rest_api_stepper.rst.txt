Entry-Points: Stepper
=====================

.. note::
   Eine Gesamtübersicht der API findest du unter :doc:`index`.

**EntryPoints:**

- :ref:`POST /api/agv/stepper/setVelocity <post-api-agv-stepper-setvelocity>`
- :ref:`POST /api/agv/stepper/enable <post-api-agv-stepper-enable>`
- :ref:`GET /api/agv/stepper/isMoving <get-api-agv-stepper-ismoving>`
- :ref:`GET /api/agv/stepper/motionMode <get-api-agv-stepper-motionmode>`
- :ref:`GET /api/agv/stepper/abortMotion <get-api-agv-stepper-abortmotion>`
- :ref:`GET /api/agv/stepper/resetPosition <get-api-agv-stepper-resetposition>`
- :ref:`GET /api/agv/stepper/getCurrentVelocity <get-api-agv-stepper-getcurrentvelocity>`
- :ref:`GET /api/agv/stepper/getCurrentPosition <get-api-agv-stepper-getcurrentposition>`
- :ref:`POST /api/agv/stepper/setVelocitySingle <post-api-agv-stepper-setvelocitysingle>`
- :ref:`POST /api/agv/stepper/setMaxVelocityPerc <post-api-agv-stepper-setmaxvelocityperc>`
- :ref:`POST /api/agv/stepper/setMaxAccelerationPerc <post-api-agv-stepper-setmaxaccelerationperc>`
- :ref:`POST /api/agv/stepper/setMoveAbsolute <post-api-agv-stepper-setmoveabsolute>`
- :ref:`POST /api/agv/stepper/setMoveRelative <post-api-agv-stepper-setmoverelative>`


.. _post-api-agv-stepper-setvelocity:

Set Velocity (beide) – /api/agv/stepper/setVelocity
---------------------------------------------------

.. http:post:: /api/agv/stepper/setVelocity

   :synopsis: Setzt die Zielgeschwindigkeit beider Schrittmotoren in % der Maximalgeschwindigkeit.
   :reqheader Content-Type: application/json
   :resheader Content-Type: application/json
   :jsonparam float velLeft_perc: Zielgeschwindigkeit linker Motor (Bereich ``-100.0`` bis ``100.0``).
   :jsonparam float velRight_perc: Zielgeschwindigkeit rechter Motor (Bereich ``-100.0`` bis ``100.0``).
   :statuscode 200: Geschwindigkeiten gesetzt.
   :statuscode 400: Ungültige Werte oder fehlende Felder.

**Request Body – JSON:**

.. code-block:: json

    { 
     "velLeft_perc": -20.0, 
     "velRight_perc": 20.0 
    }

**Response – Success (200):**

.. code-block:: json

   {
     "code": 200,
     "status": "success",
     "data": { "velLeft_perc": -20.0, 
               "velRight_perc": 20.0 
              }
   }

**Response – Error (400):**

- *Invalid Value* – Werte außerhalb ``[-100.0, 100.0]`` oder falsche Typen.
- *Missing Key* – Erforderliche Felder fehlen.


.. _post-api-agv-stepper-enable:

Enable/Disable – /api/agv/stepper/enable
----------------------------------------

.. http:post:: /api/agv/stepper/enable

   :synopsis: Aktiviert oder deaktiviert die Schrittmotor-Treiber.
   :reqheader Content-Type: application/json
   :resheader Content-Type: application/json
   :jsonparam string stepper: ``"on"`` oder ``"off"``.
   :statuscode 200: Zustand gesetzt.
   :statuscode 400: Ungültiger Wert oder fehlendes Feld.

**Request Body – JSON:**

.. code-block:: json

    { 
     "stepper": "on" 
    }

**Response – Success (200):**

.. code-block:: json

    {
     "code": 200,
     "status": "success",
     "data": { "stepper": "on" }
    }

**Response – Error (400):**
- *Invalid Value* – ``stepper`` nicht einer der erlaubten Werte.


.. _get-api-agv-stepper-ismoving:

Is Moving – /api/agv/stepper/isMoving
-------------------------------------

.. http:get:: /api/agv/stepper/isMoving

   :synopsis: Prüft, ob gerade eine Bewegung aktiv ist.
   :resheader Content-Type: application/json
   :statuscode 200: Status geliefert.

**Response – Success (200):**

.. code-block:: json

   {
     "code": 200,
     "status": "success",
     "data": { "isMoving": true }
   }


.. _get-api-agv-stepper-motionmode:

Motion Mode – /api/agv/stepper/motionMode
-----------------------------------------

.. http:get:: /api/agv/stepper/motionMode

   :synopsis: Liefert den aktuellen Bewegungsmodus.
   :resheader Content-Type: application/json
   :statuscode 200: Modus geliefert.

**Beschreibung:**  
Mögliche Werte: ``"idle"``, ``"velocity"``, ``"position"``, ``"position_planning"``, ``"mode_unknown"``.

**Response – Success (200):**

.. code-block:: json

   {
     "code": 200,
     "status": "success",
     "data": { "motionMode": "velocity" }
   }


.. _get-api-agv-stepper-abortmotion:

Abort Motion – /api/agv/stepper/abortMotion
-------------------------------------------

.. http:get:: /api/agv/stepper/abortMotion

   :synopsis: Bricht die aktuelle Bewegung ab.
   :resheader Content-Type: application/json
   :statuscode 200: Abbruch initiiert.

**Response – Success (200):**

.. code-block:: json

   {
     "code": 200,
     "status": "success",
     "data": { "aborted": true }
   }


.. _get-api-agv-stepper-resetposition:

Reset Position – /api/agv/stepper/resetPosition
-----------------------------------------------

.. http:get:: /api/agv/stepper/resetPosition

   :synopsis: Setzt die aktuelle Position beider Motoren zurück.
   :resheader Content-Type: application/json
   :statuscode 200: Position zurückgesetzt.
   :statuscode 400: Stepper Busy – Zurücksetzen während Bewegung nicht möglich.

**Response – Success (200):**

.. code-block:: json

   {
     "code": 200,
     "status": "success",
     "data": { "positionReset": true }
   }

**Response – Error (400):**

- *Stepper Busy* – Motoren bewegen sich noch.


.. _get-api-agv-stepper-getcurrentvelocity:

Get Current Velocity – /api/agv/stepper/getCurrentVelocity
----------------------------------------------------------

.. http:get:: /api/agv/stepper/getCurrentVelocity

   :synopsis: Liefert aktuelle Winkelgeschwindigkeit beider Motoren.
   :resheader Content-Type: application/json
   :statuscode 200: Geschwindigkeiten geliefert.

**Beschreibung:**  

Die Einheit ist **rad/s**. Zusätzlich wird die konfigurierte Maximalgeschwindigkeit mitgeliefert.

**Response – Success (200):**

.. code-block:: json

   {
     "code": 200,
     "status": "success",
     "data": {
       "leftVelocity": 1.2,
       "rightVelocity": -0.8,
       "unit": "radPerSec",
       "maxVelocity": 12.34
     }
   }


.. _get-api-agv-stepper-getcurrentposition:

Get Current Position – /api/agv/stepper/getCurrentPosition
----------------------------------------------------------

.. http:get:: /api/agv/stepper/getCurrentPosition

   :synopsis: Liefert die aktuelle Position (Steps) beider Motoren.
   :resheader Content-Type: application/json
   :statuscode 200: Position geliefert.

**Beschreibung:**  

Die Einheit ist **Steps**; zusätzlich wird ``stepsPerRevolution`` mitgeliefert.

**Response – Success (200):**

.. code-block:: json

   {
     "code": 200,
     "status": "success",
     "data": {
       "leftPosition": 1234,
       "rightPosition": -567,
       "unit": "steps",
       "stepsPerRevolution": 200
     }
   }


.. _post-api-agv-stepper-setvelocitysingle:

Set Velocity (einzeln) – /api/agv/stepper/setVelocitySingle
-----------------------------------------------------------

.. http:post:: /api/agv/stepper/setVelocitySingle

   :synopsis: Setzt die Zielgeschwindigkeit eines einzelnen Motors in % der Maximalgeschwindigkeit.
   :reqheader Content-Type: application/json
   :resheader Content-Type: application/json
   :jsonparam float vel_perc: Zielgeschwindigkeit (Bereich ``-100.0`` bis ``100.0``).
   :jsonparam string stepper: Zielmotor ``"left"`` oder ``"right"``.
   :statuscode 200: Geschwindigkeit gesetzt.
   :statuscode 400: Ungültige Werte/Typen oder fehlende Felder.

**Request Body – JSON:**

.. code-block:: json

    { "vel_perc": 35.0,
    "stepper": "left" 
    }

**Response – Success (200):**

.. code-block:: json

   {
     "code": 200,
     "status": "success",
     "data": { "stepper": "left", "vel_perc": 35.0 }
   }

**Response – Error (400):**

- *Invalid Value* – ``vel_perc`` außerhalb ``[-100.0, 100.0]`` oder ``stepper`` nicht ``left|right``.


.. _post-api-agv-stepper-setmaxvelocityperc:

Set Max Velocity % – /api/agv/stepper/setMaxVelocityPerc
--------------------------------------------------------

.. http:post:: /api/agv/stepper/setMaxVelocityPerc

   :synopsis: Setzt die maximale Geschwindigkeit (global) in Prozent.
   :reqheader Content-Type: application/json
   :resheader Content-Type: application/json
   :jsonparam float maxVel_perc: Prozentwert (Bereich ``0.0`` bis ``100.0``).
   :statuscode 200: Maximalgeschwindigkeit gesetzt.
   :statuscode 400: Ungültiger Wert/Typ oder Motoren bewegen sich (State).

**Beschreibung:**  
Wenn die Motoren noch laufen, kann die Maximalgeschwindigkeit nicht gesetzt werden.

**Request Body – JSON:**

.. code-block:: json

   { 
     "maxVel_perc": 80.0 
   }

**Response – Success (200):**

.. code-block:: json

   {
     "code": 200,
     "status": "success",
     "data": {
       "maxVel_perc": 80.0,
       "maxVel_radPerSec": 9.87
     }
   }

**Response – Error (400):**

- *Invalid Value* – Außerhalb ``[0.0, 100.0]`` oder falscher Typ.
- *Invalid State* – Änderung während Bewegung nicht möglich.


.. _post-api-agv-stepper-setmaxaccelerationperc:

Set Max Acceleration % – /api/agv/stepper/setMaxAccelerationPerc
----------------------------------------------------------------

.. http:post:: /api/agv/stepper/setMaxAccelerationPerc

   :synopsis: Setzt die maximale Beschleunigung (global) in Prozent.
   :reqheader Content-Type: application/json
   :resheader Content-Type: application/json
   :jsonparam float maxAcc_perc: Prozentwert (Bereich ``0.0`` bis ``100.0``).
   :statuscode 200: Maximale Beschleunigung gesetzt.
   :statuscode 400: Ungültiger Wert/Typ oder Motoren bewegen sich (State).

**Request Body – JSON:**

.. code-block:: json

   { 
     "maxAcc_perc": 60.0 
   }

**Response – Success (200):**

.. code-block:: json

   {
     "code": 200,
     "status": "success",
     "data": {
       "maxAcc_perc": 60.0,
       "maxAcc_radPerSec2": 12.34
     }
   }

**Response – Error (400):**

- *Invalid Value* – Außerhalb ``[0.0, 100.0]`` oder falscher Typ.
- *Invalid State* – Änderung während Bewegung nicht möglich.


.. _post-api-agv-stepper-setmoveabsolute:

Move Absolute – /api/agv/stepper/setMoveAbsolute
------------------------------------------------

.. http:post:: /api/agv/stepper/setMoveAbsolute

   :synopsis: Startet eine Positionsbewegung beider Motoren auf absolute Zielpositionen (Steps).
   :reqheader Content-Type: application/json
   :resheader Content-Type: application/json
   :jsonparam long leftPos_steps: Zielposition linker Motor in Steps.
   :jsonparam long rightPos_steps: Zielposition rechter Motor in Steps.
   :statuscode 200: Bewegung gestartet.
   :statuscode 400: Ungültige Werte/Typen oder Motoren beschäftigt.

**Request Body – JSON:**

.. code-block:: json

   { 
     "leftPos_steps": 1200, 
     "rightPos_steps": -800 
    }

**Response – Success (200):**

.. code-block:: json

   {
     "code": 200,
     "status": "success",
     "data": { 
                "leftPos_steps": 1200,
                "rightPos_steps": -800 
              }
   }

**Response – Error (400):**

- *Invalid Value* – Falsche Typen.
- *Invalid State* – Motoren sind beschäftigt (busy).


.. _post-api-agv-stepper-setmoverelative:

Move Relative – /api/agv/stepper/setMoveRelative
------------------------------------------------

.. http:post:: /api/agv/stepper/setMoveRelative

   :synopsis: Startet eine Relativbewegung beider Motoren (Delta in Steps).
   :reqheader Content-Type: application/json
   :resheader Content-Type: application/json
   :jsonparam long leftDelta_steps: Schritt-Differenz linker Motor.
   :jsonparam long rightDelta_steps: Schritt-Differenz rechter Motor.
   :statuscode 200: Bewegung gestartet.
   :statuscode 400: Ungültige Werte/Typen oder Motoren beschäftigt.

**Request Body – JSON:**

.. code-block:: json

    { 
     "leftDelta_steps": -200, 
     "rightDelta_steps": 200 
    }

**Response – Success (200):**

.. code-block:: json

   {
     "code": 200,
     "status": "success",
     "data": { "leftDelta_steps": -200, "rightDelta_steps": 200 }
   }

**Response – Error (400):**

- *Invalid Value* – Falsche Typen.
- *Invalid State* – Motoren sind beschäftigt (busy).
