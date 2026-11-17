from datetime import datetime

from pydantic import BaseModel, Field, ValidationError

# Pydantic: libreria de python que valida datos.
# Funciona gracias a los type hints, si le entra un dato
# que puede convertir al necesitado lo hace, sino lanza error


# BaseModel: sirve para crear un modelo de atributos que validar
# Field: te permite añadir condiciones a la hora de validar
class SpaceStation(BaseModel):
    # min_length / max_length: limites de longitud (strings)
    station_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=1, max_length=50)
    # ge / le: limites de valor (numeros), ambos incluidos
    crew_size: int = Field(ge=1, le=20)
    power_level: float = Field(ge=0.0, le=100.0)
    oxygen_level: float = Field(ge=0.0, le=100.0)
    # sin valor por defecto -> obligatorio
    last_maintenance: datetime
    # para poner un campo por defecto, pones el valor
    is_operational: bool = True
    # str | None = acepta cualquiera de esos datos
    # default=None, te permite no pasarle el argumento
    notes: str | None = Field(default=None, max_length=200)


def main() -> None:
    print("Space Station Data Validation")
    print("========================================")
    try:
        # pydantic tambien aceptaria el string "2025-03-14T09:30:00"
        # y lo convertiria a datetime, pero mypy lo marcaria como error
        station = SpaceStation(
            station_id="ISS001",
            name="International Space Station",
            crew_size=6,
            power_level=85.5,
            oxygen_level=92.3,
            last_maintenance=datetime(2025, 3, 14, 9, 30),
        )
        status = "Operational" if station.is_operational else "Not Operational"
        print("Valid station created:")
        print(f"ID: {station.station_id}")
        print(f"Name: {station.name}")
        print(f"Crew: {station.crew_size} people")
        print(f"Power: {station.power_level}%")
        print(f"Oxygen: {station.oxygen_level}%")
        print(f"Status: {status}")
    except ValidationError as e:
        print("Unexpected validation error:")
        print(e.errors()[0]["msg"])

    print("\n========================================")
    try:
        SpaceStation(
            station_id="ISS002",
            name="Overcrowded Station",
            crew_size=21,
            power_level=50.0,
            oxygen_level=80.0,
            last_maintenance=datetime(2025, 1, 10, 12, 0),
        )
    except ValidationError as e:
        print("Expected validation error:")
        # e.errors() devuelve una lista de dicts, uno por error;
        # la clave "msg" contiene solo el mensaje legible
        print(e.errors()[0]["msg"])


if __name__ == "__main__":
    main()
