 
from typing import List
import docx

from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel


class DocxIngestor(IngestorInterface):
    """The Docx Ingestor Class, to ingestor Docx quotes

    Args:
        IngestorInterface: This class inherits from Interface
    """
    allowed_extensions = ['docx']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        if not cls.can_ingest(path):
            raise Exception('cannot ingest exception')

        quotes = []
        doc = docx.Document(path)

        for para in doc.paragraphs:
            if para.text != "":
                parse = para.text.split(' - ')
                new_quote = QuoteModel(parse[0], parse[1])
                quotes.append(new_quote)

        return quotes