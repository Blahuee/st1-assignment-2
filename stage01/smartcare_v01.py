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
    
    appointment = {
        "patient_name": patient_name,
        "practitioner_name": practitioner_name,
        "appointment_time": appointment_time
    }
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
create_appointment("Jane Doe", "Dr. Smith", "2026-09-10 10:30 AM")
create_appointment("John Doe", "Dr. Jones", "2026-09-10 11:00 AM")

## LIST CREATED APPOINTMENTS
list_appointments()