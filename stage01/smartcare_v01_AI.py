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