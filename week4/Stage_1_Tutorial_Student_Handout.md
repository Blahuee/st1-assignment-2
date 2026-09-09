# Stage 1 Tutorial Activity - Why Software Engineering Still Matters 

**Stage 1 | Introducing Software Technology Case Study with Python and Guided AI use**

## Activity 1 - Think-Pair-Share (10 minutes) 
If ChatGPT or Copilot can produce a 100-line Python application very quickly, what knowledge does a software engineer still need? 

1. The ability to verify the code AI produces is the expected output
2. The ability to identify bugs or mistakes produced by AI
3. The ability to know when AI’s solution is appropriate and when it’s not 

## Activity 2 - Is This Software Engineering? (10 minutes)
Scenario A: A student writes a 50-line Python calculator. 
Scenario B: A team develops a payroll system used by 5,000 employees. 
Scenario C: An AI assistant generates a simple appointment application from one prompt. 

| Scenario | Programming? | Software engineering? |                                                                                                        Why?                                                                                                         |
| :------: | :----------: | :-------------------: | :-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------: |
|    A     |     Yes      |          No           | The student has written code. They haven’t necessarily been given formal requirements, design, testing process or documentation considerations.  They have coded a small, isolated program not an engineered system |
|    B     |     Yes      |          Yes          |                                           The software is designed, developed, tested and maintained to meet a goal and ensures reliability for multiple users over time.                                           |
|    C     |     Yes      |          No           |                                   AI produces code it doesn’t perform engineering tasks of its own. It’s given requirements as prompts but doesn’t apply engineering principles.                                    |

## Activity 3 - SmartCare Problem Analysis (20 minutes)
Client statement: SmartCare Community Clinic currently uses spreadsheets and paper records to manage patients and appointments. The clinic wants new software to improve these processes. 

**Task 1 - Identify stakeholders**
|   Stakeholder   |                     What do they need?                     |
| :-------------: | :--------------------------------------------------------: |
|  Receptionists  | A better way of booking and organising client appointments |
|    Patients     |               Faster service and better care               |
|  Practitioners  |           Easy and secure access to patient data           |
| Clinic Managers |             Better organisation and reporting              |

**Task 2 - Identify current problems**

1. Paper records can get damaged or lost 
2. Spreadsheets become difficult to manage and update 
3. Manually booked appointments is more prone to error (double bookings) 
4. Patient information can be difficult for practitioners to get access to quickly 

**Task 3 - Ask client questions**
1. What patient information needs to be stored? 
2. Who requires access to patient records? 
3. Do you want patients to be able to book appointments online? 
4. Who should have access to patient records? 
5. Are there any privacy or security requirements? 

## Activity 4 - Critique an AI Response (15 minutes) 
An AI assistant suggests: appointment management; facial-recognition login; AI diagnosis recommendations; patient search; online payment; practitioner schedule view; insurance processing; automatic treatment-plan generation. 

|          Suggestion          |              Client evidence?              | In scope? | Decision |
| :--------------------------: | :----------------------------------------: | :-------: | :------: |
|    Appointment management    | Clinic needs better appointment management |    Yes    | Include  |
|   Facial recognition login   |                     No                     |    No     | Exclude  |
| AI diagnosis recommendations |                     No                     |    No     | Exclude  |
|        Patient search        | Practitioners need access to patient data  |    Yes    | Include  |
|        Online payment        |                     No                     |    No     | Exclude  |
|  Practitioner schedule view  |     Required for booking appointments      |    Yes    | Include  |
|     Insurance processing     |                     No                     |    No     | Exclude  |
|  Treatment-plan generation   |                     No                     |    No     | Exclude  |

## Exit question
**Write one activity that a software engineer must perform and that cannot safely be delegated entirely to AI.**\
Decide what the software should do and ensure the solution meets the safety requirements of the design documentation 