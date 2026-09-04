# Prompt 1

As a Python tutor, I'll explain the program at a beginner level, point out some limitations, suggest practical improvements, and then test your understanding with two questions.

## 1. What the code does

This program simulates a simple clinic appointment booking system called SmartCare.

**Part A: Basic output using variables**

The first section:

print("Welcome to SmartCare: Community Clinic Appointment Booking System!")


displays a welcome message.

Next, the program stores information for two appointments in separate variables:

```python
patient1_name = 'Alice Smith'
practitioner1_name = 'Dr. John Doe'
appointment1_time = '2024-07-20 10:00 AM
```

and
```python
patient2_name = 'Bob Johnson'
practitioner2_name = 'Dr. Jane Roe'
appointment2_time = '2024-07-20 11:30 AM
```

These values are then displayed using f-strings:

```python
print(f"Patient: {patient1_name} | Practitioner: {practitioner1_name} | Time: {appointment1_time}")
```

An f-string allows variables to be inserted directly into text using {}.

**Part B: Using a list and dictionary**

The program creates an empty list:

```python
appointments = []
```

This list will store all appointment records. Inside the `book_appointment()` function, a dictionary is created:

```python
appointment = {
    "patient": patient_name,
    "practitioner": practitioner_name,
    "time": appointment_time
}
```

A dictionary stores data as key-value pairs.

Example:

```python
{
    "patient": "Alice Smith",
    "practitioner": "Dr. John Doe",
    "time": "2024-07-20 10:00 AM"
}
```

The dictionary is added to the list using:

```python
appointments.append(appointment)
```

**Part C: Functions**

The program contains two functions:


**`book_appointment()`**

This function:
1. Receives appointment details.
2. Checks that the patient name is not empty.
3. Creates a dictionary containing the appointment details.
4. Stores the appointment in the appointments list. 

**`display_appointments()`**

This function:

1. Checks whether any appointments exist.
2. Prints a message if the list is empty.
3. Otherwise loops through all appointments and displays them.

The loop:

```python
for appointment in appointments:
```

processes each appointment one at a time.

**Program execution**

The following statements:

```python
book_appointment('Alice Smith', 'Dr. John Doe', '2024-07-20 10:00 AM')
book_appointment('Bob Johnson', 'Dr. Jane Roe', '2024-07-20 11:30 AM')
```

add two appointments to the list.

Finally:
```python
display_appointments()
```

prints all stored appointments.



## 2. Three limitations

**1. Limited input validation**

The program only checks whether the patient name is empty.\
For example: 

```python
book_appointment("Alice", "", "")
```

would still be accepted even though important information is missing.

---

**2. No prevention of scheduling conflicts**

  - The system allows multiple appointments at the same time.
  - For example, two patients could be booked with the same practitioner at exactly 10:00 AM.

---

**3. Data is not saved permanently**

  - Appointments exist only while the program is running.
  - If the program closes, the appointment list is lost because it is stored only in memory.

## 3. Suggested improvements
**Improve validation**

  Check that:
  - Patient name is provided.
  - Practitioner name is provided.
  - Appointment time is provided.
  - Date and time follow a valid format.

---

**Detect double bookings**

Before adding a new appointment, check whether the practitioner already has an appointment scheduled at that time.

This would make the booking system more realistic.

---

**Save data to a file**

Store appointments in a file such as:

- JSON
- CSV
- Database (for larger systems)

This would allow appointments to remain available after the program is closed.

---

**Add appointment management features**

Possible additions include:

- Cancelling appointments.
- Updating appointment times.
- Searching for a patient.
- Viewing appointments for a specific practitioner.

These features would make the system more useful without completely redesigning it.

## 4. Summary

This code demonstrates several important introductory Python concepts:

- Variables
- Lists
- Dictionaries
- Functions
- Input validation
- Loops
- f-strings

It is a good example of moving from storing data in individual variables to using data structures and functions to make the code more scalable.

## 5. Check your understanding
**Question 1**

Why is a list used for appointments instead of creating separate variables such as appointment1, appointment2, appointment3, and so on?

**Question 2**

What is the purpose of this line?

```python
appointments.append(appointment)
```

Specifically, what would happen if this line were removed from the `book_appointment()` function?

# Prompt 2

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

**How it works**
The function `book_appointment()` accepts three pieces of information:
- `patient_name`
- `practitioner_name`
- `appointment_time`\
- It stores them in a **dictionary**.
- The dictionary is returned and stored in **appointment1**.
- **print(appointment1)** displays the appointment details.

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