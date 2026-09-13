## BEFORE AI SUGGESTIONS WERE IMPLEMENTED

#######################################################################################################################################################
##  CREATE APPOINTMENT FUNCTION
#######################################################################################################################################################
# def create_appointment(patient_name, practitioner_name, appointment_time):
#     if not patient_name:
#         raise ValueError("Patient name cannot be empty")
#     if not practitioner_name:
#         raise ValueError("Practitioner name cannot be empty")
#     if not appointment_time:
#         raise ValueError("Appointment time cannot be empty")
    
#     appointment = {
#         "patient_name": patient_name,
#         "practitioner_name": practitioner_name,
#         "appointment_time": appointment_time
#     }
#     appointments.append(appointment)
#     return appointment

#######################################################################################################################################################
##  LIST APPOINTMENTS FUNCTION
#######################################################################################################################################################
# def list_appointments():
#     if not appointments:
#         print("No appointments recorded.")
#         return

#     for appointment in appointments:
#         print(f"Patient: {appointment['patient_name']} | Practitioner: {appointment['practitioner_name']} | Time: {appointment['appointment_time']}")

#######################################################################################################################################################

## DECLARE EMPTY APPOINTMENTS LIST ARRAY
# appointments = []

# ## CREATE APPOINTMENTS
# patient_name = input("Enter patient name: ")
# practitioner_name = input("Enter practitioner name: ")
# appointment_time = input("Enter appointment time (DD/MM/YYYY HH:MM AM/PM): ")

# create_appointment(patient_name, practitioner_name, appointment_time)

## LIST CREATED APPOINTMENTS
#list_appointments()

## AFTER AI SUGGESTIONS WERE IMPLEMENTED

## IMPORT MODULE
import datetime as dt

#######################################################################################################################################################
##  CREATE APPOINTMENT FUNCTION
#######################################################################################################################################################
def create_appointment(patient_name, practitioner_name, appointment_time):
    if not patient_name:
        raise ValueError("Patient name cannot be empty")
    if not practitioner_name:
        raise ValueError("Practitioner name cannot be empty")
    if not appointment_time:
        raise ValueError("Appointment time cannot be empty")

    # CONVERT STRING TO DATETIME OBJECT AND VALIDATE FORMAT
    try:
        appointment_datetime = dt.datetime.strptime(appointment_time, "%d/%m/%Y %I:%M %p")
    except ValueError:
        raise ValueError("Invalid date format. Please use D, M, Y, H, M HH:MM AM/PM")

    # CREATE APPOINTMENT DICTIONARY
    appointment = {
        "patient_name": patient_name,
        "practitioner_name": practitioner_name,
        "appointment_time": appointment_time
    }
    # CHECK FOR DUPLICATES
    for existing_appointment in appointments:
        if (existing_appointment['patient_name'] == patient_name and
            existing_appointment['practitioner_name'] == practitioner_name and
            existing_appointment['appointment_time'] == appointment_time):
            raise ValueError("Duplicate appointment detected. This appointment already exists.")

    appointments.append(appointment)
    return appointment

#######################################################################################################################################################
##  LIST APPOINTMENTS FUNCTION
#######################################################################################################################################################
def list_appointments():
    if not appointments:
        print("No appointments recorded.")
        return

    for appointment in appointments:
        print(f"Patient: {appointment['patient_name']} | Practitioner: {appointment['practitioner_name']} | Time: {appointment['appointment_time']}")

#######################################################################################################################################################

## DECLARE EMPTY APPOINTMENTS LIST ARRAY
appointments = []

## CREATE APPOINTMENTS
create_booking = True
while create_booking == True:
    try:
        patient_name = input("Enter patient name: ")
        practitioner_name = input("Enter practitioner name: ")
        appointment_time = input("Enter appointment time (DD/MM/YYYY HH:MM AM/PM): ")

        create_appointment(patient_name, practitioner_name, appointment_time)
        print("Appointment created successfully!")

        create_booking = input("Do you want to create another appointment? (y/n): ").strip().lower() == 'y'
        if not create_booking:
            break  # Exit the loop if appointment creation is successful
    except ValueError as e:
        print(f"Error: {e}. Please try again.")

## LIST CREATED APPOINTMENTS
list_appointments()