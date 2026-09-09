# SmartCare v0.1 - Initial Engineering Brief and AI Activity Card 

A2 Case Study Stage 1 student resource 

## SmartCare scenario
SmartCare Community Clinic currently uses spreadsheets and paper records to manage patients and appointments. The client says: 'We need software to help manage patients, practitioners, and appointments.' This is not yet a complete specification. 

## Initial Engineering Brief 

1. **Problem summary**\
SmartCare is currently using spreadsheets and paper records to manage their patients and appointments. This would be difficult to keep information organised, find records quickly, manage patient appointments and coordinate practitioners. SmartCare want a software that can help them better manage patient information, their appointments and practitioners. SmartCare's current request is very broad and doesn't explain exact features, users, security requirements or workflow. 

2. **Initial stakeholders**

|   Stakeholder   |                          Possible need                           |
| :-------------: | :--------------------------------------------------------------: |
|  Receptionists  |           Manage appointments and patient information            |
|    Patients     |              Appointments are recorded and managed               |
|  Practitioners  | View their appointment schedule and relevant patient information |
| Clinic Managers |     Manage practitioners and maintain system and user access     |

3. **Initial features** 

|             Feature             | Confirmed or provisional? |                                    Why?                                     |
| :-----------------------------: | :-----------------------: | :-------------------------------------------------------------------------: |
|     Manage patient records      |         Confirmed         |                       Client explicitly requested it                        |
| Manage practitioner information |         Confirmed         |                       Client explicitly requested it                        |
|       Manage appointments       |         Confirmed         |                       Client explicitly requested it                        |
|       Search for patients       |        Provisional        |              Would be useful for lots of clients in the system              |
|           User login            |        Provisional        | Security should be kept in mind when access to personal records is involved |
|   Patient appointment history   |        Provisional        |                     Would be useful for client queires                      |

4. **Questions for the client** 

    1. What information is required for each patient
    2. Who would need access to view patient records
    3. Who would need access to modify patient records
    4. Are there any security or legal requirements for storing patient information?
    5. How should appointments be created, changed or cancelled? 

5. **What we do not yet know**
   1. What patient information is required to be stored
   2. What user permissions are required
   3. How do they want appointments, created, changed or cancelled? 

## AI Activity Card - Ask, Check, Explain 

### Before AI
**What do I think the code does? What problems can I already identify?**\
Creates appointment with the inputted patient name, practitioner and appointment time then lists the appointment. There is currently no way to delete appointments 

**AI request**\
Act as a tutor. Explain this code and identify potential problems. Do not provide a complete replacement. Ask me questions that help me reason about the solution. 

**Evaluate**
|          Suggestion            | Useful | Unclear | Incorrect | Out of scope |
| :---------------------------:  | :----: | :-----: | :-------: | :----------: |
|     Whitespace-only input      |   X    |         |           |              |
| Appointment time is just text  |   X    |         |           |              |
|Program crashes on invalid input|   X    |         |           |              |
| Duplicate appointments         |   X |
| Data only exists while the program runs | X|

## Decide
**For each significant suggestion: Accept / Modify / Reject / Keep unverified.**
- Whitespace-Only input: Accept
- Appointment time is just text: Accept 
- Program crashes on invalid input: Accept
- Duplicate Appointments: Accept
- Data only exists while the program is running: Keep unverified

## Verify 
- Run the code
- Test normal input
- Test unusual input
- Compare with requirements
- Ask tutor/peer
- Check documentation

## Explain
**Can I explain the final code without reading the AI response? What do I still need to understand?**\ Yes, I’m able to understand the code. I manually commented the code so I could understand it when I implemented it into the script 