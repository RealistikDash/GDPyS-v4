from coding import hashes
from typing import Optional
import asyncio


class AuthComponent:
    """Manages the handling of credential authentication for a user, managing
    the caching of the password hash result. This is also a thread-safe class, using
    asynchronous locks."""

    def __init__(self, user_id: int, bcrypt_pw: Optional[str]) -> None:
        self._user_id = user_id
        self._lock = asyncio.Lock()
        self._known_gjp = None
        self._hash = bcrypt_pw

    def _reset_cached_gjp(self) -> None:
        """Resets the cached GJP value."""

        self._known_gjp = None

    async def set_password(self, bcrypt_pw: str) -> None:
        """Sets the password hash for the user. This will automatically reset the
        cached GJP value.

        Args:
            bcrypt_pw (str): The bcrypt hash of the password to set.

        Note:
            This method acquires the auth lock before setting the hash and clearing
            the cached GJP value.
        """

        async with self._lock:
            self._hash = bcrypt_pw
            self._reset_cached_gjp()

    async def compare_password(self, password: str) -> bool:
        """Compares the plaintext password to the stored password hash.

        Args:
            password (str): The password to be compared.

        Returns:
            bool: Whether or not the password matches the stored hash.

        Note:
            This method acquires the auth lock before comparing the password.
            This method does not implement any caching, and runs a bcrypt check
            every time its called.
        """

        async with self._lock:
            return await self._compare_password(password)

    async def _compare_password(self, password: str) -> bool:
        """Compares the plaintext password to the stored password hash.

        Args:
            password (str): The password to be compared.

        Returns:
            bool: Whether or not the password matches the stored hash.

        Note:
            This method does not implement any caching, and runs a bcrypt check
            every time its called.
        """

        return await hashes.compare_bcrypt_async(password, self._hash)
