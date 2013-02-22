from .default_settings import *
from .clubmembers_settings import *

try:
    from .local_settings import *
except ImportError:
    pass
