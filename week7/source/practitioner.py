class Practitioner:
    def __init__(self, practitioner_id: int, practitioner_name: str, specialty: str) -> None:
        self.__practitioner_id = practitioner_id
        self.__practitioner_name = practitioner_name
        self.__specialty = specialty

    @property
    def practitioner_id(self) -> int:
        return self.__practitioner_id

    @property
    def practitioner_name(self) -> str:
        return self.__practitioner_name

    @practitioner_name.setter
    def practitioner_name(self, new_practitioner_name: str) -> None:
        """_summary_ validate str not duplicate
                
                Args:
                    new_practitioner_name (str): practitioner new name eg last name
                """
        if isinstance(new_practitioner_name, str) and new_practitioner_name:
                self.__practitioner_name = new_practitioner_name

    @property
    def specialty(self) -> str:
        return self.__specialty