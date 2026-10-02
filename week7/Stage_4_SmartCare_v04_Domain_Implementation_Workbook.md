# UML-to-Code Trace
|              UML Element               |            Python Element            | Implemented? |                Notes                |
| :------------------------------------: | :----------------------------------: | :----------: | :---------------------------------: |
|                Patient                 |           `class Patient`            |     Yes      |      Domain class implemented       |
|               patient_id               |          `self.patient_id`           |     Yes      |         Patient identifier          |
|                  name                  |             `self.name`              |     Yes      |            Patient name             |
|            contact_details             |        `self.contact_details`        |     Yes      |         Contact information         |
|             view_history()             |       `def view_history(self)`       |     Yes      | Displays appointment history for a patient |
|              Practitioner              |         `class Practitioner`         |     Yes      |      Domain class implemented       |
|            practitioner_id             |        `self.practitioner_id`        |     Yes      |       Practitioner identifier       |
|               specialty                |           `self.specialty`           |     Yes      |       Practitioner specialty        |
|            view_schedule()             |      `def view_schedule(self)`       |     Yes      |        Method stub included         |
|              Appointment               |         `class Appointment`          |     Yes      |      Domain class implemented       |
|             appointment_id             |        `self.appointment_id`         |     Yes      |       Appointment identifier        |
|          appointment_datetime          |     `self.appointment_datetime`      |     Yes      |      Appointment date and time      |
|                 status                 |            `self.status`             |     Yes      |         Appointment status          |
|                cancel()                |          `def cancel(self)`          |     Yes      |        Method stub included         |
|              reschedule()              | `def reschedule(self, new_datetime)` |     Yes      |        Method stub included         |
|            check_conflict()            |      `def check_conflict(self)`      |     Yes      |        Method stub included         |
|   Appointment → Patient association    |       `self.patient = patient`       |     Yes      |   Appointment references Patient    |
| Appointment → Practitioner association |  `self.practitioner = practitioner`  |     Yes      | Appointment references Practitioner |

# Domain Invariants
|    Class     |                 Invariant / Rule                 |                  How Protected                   |
| :----------: | :----------------------------------------------: | :----------------------------------------------: |
|   Patient    |              Patient ID must exist               |     Set during object creation (`__init__`)      |
|   Patient    |           Patient name cannot be empty           |            Validation in constructor             |
| Practitioner |            Practitioner ID must exist            |     Set during object creation (`__init__`)      |
| Practitioner |            Specialty must be provided            |            Validation in constructor             |
| Appointment  |    Appointment must have exactly one Patient     |     Constructor requires `patient` reference     |
| Appointment  |  Appointment must have exactly one Practitioner  |  Constructor requires `practitioner` reference   |
| Appointment  |    Status must be a valid appointment status     |         Use an `AppointmentStatus` enum          |
| Appointment  | Cancelled appointments cannot be cancelled again | Checked inside `cancel()` before changing status |

# Composition / Inheritance Decisions
|                        Relationship                        |         Decision          |                                                                  Rationale                                                                  |
| :--------------------------------------------------------: | :-----------------------: | :-----------------------------------------------------------------------------------------------------------------------------------------: |
|                  Appointment and Patient                   | Composition / Association |          An Appointment is associated with a Patient because it is booked for a Patient. An Appointment is not a type of Patient.           |
|                Appointment and Practitioner                | Composition / Association | An Appointment is associated with a Practitioner because it is scheduled with a Practitioner. An Appointment is not a type of Practitioner. |
|           Doctor and Practitioner (hypothetical)           |        Inheritance        |                          A Doctor is a specialised type of Practitioner, making this a valid "is-a" relationship.                           |
|      Appointment → Patient reference (`self.patient`)      | Composition / Association |                     The Python class stores a reference to a Patient object, matching the UML association relationship.                     |
| Appointment → Practitioner reference (`self.practitioner`) | Composition / Association |                  The Python class stores a reference to a Practitioner object, matching the UML association relationship.                   |

# AI Pair-Programming Record
|         AI contribution          | Conforms? | Decision |                 Reason                 |            Verification             |
| :------------------------------: | :-------: | :------: | :------------------------------------: | :---------------------------------: |
| Appointment class implementation |    Yes    | Accepted |      Matches approved UML design.      |   Compared with UML and skeleton.   |
|      AppointmentStatus enum      |    Yes    | Accepted |   Supports valid appointment states.   |        Tested status values.        |
|   Status transition validation   |    Yes    | Accepted |          Protects invariants.          | Attempted invalid state transition. |
|       NotificationManager        |    No     | Rejected |     Not supported by requirements.     |        Compared against UML.        |
|          Database code           |    No     | Rejected | Outside domain layer responsibilities. |   Compared against design rules.    |

# Updated UML
Insert updated UML only if implementation revealed a justified design change. Explain every change.