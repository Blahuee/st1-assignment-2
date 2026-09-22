# Patient Class
class Patient:
    def __init__(self, patient_id, name, contact_details):
        self.patient_id = patient_id
        self.name = name
        self.contact_details = contact_details

    def view_history(self):
        pass

# Practitioner Class
class Practitioner:
    def __init__(self, practitioner_id, name, specialty):
        self.practitioner_id = practitioner_id
        self.name = name
        self.specialty = specialty

    def view_schedule(self):
        pass

# Appointment Class
class Appointment:
    def __init__(self, appointment_id, appointment_datetime, status,
                 patient, practitioner):
        self.appointment_id = appointment_id
        self.appointment_datetime = appointment_datetime
        self.status = status
        self.patient = patient
        self.practitioner = practitioner

    def cancel(self):
        pass

    def reschedule(self, new_datetime):
        pass

    def check_conflict(self):
        pass