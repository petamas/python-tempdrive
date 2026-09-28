__all__ = [
    'ByRef',
]

import ctypes
from typing import TYPE_CHECKING
from typing import Generic
from typing import TypeVar

if TYPE_CHECKING:
    _CData = ctypes._CData
else:
    _CData = object

CDataT = TypeVar('CDataT', bound=_CData)


class ByRef(Generic[CDataT]):
    """
    Typed alternative to ctypes.byref()
    """

    def __init__(self, value: CDataT) -> None:
        self._as_parameter_ = ctypes.byref(value)
