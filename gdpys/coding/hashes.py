import bcrypt
import asyncio


def hash_bcrypt(password: str) -> str:
    """Hashes a password using the bcrypt algorithm with a random salt, returning
    the resulting hash.

    Args:
        password (str): The password to be hashed.

    Returns:
        str: The hashed password."""

    return bcrypt.hashpw(password.encode(), bcrypt.gensalt(12)).decode()


def compare_bcrypt(password: str, hash: str) -> bool:
    """Compares a password to a hash using the bcrypt algorithm. If the check
    fails due to an incorrect hash format, False will still be returned.

    Args:
        password (str): The password to be compared.
        hash (str): The hash to be compared to.

    Returns:
        bool: Whether or not the password matches the hash."""

    try:
        return bcrypt.checkpw(password.encode(), hash.encode())
    except ValueError:
        return False


async def compare_bcrypt_async(password: str, hash: str) -> bool:
    """Compares a password to a hash using the bcrypt algorithm. This check is ran
    within a loop executor to prevent blocking the main thread for extended quantities of time.
    If the check fails due to an incorrect hash format, False will still be returned.

    Args:
        password (str): The password to be compared.
        hash (str): The hash to be compared to.

    Returns:
        bool: Whether or not the password matches the hash."""

    loop = asyncio.get_event_loop()
    return await loop.run_in_executor(None, compare_bcrypt, password, hash)
