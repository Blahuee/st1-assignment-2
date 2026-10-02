from appointment import Appointment

class Patient:
    def __init__(self, patient_id: int, patient_name: str, contact: str) -> None:
        self.__patient_id = patient_id
        self.__patient_name = patient_name
        self.__contact = contact
        self.__appointment = []

    def add_appointment(self, appointment) -> None:
        self.__appointment.append(appointment)

    def view_history(self, appointments: list) -> list:
        """Return appointments belonging to this patient."""
        return [
            appointment
            for appointment in appointments
            if appointment.patient == self
        ]

    @property
    def patient_id(self) -> int:
        return self.__patient_id
    
    @property
    def patient_name(self) -> str:
        return self.__patient_name

    @patient_name.setter
    def patient_name(self, new_patient_name: str) -> None:
        """_summary_ validate str not duplicate
        
                Args:
                    new_patient_name (str): patient new name eg last name
                """
        if isinstance(new_patient_name, str) and new_patient_name:
             self.__patient_name = new_patient_name

    @property
    def contact(self) -> str:
        return self.__contact

    @contact.setter
    def contact(self, new_contact: str) -> None:
        """_summary_ validate str value and no. of digits in new content

        Args:
            new_contact (str): patient new contact number
        """
        if (isinstance(new_contact, str) and new_contact.isdigit() and len(new_contact) == 10):
            self.__contact = new_contact
        else:
            raise ValueError("Contact number must contain exactly 10 digits.")

    def __str__(self) -> str:
        return f"{self.patient_id} has name {self.__patient_name} with contact: {self.contact}"