from typing import Optional, TypeVar, Union
import asyncio

T = TypeVar("T")
INDEXES = Union[int, str, tuple]


class LRUAsyncCache:
    """
    A memory based LRU cache implementation based on a key and value pair.
    Upon exceeding the max specified capacity, the last added object will be
    dropped from the internal dictionary. Additionally, any public fetch/insert
    operation will acquire the async lock.
    """

    def __init__(self, max_capacity: int) -> None:
        self.max_capacity = max_capacity
        self._store: dict[INDEXES, CacheStorage] = {}
        self._lock = asyncio.Lock()

    def __len__(self) -> int:
        """Retrieves the quantity of items currently stored within the cache."""

        return len(self._store)

    def __bool__(self) -> bool:
        """Returns a bool corresponding to whether the cache currently has objects
        stored within it."""

        return not self.empty

    @property
    def empty(self) -> bool:
        """Returns a bool corresponding to whether the cache is currently empty."""

        return len(self._store) == 0

    @property
    def at_capacity(self) -> bool:
        """Returns a bool corresponding to whether the cache is operating at
        maximum specified capacity."""

        # This assumes that we can NEVER go over the capacity.
        return len(self) == self.max_capacity

    def __get_last_item_index(self) -> Optional[INDEXES]:
        """Retrieves the index value of the oldest item within the cache."""

        # Running later code while the cache is empty will yield an `IndexError`
        if self.empty:
            return

        return next(iter(self._store))

    def __remove_oldest_item(self) -> bool:
        """
        Drops the oldest item from the cache.

        Note:
            Assumes that the cache lock is acquired.

        Returns:
            bool: Whether an item actually has been removed.
        """

        if not (key := self.__get_last_item_index()):
            return False

        del self._store[key]
        return True


class CacheStorage:
    """
    An object utilised for the storage of an object within the cache. Alongside
    storing a reference to the object, it also features an access lock used by
    the `CacheReference` object.
    """

    __slots__ = ("obj", "lock")

    def __init__(self, obj: T) -> None:
        self.obj = obj
        self.lock = asyncio.Lock()


class CacheReference:
    ...
