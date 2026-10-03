# Reflection
**Which AI-generated part did you modify or reject? Why? How did the approved design constrain the AI?**\
I modified some of the AI-generated code because it suggested storing appointment lists inside the Patient and Practitioner classes. I rejected this because it was not part of the approved UML design. Instead, I used view_history() and view_schedule() to filter appointments from the existing appointment list.
The approved design constrained the AI by limiting the solution to the classes, attributes, and methods defined in the UML. This helped me avoid adding unnecessary features and keep the implementation consistent with the SmartCare domain model.

The AI was used only to implement the Appointment class and the agreed AppointmentStatus enum, following the approved UML, business rules, and explicit constraints. The resulting implementation was then reviewed and used to identify where the UML needed to more accurately represent the implemented design.