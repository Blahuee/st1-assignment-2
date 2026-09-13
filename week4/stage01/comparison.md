| Question | Human Version | AI Version |
| :---: | :---: | :---: |
| Easy to understand? | Yes the functions are clearly labelled and the code is organised into creating and listing appointments | Yes, but uses a function and dictionary |
| Runs successfully? | Yes. As long as `appointments` is defined before the function is called | Yes |
| Uses only required features? | Yes | Yes |
| Adds assumptions?  | It assumes an appointment contains a patient name, practitioner name, and appointment time, and that appointments should be stored in a list. | Yes, it assumes appointments should be stored dictionaries |
| Handles errors? | Yes - Basic errors. Checks the patient name, practitioner_name and appointment_time are not empy | No validation or error handling |
| Could I explain it? | Yes the code is clearly separated into functions with descriptions on their functionality | Yes |

## Summary
I find the human version is easier to understand as it's commented clearly. Although the human version is more advanced it allows the user to enter appointment details, validate the required information has been entered and stores the information gathered into a list then displays it. The AI verison is simpler but only creates and returns one appointment and does not include input validation or a way to store multiple appointments.