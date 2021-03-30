from abc import ABC, abstractmethod

import pandas

class IngestorInterface(ABC):

    @classmethod
    def can_ingest(cls, path: str)->bool:
        pass

    
    importers = [DocxImporter, CSVImporter]
    
    @classmethod
    def parse(cls, path: str) -> List[Cat]:
        for importer in cls.importers:
            if importer.can_ingest(path):
                return importer.parse(path)


class DocxImporter(IngestorInterface):
    
    allowed_extensions = ['docx']
    
    @classmethod
    def parse(cls, path: str):
        if not cls.can_ingest(path):
            raise Exception('cannot ingest exeption')
        
        cats = []
        doc = docx.Document(path)
        
        for para in doc.paragraphs:
            if para.text != "":
                parse = para.text.split(',')
                new_cat = Cat(parse[0], int(parse[1]), bool(parse[2]) )
                cats.append(new_cat)
        
        return cats

class CSVImporter(IngestorInterface):
    allowed_extensions = ['csv']

    @classmethod
    def parse(cls, path: str) -> List[Cat]:
        if not cls.can_ingest(path):
            raise Exception('cannot ingest exception')

        cats = []
        df = pandas.read_csv(path, header=0)

        for index, row in df.iterrows():
            new_cat = Cat(row['Name'], row['Age'], row['isIndoor'])
            cats.append(new_cat)

        return cats