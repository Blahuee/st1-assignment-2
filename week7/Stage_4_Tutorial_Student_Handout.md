# Activity 1 - Encapsulation Review
|    Class     | Protected State / Invariant | Public operations |
| :----------: | :-------------------------: | :---------------: |
|   Patient    |
| Practitioner |
| Appointment  |

# Activity 2 - Composition or Inheritance?
Appointment and Patient -> □ Composition/association  □ Inheritance  Reason: __________________
Appointment and Practitioner -> □ Composition/association  □ Inheritance  Reason: __________________
Doctor and Practitioner (hypothetical) -> □ Composition/association  □ Inheritance  Reason: __________________
Clinic and Appointment -> □ Composition/association  □ Inheritance  Reason: __________________

# Activity 3 - Responsibility Allocation
Who decides whether SCHEDULED can become CANCELLED?
Who validates a patient name?
Should Appointment execute SQL? Why?
Should the UI decide whether a status transition is legal?

# Activity 4 - AI Code Critique
AI generates an Appointment class with public status mutation, SQL inside cancel(), a NotificationManager dependency and inheritance from PatientRecord. Identify at least five design problems and corrections.

# Exit question
Why can code be object-oriented syntactically but still have poor object-oriented design?