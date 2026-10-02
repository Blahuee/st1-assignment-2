# UML-to-Code Trace
|              UML Element               |           Python Element           | Implemented? |                   Notes                    |
| :------------------------------------: | :--------------------------------: | :----------: | :----------------------------------------: |
|                Patient                 |          `class Patient`           |     Yes      |          Domain class implemented          |
|               patient_id               |         `self.patient_id`          |     Yes      |             Patient identifier             |
|                  name                  |            `self.name`             |     Yes      |                Patient name                |
|                contact                 |           `self.contact`           |     Yes      |      Contact information for Patient       |
|             view_history()             |      `def view_history(self)`      |     Yes      | Displays appointment history for a patient |
|              Practitioner              |        `class Practitioner`        |     Yes      |          Domain class implemented          |
|            practitioner_id             |       `self.practitioner_id`       |     Yes      |          Practitioner identifier           |
|               specialty                |          `self.specialty`          |     Yes      |           Practitioner specialty           |
|            view_schedule()             |     `def view_schedule(self)`      |     Yes      |            Method stub included            |
|              Appointment               |        `class Appointment`         |     Yes      |          Domain class implemented          |
|             appointment_id             |       `self.appointment_id`        |     Yes      |           Appointment identifier           |
|          appointment_datetime          |    `self.appointment_datetime`     |     Yes      |         Appointment date and time          |
|                 status                 |           `self.status`            |     Yes      |             Appointment status             |
|   Appointment → Patient association    |      `self.patient = patient`      |     Yes      |       Appointment references Patient       |
| Appointment → Practitioner association | `self.practitioner = practitioner` |     Yes      |    Appointment references Practitioner     |

# Domain Invariants
|    Class     |                           Invariant / Rule                            |                                      How Protected                                      |
| :----------: | :-------------------------------------------------------------------: | :-------------------------------------------------------------------------------------: |
|   Patient    | Patient contact number must contain only digits and be 10 digits long | contact property setter validates using `isdigit()` and checks length before assignment |
|   Patient    |                     Patient name cannot be empty                      |      Property setter validates that the name is a non-empty string before updating      |
|   Patient    |       A patient can only view appointments that belong to them        |          `view_history()` filters appointments by matching the patient object           |
| Practitioner |                   Practitioner ID must be positive                    |          Validation in `__init__()` raises a `ValueError` if the ID is invalid          |
| Practitioner |                   Practitioner name cannot be empty                   |              `practitioner_name` setter validates input before assignment               |
| Practitioner |                       Specialty cannot be empty                       |                  `specialty` setter validates input before assignment                   |
| Practitioner |          A practitioner can only view their own appointments          |       `view_schedule()` filters appointments by matching the practitioner object        |
| Appointment  |           Every appointment must have an associated patient           |                   Required parameter in the Appointment constructor.                    |
| Appointment  |        Every appointment must have an associated practitioner         |                    Required parameter in the Appointment constructor                    |
| Appointment  |               Cancelled appointments remain in history                |    `cancel()` updates appointment status instead of deleting the appointment object     |

# Composition / Inheritance Decisions
|                        Relationship                        |         Decision          |                                                                  Rationale                                                                  |
| :--------------------------------------------------------: | :-----------------------: | :-----------------------------------------------------------------------------------------------------------------------------------------: |
|                  Appointment and Patient                   | Composition / Association |          An Appointment is associated with a Patient because it is booked for a Patient. An Appointment is not a type of Patient.           |
|                Appointment and Practitioner                | Composition / Association | An Appointment is associated with a Practitioner because it is scheduled with a Practitioner. An Appointment is not a type of Practitioner. |
|           Doctor and Practitioner (hypothetical)           |        Inheritance        |                          A Doctor is a specialised type of Practitioner, making this a valid "is-a" relationship.                           |
|      Appointment → Patient reference (`self.patient`)      | Composition / Association |                     The Python class stores a reference to a Patient object, matching the UML association relationship.                     |
| Appointment → Practitioner reference (`self.practitioner`) | Composition / Association |                  The Python class stores a reference to a Practitioner object, matching the UML association relationship.                   |

# AI Pair-Programming Record
|         AI contribution          | Conforms? | Decision |                Reason                 |            Verification            |
| :------------------------------: | :-------: | :------: | :-----------------------------------: | :--------------------------------: |
| Appointment class implementation |    Yes    | Accepted |      Matches approved UML design      |   Compared with UML and skeleton   |
|      AppointmentStatus enum      |    Yes    | Accepted |   Supports valid appointment states   |        Tested status values        |
|   Status transition validation   |    Yes    | Accepted |          Protects invariants          | Attempted invalid state transition |
|       NotificationManager        |    No     | Rejected |     Not supported by requirements     |        Compared against UML        |
|          Database code           |    No     | Rejected | Outside domain layer responsibilities |   Compared against design rules    |

# Updated UML
**Insert updated UML only if implementation revealed a justified design change. Explain every change.**\
No changes required