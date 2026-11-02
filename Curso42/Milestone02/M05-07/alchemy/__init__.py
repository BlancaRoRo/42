# del archivo elements solo se expone create_air, create_earth no
from .elements import create_air

# nombres públicos del paquete (los que trae "from alchemy import *")
__all__ = ["create_air"]
__version__ = "1.0.0"
