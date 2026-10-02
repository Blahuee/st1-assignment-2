from patient import Patient
from practitioner import Practitioner
from appointment import Appointment, AppointmentStatus
from datetime import datetime

# CREATE OBJECTS

dr_smith = Practitioner(
    1,
    "Dr Smith",
    "General Practice"
)

dr_jones = Practitioner(
    2,
    "Dr Jones",
    "Cardiology"
)

patient_1 = Patient(
    101,
    "Alice Brown",
    "0400111222"
)

patient_2 = Patient(
    102,
    "Bob White",
    "0400333444"
)

appointment_1 = Appointment(
    1001,
    datetime(2026, 10, 10, 9, 0),
    patient_1,
    dr_smith
)

appointment_2 = Appointment(
    1002,
    datetime(2026, 10, 10, 10, 0),
    patient_2,
    dr_smith
)

appointment_3 = Appointment(
    1003,
    datetime(2026, 10, 1, 11, 0),
    patient_1,
    dr_jones
)

all_appointments = [
    appointment_1,
    appointment_2,
    appointment_3
]

# UPDATE PATIENT 2'S CONTACT NUMBER

print (f"Patient 2 contact before update: {patient_2.contact}")
patient_2.contact = "0400555666"
print (f"Patient 2 contact after update: {patient_2.contact}")

# RETRIEVE DR SMITH'S SCHEDULE

schedule = dr_smith.view_schedule(all_appointments)

print(f"\nSchedule for {dr_smith.practitioner_name}")

for appointment in schedule:
    print(
        f"Appointment ID: {appointment.appointment_id} | "
        f"Patient: {appointment.patient.patient_name} | "
        f"Time: {appointment.appointment_datetime}"
    )

# RETRIEVE DR JONES'S SCHEDULE
schedule = dr_jones.view_schedule(all_appointments)

print(f"\nSchedule for {dr_jones.practitioner_name}")

for appointment in schedule:
    print(
        f"Appointment ID: {appointment.appointment_id} | "
        f"Patient: {appointment.patient.patient_name} | "
        f"Time: {appointment.appointment_datetime}"
    )

# VIEW PATIENT 1'S APPOINTMENT HISTORY

print(f"\nAppointment history for {patient_1.patient_name}")
history = patient_1.view_history(all_appointments)
for appointment in history:
    print(
        f"Appointment ID: {appointment.appointment_id} | "
        f"Practitioner: {appointment.practitioner.practitioner_name} | "
        f"Time: {appointment.appointment_datetime}"
    )

# CANCEL APPOINTMENT 2

print(f"\nCancelling appointment ID: {appointment_2.appointment_id}")
appointment_2.cancel()
print(f"Appointment ID: {appointment_2.appointment_id} status: {appointment_2.status.value}")