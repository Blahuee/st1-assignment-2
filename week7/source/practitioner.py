class Practitioner:
    def __init__(self, practitioner_id: int, practitioner_name: str, specialty: str) -> None:
        if practitioner_id <= 0:
            raise ValueError("Practitioner ID must be positive")
        
        self.__practitioner_id = practitioner_id
        self.practitioner_name = practitioner_name
        self.specialty = specialty

    @property
    def practitioner_id(self) -> int:
        return self.__practitioner_id

    @property
    def practitioner_name(self) -> str:
        return self.__practitioner_name

    @practitioner_name.setter
    def practitioner_name(self, new_practitioner_name: str) -> None:
        if not isinstance(new_practitioner_name, str) or not new_practitioner_name.strip():
            raise ValueError("Practitioner name cannot be empty")

        self.__practitioner_name = new_practitioner_name

    @property
    def specialty(self) -> str:
        return self.__specialty

    @specialty.setter
    def specialty(self, new_specialty: str) -> None:
        if not isinstance(new_specialty, str) or not new_specialty.strip():
            raise ValueError("Specialty cannot be empty")

        self.__specialty = new_specialty

    def view_schedule(self, appointments: list) -> list:
        """Return appointments belonging to this practitioner."""

        return [
            appointment
            for appointment in appointments
            if appointment.practitioner == self
        ]