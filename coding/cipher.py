from itertools import cycle
import base64

def cipher_xor(text: str, key: str) -> str:
    """Encrypts the string `text` using the XOR cipher with the key `key`.
    
    Args:
        text (str): The text that is to be encrypted using the XOR cipher.
        key (int): The key to be used within the encryption process.
    
    Returns:
        An XOR encoded string of param `text` using the key `key`.
    """

    return "".join(chr(ord(x) ^ ord(y)) for (x, y) in zip(str(text), cycle(key)))

def cipher_b64_encode(text: str) -> str:
    """Encodes the string `text` using the URL-safe Base64 algorithm.
    
    Args:
        text (str): The text that is to be encoded using the base64 algorithm.
    
    Returns:
        str: Base64 encoded string of param `text`.
    """

    return base64.urlsafe_b64encode(text.encode()).decode()
