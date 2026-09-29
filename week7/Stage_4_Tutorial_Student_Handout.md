# Activity 1 - Encapsulation Review
|    Class     | Protected State / Invariant |   Public operations    |
| :----------: | :-------------------------: | :--------------------: |
|   Patient    |    Name cannot be empty     |    update_details()    |
| Practitioner |  Name and specialty valid   |    view_schedule()     |
| Appointment  |  Valid status transitions   | cancel(), reschedule() |

# Activity 2 - Composition or Inheritance?
|              Relationship              |        Decision         |                                      Reason                                      |
| :------------------------------------: | :---------------------: | :------------------------------------------------------------------------------: |
|        Appointment and Patient         | Composition/association |      Appointment is associated with a Patient and is not a type of Patient       |
|      Appointment and Practitioner      | Composition/association | Appointment is associated with a Practitioner and is not a type of Practitioner  |
| Doctor and Practitioner (hypothetical) |       Inheritance       |                  A Doctor is a specialised type of Practitioner                  |
|         Clinic and Appointment         | Composition/association |          A Clinic manages Appointments but is not a type of Appointment          |

# Activity 3 - Responsibility Allocation
**Who decides whether SCHEDULED can become CANCELLED?**\
Appointment class

**Who validates a patient name?**\
Patient Class

**Should Appointment execute SQL? Why?**\
No. Domain objects should not contain database logic.

**Should the UI decide whether a status transition is legal?**\
No. The Appointment class should enforce the business rule.

# Activity 4 - AI Code Critique
**AI generates an Appointment class with public status mutation, SQL inside cancel(), a NotificationManager dependency and inheritance from PatientRecord. Identify at least five design problems and corrections.**

|                                            Problem                                             |                                  Correction                                  |
| :--------------------------------------------------------------------------------------------: | :--------------------------------------------------------------------------: |
|          Public status mutation allows any code to change appointment status directly          | Make status protected/private and change it through methods such as cancel() |
|                   SQL inside cancel() mixes domain logic with database logic                   |            Keep database code separate from the Appointment class            |
|                    NotificationManager dependency adds unnecessary coupling                    |                 Remove the dependency from the domain class                  |
| Inheritance from PatientRecord is incorrect because Appointment is not a type of PatientRecord |                     Use association with Patient instead                     |
|             Violates separation of concerns by combining multiple responsibilities             |         Keep Appointment focused on appointment behaviour and state          |

# Exit question
**Why can code be object-oriented syntactically but still have poor object-oriented design?**\
Code can be object-oriented syntactically because it uses classes and objects, but it can still have poor object-oriented design if classes have the wrong responsibilities, business rules are not protected, or there is excessive coupling between classes.