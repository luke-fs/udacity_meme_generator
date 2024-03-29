from abc import ABC, abstractmethod

from typing import List
from .QuoteModel import QuoteModel

class IngestorInterface(ABC):
    """The Interface for the different Ingestors
    Args:
        ABC: Inheritance from the abstract base class
    """

    @classmethod
    def can_ingest(cls, path: str)->bool:
        ext = path.split('.')[-1]
        return ext in cls.allowed_extensions

    #enforce to implement child classes the method
    @classmethod
    @abstractmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        pass