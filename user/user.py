from dataclasses import dataclass
from .constants import version

@dataclass
class GDVersion:
    """An object representing the Geometry Dash styled versioning system."""

    major: int
    minor: int
    patch: int # Not displayed if eq to 0
    bin_ver: int

    def into_str(self) -> str:
        """Returns the version of as a string, trying to match Geometry Dash's versioning.
        
        Examples:
            If patch = 0:
                `2.1`, `2.2`
            If patch > 0:
                `2.11`, `2.12`
        """
        return f"{self.major}.{self.minor}{self.patch or ''}"
    
    def __str__(self) -> str: return self.into_str()
    def __repr__(self) -> str: return f"<GDVersion {str(self)} ({self.bin_ver})>"
    
    def determine_device_type(self) -> version.DeviceType:
        """Determines the device type of the user based on the version information.
        
        Returns:
            version.DeviceType: The device type of the user.
        """
        
        # 1.9 if the first PC release.
        if self.major == 1 and self.minor < 9: return version.DeviceType.MOBILE
        # 2.13 has different bin vers for PC and mobile.
        elif self.bin_ver == 34: return version.DeviceType.PC
        elif self.bin_ver == 35: return version.DeviceType.MOBILE

        return version.DeviceType.UNKNOWN
    
    @property
    def mobile(self) -> bool:
        """Checks if it can be certainly determined that the user is playing on mobile
        based on the user's version information."""

        return self.determine_device_type() is version.DeviceType.MOBILE
    
    @property
    def pc(self) -> bool:
        """Checks if it can be certainly determined that the user is playing on PC/Mac
        (cannot be currently differentiated) based on the user's version information."""
        
        return self.determine_device_type() is version.DeviceType.PC

@dataclass
class Email:
    """A class for representing a user's email address."""

    prefix: str
    domain: str

    def into_str(self) -> str:
        """Returns the email address in standard string form."""
            
        return f"{self.prefix}@{self.domain}"
    
    def __str__(self) -> str: return self.into_str()
    def __repr__(self) -> str: return f"<Email {str(self)}>"
    
    @classmethod
    def from_str(cls, email: str) -> 'Email':
        """Creates an Email object from a string.
        
        Args:
            email (str): The email address to create the object from in standard
            string form eg `prefix@domain.com`.
        
        Returns:
            Email: The created Email object.
        """

        # Sanity checks
        assert "@" in email
        email_split = email.split("@")
        assert len(email_split) == 2
        assert "." in email_split[1]

        return cls(*email_split)
    
    @property
    def allowed(self) -> bool:
        """Checks if the email originates from a whitelisted domain."""

        # TODO: Implement the whitelist, preferably inside a database table.
        ...
