# Candidate Concepts
|  Candidate   | Class? |                                                             Reason                                                             |
| :----------: | :----: | :----------------------------------------------------------------------------------------------------------------------------: |
|   Patient    |  yes   |                         Core business entity. The system creates, searches and stores patient records.                         |
| Practitioner |  Yes   |                  Core business entity. The system stores practitioner information and appointment schedules.                   |
| Appointment  |  Yes   |                           Central entity that links patients and practitioners and tracks bookings.                            |
|     Name     |   No   |                             Attribute of Patient and Practitioner, not a separate business object.                             |
|    Clinic    | Maybe  | Could be a class if it has important responsibilities, but the requirements focus on patients, practitioners and appointments. |
|   Database   |   No   |                               Technical implementation detail, not part of the business domain.                                |
| Cancellation |   No   |                                  Usually an action or appointment status rather than a class.                                  |
|    Status    |   No   |                   Better represented as an attribute of Appointment (Booked, Completed, Cancelled, No-Show).                   |

# CRC Cards
### Patient
|     Responsibilities     | Collaborators |
| :----------------------: | :-----------: |
|  Store patient details   |  Appointment  |
| View appointment history | Practitioner  |

### Practitioner
|      Responsibilities      | Collaborators |
| :------------------------: | :-----------: |
| Store practitioner details |  Appointmnt   |
| View appointment schedule  |    Patient    |

### Appointment
|         Responsibilities         | Collaborators |
| :------------------------------: | :-----------: |
| Record appointment date and time |    Patient    |
|     Track appointment status     | Practitioner  |

# Relationship Reasoning
**Patient to Appointment: which relationship and why?**
A Patient can have multiple Appointments over time, but each Appointment is booked for one Patient. This is supported by the appointment booking and patient appointment history requirements.

**Practitioner to Appointment: what multiplicity?**
One Practitioner can have many Appointments, while each Appointment is assigned to one Practitioner. The requirement to prevent double-booking of practitioners implies appointments belong to individual practitioners.

**Should Appointment inherit from Patient?**
No. Appointment is not a type of Patient. Inheritance should only be used for an "is-a" relationship. Instead, Appointment has an association with Patient because appointments are booked for patients.

**Does Clinic need to own every object?**
No. The confirmed requirements focus on Patient, Practitioner, and Appointment. A Clinic may be included as an optional class, but there is no requirement stating that it must own every object in the system. Adding ownership relationships would add unnecessary complexity.

# AI Model Critique
Critique AI proposals: PatientManager, PractitionerManager, AppointmentManager, ClinicController, NotificationManager, ScheduleEngine.
|     AI Proposal     |  Keep?   |                                                                                   Reason                                                                                    |
| :-----------------: | :------: | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------: |
|   PatientManager    |    No    |                         Manages Patient objects but is not a real-world business concept. It is a service/implementation class, not a domain class.                         |
| PractitionerManager |    No    |                                        Similar to PatientManager. Supports system operations but does not represent a domain entity.                                        |
| AppointmentManager  |    No    |                                 Appointments are already represented by the Appointment class. A manager class is an implementation detail.                                 |
|  ClinicController   |    No    |                             A controller belongs to software architecture, not domain modelling. The requirements do not mention a controller.                              |
| NotificationManager |    No    |              Automated notifications are listed as provisional and require client confirmation, so this should not be included in the confirmed domain model.               |
|   ScheduleEngine    | Maybe/No | Preventing scheduling conflicts is required, but a separate engine class is not justified by the requirements. The behaviour can be handled by the Appointment domain model |