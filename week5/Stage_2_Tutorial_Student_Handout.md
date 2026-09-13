# Activity 1 - Stakeholder Map
|      Stakeholder       |                                Need                                 |                                      Potential conflict                                       |
| :--------------------: | :-----------------------------------------------------------------: | :-------------------------------------------------------------------------------------------: |
| Reception/Clinic Staff | Quickly register patients, access records, and manage appointments. |   Efficiency may conflict with validation checks that prevent errors or duplicate bookings.   |
|      Practitioner      |      Access accurate schedules and avoid appointment clashes.       |          Practitioner availability may limit the appointment times staff can offer.           |
|        Patient         |         Have accurate personal and appointment information.         | Patient convenience may conflict with identification, cancellation, and privacy requirements. |
|     Clinic Manager     |  Maintain a reliable, manageable, and appropriately scoped system.  | Management may want tight scope and maintainability while users may request addition features |
|  System Administrator  |  Ensure the system is secure, reliable, testable, and consistent.   |             Technical controls may add steps that users consider less convenient.             |

# Activity 2 - Functional or Non-Functional?
|                            Requirement                            | Classification |                                    Reason                                    |
| :---------------------------------------------------------------: | :------------: | :--------------------------------------------------------------------------: |
|      The system shall allow staff to cancel an appointment.       |   Functional   |                  It describes an observable system capacity                  |
| The system should remain responsive for the course-scale dataset. | Non-functional | It describes a performance/quality expectation rather than a business action |
|          The system shall retain cancelled appointments.          |   Functional   |               It specifies a behaviour the system must perform               |
|       Core business logic should be independently testable.       | Non-functional |         It describes a testability/quality property of the software          |
|           The system shall search for a patient by ID.            |   Functional   |                 It specifies an observable search capability                 |

# Activity 3 - Repair Ambiguous Requirements
### 1. The system should be easy to use.
**Problem:** “Easy to use” is subjective and not measurable.\
**Clarification question:** Which tasks should be easy to complete, and how quickly should users complete them?

### 2. Patient search should be fast.
**Problem:**“Fast” does not specify an acceptable response time.\
**Clarification question:** What is the maximum acceptable search response time?

### 3. The system should securely manage data.
**Problem:** The required security controls and authorised users are not specified.\
**Clarification question:** Who can access or modify data, and what security measures are required?

### 4. Appointments should normally be easy to cancel.
**Problem:** “Normally” and “easy” are unclear, and cancellation rules are not defined.\
**Clarification question:** Who can cancel appointments, under what conditions, and should cancelled records be retained?

# Activity 4 - AI Requirements Audit
Classify each suggestion: Confirmed / Assumption requiring validation / Unsupported / Out of scope.

|               AI Suggestion               | Classification |                                      Evidence/reason                                      |
| :---------------------------------------: | :------------: | :---------------------------------------------------------------------------------------: |
|      Patients receive SMS reminders.      |  Unsupported   |                   No requirement states that SMS reminders are needed.                    |
|         Facial recognition login.         |  Out of scope  | This adds complex biometric authentication beyond the small clinic system’s stated scope. |
|    Receptionists create appointments.     |   Confirmed    |            Activity 1 states that reception staff need to create appointments.            |
|              Online payment.              |  Out of scope  |                No payment functionality is mentioned in the requirements.                 |
|       Practitioners view schedules.       |   Confirmed    | Activity 1 states that practitioners need accurate appointment information and schedules. |
|         AI recommends treatments.         |  Out of scope  |       Treatment recommendations are not part of the appointment-management system.        |
| Cancelled appointments remain in history. |   Confirmed    |     Activity 2 explicitly states that the system shall retain cancelled appointments.     |

# Exit question
**Why is 'AI suggested it' not sufficient evidence for a requirement?**\
AI may make assumptions or provide inaccurate information. Requirements must be supported by stakeholder needs, project scope, business rules, or other reliable evidence.