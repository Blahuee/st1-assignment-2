# Stage 1 Lab - Human vs AI: Building Your First SmartCare Prototype 

## Part A - Understand the Problem: AI OFF 

SmartCare needs a small prototype that allows a receptionist to record patient appointments. Each appointment records patient name, practitioner name and appointment time. 

**What data must be stored?**\
Patient name, practitioner name, appointment time 

**What functions might be useful?**\
Patient search function 

**What could go wrong?**\
Duplicate appointments could be created, appointments aren't saved, Invalid or missing information could be entered 

**What requirements are unclear?**\
How are duplicate appointments handled, what should happen if required information is missing 

## Part B - Build a Human-Written Prototype: AI OFF 

```python
#task 1 

# Create and run a simple Python file with basic input,output statements 

print("Welcome to SmartCare: Community Clinic Appointment Booking System!") 

# First Appointment 

patient1_name = 'Alice Smith' 

practitioner1_name = 'Dr. John Doe' 

appointment1_time = '2024-07-20 10:00 AM' 

print(f"Patient: {patient1_name} | Practitioner: {practitioner1_name} | Time: {appointment1_time}") 

# Second Appointment 

patient2_name = 'Bob Johnson' 

practitioner2_name = 'Dr. Jane Roe' 

appointment2_time = '2024-07-20 11:30 AM' 

print(f"Patient: {patient2_name} | Practitioner: {practitioner2_name} | Time: {appointment2_time}") 
```

```python
#task1enhanced 

# Use lists, dictionaries and functions to enhance the Python file 

appointments = [] 

def book_appointment(patient_name, practitioner_name, appointment_time): 

    if not patient_name: 

        raise ValueError("Patient name cannot be empty") 

    appointment = { 

        "patient": patient_name, 

        "practitioner": practitioner_name, 

        "time": appointment_time 

    } 

    appointments.append(appointment) 

def display_appointments(): 

    if not appointments: 

        print("No appointments recorded.") 

        return 

    for appointment in appointments: 

        print(f"Patient: {appointment['patient']} | Practitioner: {appointment['practitioner']} | Time: {appointment['time']}") 

print("Welcome to SmartCare: The Clinical Appointment Booking System!") 

book_appointment('Alice Smith', 'Dr. John Doe', '2024-07-20 10:00 AM') 

book_appointment('Bob Johnson', 'Dr. Jane Roe', '2024-07-20 11:30 AM') 

display_appointments() 
```
^ Now, run  both programs, and identify at least five limitations. 

**Limitations Identified:**
- Practitioners name can be blank
- No handling for duplicate appointments
- Appointments aren’t saved when the script is closed
- No user-friendly menu/GUI
- Users cannot edit or remove appointments 

## Part C - Use AI as Tutor: AI ON (Use only UC approved GenAI Tool such as Microsoft CoPilot) 

**Suggested prompt structure:**\
Act as a Python tutor. 
I am learning introductory software technology. 
Here is a small appointment-booking function. 
1. Explain what the code does. 
2. Identify three limitations. 
3. Suggest improvements. 
4. Do not rewrite the whole application. 
5. Ask me two questions to test my understanding. 

## Part D - Generate an Alternative: AI ON 

Ask AI to create a simple beginner-friendly Python function that stores patient name, practitioner name and appointment time. Explicitly prohibit a database or GUI. 

## Part E - Compare Human and AI Versions 

|           Question           |                                   Human Version                                   |                         AI Version                         |
| :--------------------------: | :-------------------------------------------------------------------------------: | :--------------------------------------------------------: |
|     Easy to understand?      |                     Yes. Simple variable and print statements                     |          Yes, but uses a function and dictionary           |
|      Runs successfully?      |                                        Yes                                        |                            Yes                             |
| Uses only required features? |                        Yes, but only basic python features                        |                            Yes                             |
|      Adds assumptions?       | Yes, as the appointment details are stored as separate variables and time is text | Yes, it assumes appointments should be stored dictionaries |
|       Handles errors?        |                          No validation or error handling                          |              No validation or error handling               |
|     Could I explain it?      |                                        Yes                                        |                            Yes                             |

## Part F - Verify Behaviour 

- Normal appointment
- Blank patient name
- Two appointments for the same practitioner/time
- Strange input such as patient_name=None or appointment_time=None

**Test 1:** 
```python
book_appointment(
    "John Doe",
    "Dr Phil",
    "06/09/2026 10:30 AM"
)
```
**Result:** task1.py displays two appointments using variables and print statements. After correcting the indentation in task1_enhanced.py, it stores the two appointments in a list of dictionaries and displays them using a function.\
**Limitation:** Both versions use hardcoded appointment details, so the user cannot enter appointment information interactively.

**Test 2:**
```python
book_appointment(
    "",
    "Dr Phil",
    "06/09/2026 10:30 AM"
)
```
**Result:** The enhanced version raises a ValueError when the patient name is a blank string, because empty strings are treated as a false value by the validation check. However, it accepts an empty-string as the appointment time because that field is not validated. The original version has no validation and would display hardcoded values without checking them.
**Limitation:** The enhanced version only validates the patient name and does not ensure that all required appointment details are valid.

**Test 3:**
```python
book_appointment(
    "John Doe",
    "Dr Phil",
    "06/09/2026 10:30 AM"
)
book_appointment(
    "Jane Doe",
    "Dr Phil",
    "06/09/2026 10:30 AM"
)
```
**Result:** Both appointments are added to the list because the enhanced version does not check for scheduling conflicts.\
**Limitation:** Multiple patients can be booked with the same practitioner at the same time, potentially creating conflicting appointments. The original version also has no conflict checking.

## Part G - Improve One Thing 
**Choose exactly one controlled improvement, for example: if not patient_name: raise ValueError("Patient name cannot be empty")**\
Add a loop to book multiple appointments in quick succession