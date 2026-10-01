class Patient:
    def __init__(self, patient_id: int, patient_name: str, contact: int) -> None:
        self.__patient_id = patient_id
        self.__patient_name = patient_name
        self.__contact = contact

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
    def contact(self) -> int:
        return self.__contact

    @contact.setter
    def contact(self, new_contact: int) -> None:
        """_summary_ validate int value and no. of digits in new content

        Args:
            new_contact (int): patient new contact number
        """
        if isinstance(new_contact, int) and new_contact >= 0 and len(str(abs(new_contact))) in (9, 10):
            self.__contact = new_contact

    def __str__(self) -> str:
        return f"{self.patient_id} has name {self.__patient_name} with contact: {self.contact}"