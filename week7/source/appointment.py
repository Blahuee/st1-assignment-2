from enum import Enum
from datetime import datetime

class AppointmentStatus(Enum):
    SCHEDULED = "SCHEDULED"
    CANCELLED = "CANCELLED"
    COMPLETED = "COMPLETED"

class Appointment:
    def __init__(self, appointment_id: int, appointment_datetime: datetime, patient, practitioner, status: AppointmentStatus = AppointmentStatus.SCHEDULED) -> None:
        self.__appointment_id = appointment_id
        self.__appointment_datetime = appointment_datetime
        self.__patient = patient
        self.__practitioner = practitioner
        self.__status = status

    @property
    def appointment_id(self) -> int:
        return self.__appointment_id

    @property
    def appointment_datetime(self) -> datetime:
        return self.__appointment_datetime

    @property
    def patient(self):
        return self.__patient

    @property
    def practitioner(self):
        return self.__practitioner

    @property
    def status(self) -> AppointmentStatus:
        return self.__status

    def cancel(self) -> None:
        if self.__status == AppointmentStatus.CANCELLED:
            raise ValueError("Appointment already cancelled")

        self.__status = AppointmentStatus.CANCELLED

    def reschedule(self, new_datetime: datetime) -> None:
        if self.__status == AppointmentStatus.CANCELLED:
            raise ValueError(
                "Cancelled appointments cannot be rescheduled"
            )

        self.__appointment_datetime = new_datetime

    def check_conflict(self, other_appointment) -> bool:
        return (
            self.practitioner == other_appointment.practitioner
            and self.appointment_datetime
            == other_appointment.appointment_datetime
        )