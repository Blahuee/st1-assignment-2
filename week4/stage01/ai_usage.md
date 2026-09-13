# Prompt 1

### As a Python tutor, I'll explain the program at a beginner level, point out some limitations, suggest practical improvements, and then test your understanding with two questions.

This explanation is written as a tutor-style review. I'll focus on what the code currently does, where it could be improved, and a few questions to help you check your understanding.

## 1. What the code does

The program is a simple appointment-booking system that stores appointments in a Python list.

### create_appointment() function
```python
def create_appointment(patient_name, practitioner_name, appointment_time):
```

This function receives three pieces of information:

- Patient name
- Practitioner name
- Appointment time

It then validates the inputs:

```python
if not patient_name:
    raise ValueError("Patient name cannot be empty")
```

Similar checks are performed for the practitioner name and appointment time.

These checks ensure that empty values are not accepted. If any field is empty, the program raises a `ValueError` and stops execution unless the error is handled elsewhere.

The function then creates a dictionary:

```python
appointment = {
    "patient_name": patient_name,
    "practitioner_name": practitioner_name,
    "appointment_time": appointment_time
}
```

A dictionary is used to group related appointment information together using key-value pairs.

The appointment is added to the global list:

```python
appointments.append(appointment)
```

Finally, the appointment dictionary is returned:

```python
return appointment
```

### list_appointments() function

```python
def list_appointments():
```

This function displays all stored appointments.

First, it checks whether the list is empty:

```python
if not appointments:
```

If no appointments exist, it prints:

```python
"No appointments recorded."
```

and exits the function.

If appointments are present, the function loops through each appointment:

```python
for appointment in appointments:
```

and prints the details in a readable format:

```python
print(f"Patient: {appointment['patient_name']} | Practitioner: {appointment['practitioner_name']} | Time: {appointment['appointment_time']}")
```

### Main program

The list is created:

```python
appointments = []
```

User input is collected:

```python
patient_name = input(...)
practitioner_name = input(...)
appointment_time = input(...)
```

The appointment is created:

```python
create_appointment(patient_name, practitioner_name, appointment_time)
```

Finally, all appointments are displayed:

```python
list_appointments()
```

## 2. Three limitations
### Limitation 1: No validation of the appointment format

The program checks that an appointment time exists, but it does not verify that the time is actually valid.

For example, the user could enter:
```
banana
```

or
```
99/99/9999
```

and the program would still accept it.

### Limitation 2: No error handling

The function raises a ValueError when a field is empty.

```python
raise ValueError(...)
```

However, the main program does not use a `try/except` block to catch the error.

As a result, the program may crash and display a traceback to the user.

### Limitation 3: Data is not saved permanently

Appointments are stored only in:

```python
appointments = []
```

This list exists only while the program is running.

When the program closes, all appointment information is lost.

## 3. Suggested improvements

Without rewriting the whole application, here are some practical improvements.

### Improvement 1: Validate date and time input

Use Python's datetime module to check whether the entered appointment time follows the expected format.

Benefits:

- Prevents invalid dates
- Improves data quality
- Reduces user errors
### Improvement 2: Add exception handling

Wrap the appointment creation code in a try/except block.

Benefits:

- Prevents program crashes
- Provides friendly error messages
- Improves user experience
### Improvement 3: Check for duplicate appointments

Before adding an appointment, check whether the same patient already has an appointment at the same time.

Benefits:

- Avoids accidental duplicates
- Makes scheduling more reliable

### Additional possible improvements
- Allow multiple appointments to be entered before listing them.
- Sort appointments by date and time.
- Store appointments in a text file, CSV file, or database.
- Trim extra spaces from user input using .strip().
- Assign each appointment a unique ID.

## 4. Key programming concepts demonstrated

This example demonstrates several important introductory programming concepts:

- Functions
- Parameters and arguments
- Input validation
- Dictionaries
- Lists
- List operations (append)
- Loops (for)
- Conditional statements (if)
- Returning values (return)
- Exceptions (ValueError)

## 5. Questions to test your understanding
### Question 1

What is the purpose of this line?

```python
appointments.append(appointment)
```

Specifically, what would happen if this line were removed from the program?

### Question 2

The code checks:

```python
if not patient_name:
```

Why does this prevent an empty string ("") from being accepted, and what exception is raised when the condition is true?

# Prompt 2
### Create a simple beginner-friendly Python function that stores patient name, practitioner name and appointment time. Do not use a database or GUI.

Here's a simple beginner-friendly function that stores a patient name, practitioner name, and appointment time in a dictionary and returns it.

```python
def book_appointment(patient_name, practitioner_name, appointment_time):
    appointment = {
        "patient": patient_name,
        "practitioner": practitioner_name,
        "time": appointment_time
    }
    
    return appointment


# Example usage
appointment1 = book_appointment(
    "Alice Smith",
    "Dr. John Doe",
    "2024-07-20 10:00 AM"
)

print(appointment1)
```

**How it works**\
The function `book_appointment()` accepts three pieces of information:
- `patient_name`
- `practitioner_name`
- `appointment_time`
- It stores them in a dictionary.
- The dictionary is returned and stored in `appointment1`.
- `print(appointment1)` displays the appointment details.

**Example output**
```python
{
    'patient': 'Alice Smith',
    'practitioner': 'Dr. John Doe',
    'time': '2024-07-20 10:00 AM'
}
```

This example uses only:
- Variables
- Functions
- Dictionaries

and does not use a database or a graphical user interface (GUI), making it suitable for beginners learning introductory Python.