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
**FR-01:** The system shall allow authorised staff to register a new patient.\
**FR-02:** The system shall prevent cancelled appointments from being treated as active bookings.\
**FR-03:** The system shall allow staff to update patient details.\
**FR-04:** The system shall allow staff to search for a patient.\
**FR-05:** The system shall allow staff to record practitioner details.\
**FR-06:** The system shall allow authorised staff to create an appointment.\
**FR-07:** The system shall prevent appointments from being created when the practitioner already has an active appointment at that time.\
**FR-08:** The system shall allow staff to view a practitioner’s appointment schedule.\
**FR-09:** The system shall allow authorised staff to cancel an active appointment.\
**FR-10:** The system shall retain cancelled appointments in the appointment history.\
**FR-11:** The system shall display each appointment’s status.

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

# Part F - AI Requirements Review:
**Prompt:** Act as a software requirements reviewer. Review the SmartCare requirements for ambiguity, inconsistency, missing clarification questions and testability. Do NOT invent new client requirements. For every suggestion, state whether it is based on evidence or is only a question/assumption requiring validation.

# Part G - VERIFY the AI Review
Classify each significant AI suggestion as Accepted, Modified, Rejected, or Unverified. Explain the evidence used.

|                     AI Suggestion                      | Classification |                                                   Evidence Used                                                   |
| :----------------------------------------------------: | :------------: | :---------------------------------------------------------------------------------------------------------------: |
|    The meaning of “patient management” is unclear.     |    Accepted    |                 The brief mentions patient management but does not define its specific functions.                 |
|  The meaning of “practitioner management” is unclear.  |    Accepted    |                  The brief does not state which practitioner details or functions are required.                   |
|  The meaning of “appointment management” is unclear.   |    Accepted    |                            The brief does not clearly list all appointment operations.                            |
|        “Simple software system” is subjective.         |    Accepted    |                                  The word “simple” has no measurable definition.                                  |
|        “Manageable application” is subjective.         |    Accepted    |                 The brief does not define how maintainability or manageability will be measured.                  |
| “Practitioner” and “GP” may refer to different groups. |   Unverified   |  The wording is unclear, but the provided information does not confirm that different practitioner types exist.   |
|       Appointment status management is required.       |    Accepted    |                  Inconsistent appointment status information is identified as a current problem.                  |
|     Patient information fields must be clarified.      |    Accepted    |                         The brief does not specify which patient details must be stored.                          |
|   Practitioner information fields must be clarified.   |    Accepted    |                                The required practitioner details are not provided.                                |
|        Appointment duration must be clarified.         |    Accepted    |                Duration affects whether appointment times conflict, but no duration is specified.                 |
|       Duplicate booking rules must be clarified.       |    Accepted    |         Duplicate bookings are a stated problem, but the exact definition of a duplicate is not provided.         |
|   Practitioner availability rules must be clarified.   |    Accepted    |                 The brief does not explain how practitioner availability is recorded or checked.                  |
|         Cancellation rules must be clarified.          |    Accepted    |              The brief identifies appointment management but does not define cancellation behaviour.              |
|    Appointment history contents must be clarified.     |    Accepted    |            Limited appointment history is identified, but the information to retain is not specified.             |
|         Operational reports must be clarified.         |   Unverified   |    Reports are mentioned as a current difficulty, but required reports are not confirmed as a system feature.     |
|        User access and roles must be clarified.        |    Accepted    |                The stakeholders are known, but their specific system permissions are not defined.                 |
|   The number of concurrent users must be clarified.    |   Unverified   |                No evidence indicates that simultaneous user numbers are a significant requirement.                |
| Existing spreadsheet data migration must be clarified. |   Unverified   |          The current use of spreadsheets is stated, but migration into the new system is not requested.           |
|      Patient record searching must be clarified.       |    Accepted    | Difficulty finding patient information is a stated problem, although the required search methods are not defined. |
| The requirements lack measurable acceptance criteria.  |    Accepted    |     Terms such as “simple,” “manageable,” and “basic” are not objectively testable without further criteria.      |