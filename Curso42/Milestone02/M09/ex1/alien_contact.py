from pydantic import BaseModel, ValidationError, Field, model_validator
from datetime import datetime
from enum import Enum


class ContactType(Enum):
    RADIO = "radio"
    VISUAL = "visual"
    PHYSICAL = "physical"
    TELEPATHIC = "telepathic"


class AlienContact(BaseModel):
    contact_id: str = Field(min_length=5, max_length=15)
    timestamp: datetime
    location: str = Field(min_length=3, max_length=100)
    contact_type: ContactType
    signal_strength: float = Field(ge=0.0, le=10.0)
    duration_minutes: int = Field(ge=1, le=1440)
    witness_count: int = Field(ge=1, le=100)
    message_received: str | None = Field(default=None, max_length=500)
    is_verified: bool = False

    # @model_validator indica que es un decorador
    # este decorador marca el metodo para que se ejecute al crear cada
    # objeto, despues de validar los campos: sirve de segundo filtro,
    # por eso no se llama a mano. Tiene que estar DENTRO de la clase.
    # Pydantic captura mi ValueError y devuelve el ValidationError
    @model_validator(mode='after')
    def Custom_Validation_Rules(self) -> "AlienContact":
        if not self.contact_id.startswith("AC"):
            raise ValueError("Contact ID must start with 'AC'")
        if (self.contact_type is ContactType.PHYSICAL
                and not self.is_verified):
            raise ValueError("Physical contact reports must be verified")
        if (self.contact_type is ContactType.TELEPATHIC
                and self.witness_count < 3):
            raise ValueError(
                "Telepathic contact requires at least 3 witnesses")
        if self.signal_strength > 7 and not self.message_received:
            raise ValueError(
                "Strong signals (> 7.0) should include received messages")
        return self


def main() -> None:
    print("Alien Contact Log Validation")
    print("======================================")
    try:
        alien = AlienContact(
            contact_id="AC_2024_001", contact_type=ContactType.RADIO,
            timestamp=datetime(2025, 3, 14, 9, 30),
            location="Area 51, Nevada", signal_strength=8.5,
            duration_minutes=45, witness_count=5,
            message_received="Greetings from Zeta Reticuli",
        )
        print("Valid contact report:")
        print(f"ID: {alien.contact_id}")
        # .value: el valor del Enum ("radio")
        print(f"Type: {alien.contact_type.value}")
        print(f"Location: {alien.location}")
        print(f"Signal: {alien.signal_strength}/10")
        print(f"Duration: {alien.duration_minutes} minutes")
        print(f"Witnesses: {alien.witness_count}")
        print(f"Message: '{alien.message_received}'")
    except ValidationError as e:
        print("Unexpected validation error:")
        print(e.errors()[0]["msg"])
    print("\n======================================")
    try:
        AlienContact(
            contact_id="AC_2024_001", contact_type=ContactType.TELEPATHIC,
            timestamp=datetime(2025, 3, 14, 9, 30),
            location="Area 51, Nevada", signal_strength=8.5,
            duration_minutes=45, witness_count=1,
            message_received="Greetings from Zeta Reticuli",
        )
    # se usa ctx pq se le añade al dict un type para decirle que
    # proviene del ValueError
    except ValidationError as e:
        print("Expected validation error:")
        print(e.errors()[0]["ctx"]["error"])


if __name__ == "__main__":
    main()
