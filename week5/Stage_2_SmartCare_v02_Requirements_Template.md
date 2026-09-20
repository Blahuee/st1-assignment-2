# Part A - Client Brief: AI OFF
Smartcare currently uses spreadsheets and paper records, causing:

1. Duplicate bookings
2. Difficulty finding patient information
3. Inconsistent appointment status
4. Limited appointment history

Management wants a small, maintainable system for patients, practitioners and appointments.

# Part B - Stakeholders and Scope: AI OFF
### Stakeholders
|      Stakeholder       |                                Need                                 |
| :--------------------: | :-----------------------------------------------------------------: |
| Reception/Clinic Staff | Quickly register patients, access records, and manage appointments. |
|      Practitioner      |      Access accurate schedules and avoid appointment clashes.       |
|        Patient         |         Have accurate personal and appointment information.         |
|     Clinic Manager     |  Maintain a reliable, manageable, and appropriately scoped system.  |
|  System Administrator  |  Ensure the system is secure, reliable, testable, and consistent.   |

### In Scope
- Patient registration
- Patient Search
- Practitioner registration
- Appointment creation
- Prevention of conflicting active practitioner appointments
- Appointment cancellation
- Retention of cancelled appointments in history
- Preservation of relevant data between sessions

### Out of Scope
- Facial recognition login
- Online payment
- AI diagnosis/treatment recommendations
- Insurance processing
- Other features with no current stakeholder evidence

### Provisional/Requires Validation
- SMS reminders
- Practitioner schedule view
- Exact role permissions
- Exact performance targets
- Exact retention rules

# Part C - Functional Requirements: AI OFF
**FR-01:** The system shall allow staff to register a new patient.\
**FR-02:** The system shall prevent cancelled appointments from being treated as active bookings.\
**FR-03:** The system shall allow staff to update patient details.\
**FR-04:** The system shall allow staff to search for a patient.\
**FR-05:** The system shall allow staff to record practitioner details.\
**FR-06:** The system shall allow staff to create an appointment.\
**FR-07:** The system shall prevent appointments from being created when the practitioner already has an active appointment at that time.\
**FR-08:** The system shall allow staff to view a practitioner’s appointment schedule.\
**FR-09:** The system shall allow staff to cancel an active appointment.\
**FR-10:** The system shall retain cancelled appointments in the appointment history.\
**FR-11:** The system shall reject a booking if the practitioner, time/date or patient is missing.

# Part D - Non-Functional Requirements: AI OFF
**NFR-01 – Reliability:** The system should maintain accurate patient, practitioner, and appointment records during normal operation.\
**NFR-02 – Data integrity:** The system shall prevent duplicate patient's and conflicting active appointments.\
**NFR-03 – Usability:** A trained receptionist should be able to create, search for, and cancel an appointment without technical assistance.\
**NFR-04 – Maintainability:** Core business logic should be separated from the user interface so it can be modified and maintained independently.\
**NFR-05 – Testability:** Patient, practitioner, and appointment operations should be independently testable using repeatable test data.\
**NFR-06 – Responsiveness:** Common searches and appointment actions should provide a response within an acceptable time for the course-scale dataset.

# Part E - User Stories and Acceptance Criteria: AI OFF
### User Stories
**US-01:** As a receptionist, I want to register a patient so that their details can be stored accurately.\
**US-02:** As a receptionist, I want to create an appointment so that a patient can be scheduled with a practitioner.\
**US-03:** As a receptionist, I want to cancel an appointment so that unavailable bookings are not treated as active.\
**US-04:** As a practitioner, I want to view my schedule so that I can see my upcoming appointments.\
**US-05:** As a clinic manager, I want cancelled appointments retained in history so that appointment records remain complete.

### Acceptance criteria
**AC-01 - Successful patient registration:**\
**GIVEN:** valid patient details are entered\
**WHEN:** the receptionist saves the patient\
**THEN:** the system confirms the patient doesn't already exist and stores the record.

**AC-02 - Successful appointment creation:**\
**GIVEN:** a patient, practitioner, and available time are selected\
**WHEN:** staff save the appointment\
**THEN:** the appointment is created with an active status.

**AC-03 - Conflicting appointment creation:**\
**GIVEN:** the practitioner already has an active appointment at that time.\
**WHEN:** staff try to create another appointment\
**THEN:** the system rejects the booking and displays a conflict message

### Assumptions and Open Questions
- Assumed: Patients are identified by name only
# Part F - AI Requirements Review:
**Prompt:** Act as a software requirements reviewer. Review the SmartCare requirements for ambiguity, inconsistency, missing clarification questions and testability. Do NOT invent new client requirements. For every suggestion, state whether it is based on evidence or is only a question/assumption requiring validation.

# Part G - VERIFY the AI Review
Classify each significant AI suggestion as Accepted, Modified, Rejected, or Unverified. Explain the evidence used.

|                            AI Suggestion                            | Classification |                                                                 Evidence Used                                                                  |                                                                                                                                                         Justification                                                                                                                                                          |
| :-----------------------------------------------------------------: | :------------: | :--------------------------------------------------------------------------------------------------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------: |
|              Define how staff can search for patients               |   Unverified   |                                     FR-04 states: "The system shall allow staff to search for a patient."                                      |                                                                                                 There is insufficient information to determine whether searching by name only is acceptable. Client confirmation is required.                                                                                                  |
|         Define the practitioner data that must be recorded.         |   Unverified   |                                  FR-05 states: "The system shall allow staff to record practitioner details."                                  |                                                                                                        The requirement remains incomplete from an implementation perspective, but no client decision has been provided.                                                                                                        |
|                 Specify appointment duration rules.                 |   Unverified   | FR-07 states: "The system shall prevent appointments from being created when the practitioner already has an active appointment at that time." |                                                                                             The review identified a possible ambiguity, but there is no evidence showing whether appointments are fixed-length or variable-length.                                                                                             |
|     Clarify who is allowed to view schedules. (FR-08 and US-04)     |   Unverified   |           FR-08: "allow staff to view a practitioner's appointment schedule" US-04: "As a practitioner, I want to view my schedule"            |                                                                                                The potential inconsistency still exists because the requirements do not explicitly state whether both roles can view schedules.                                                                                                |
|       Clarify how duplicate patients are identified. (NFR-02)       |    Modified    |                     NFR-02 states: "prevent duplicate patients". Assumption states: "Patients are identified by name only"                     | The original review questioned how duplicate patients were identified. The assumption partially answers the question by indicating that names are used. However, the assumption introduces a new risk because different patients may share the same name. Therefore, the concern has been modified rather than fully resolved. |
|               Confirm that patient names are unique.                |   Unverified   |                            Assumption: "Patients are identified by name only". NFR-02: "prevent duplicate patients"                            |                                                                                                         No evidence confirms that patient names are unique. This remains a question requiring stakeholder validation.                                                                                                          |
| Replace "acceptable time" with a measurable response time. (NFR-06) |   Unverified   |                                         NFR-06 states: "provide a response within an acceptable time"                                          |                                                                                                                           The issue remains because no measurable performance target has been added.                                                                                                                           |
|               Define measurable reliability criteria.               |   Unverified   |                   NFR-01 states: "maintain accurate patient, practitioner, and appointment records during normal operation"                    |                                                                                                                             The requirement remains subjective and difficult to test objectively.                                                                                                                              |