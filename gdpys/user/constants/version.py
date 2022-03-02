from enum import IntEnum


class DeviceType(IntEnum):
    """Enum representing a type of device the user is using, including all
    supported by Geometry Dash + one for unknown."""

    PC = 0
    MOBILE = 1
    UNKNOWN = 2
