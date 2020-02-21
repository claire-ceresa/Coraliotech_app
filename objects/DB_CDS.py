from database.functions_db import *


class DB_CDS:
    """
    CDS object, issued of the local database
    """

    def __init__(self, id=None):
        self.id = id
        self.start = None
        self.stop = None
        self.length = None
        self.mw = None
        self.complete = None
        self.seqADN = None

        if self.id is not None:
            self._set_properties()

    def get_all_attributes(self):
        dict = self.__dict__.keys()
        return list(dict)

    def get_value(self, attribute):
        try:
            value = getattr(self, attribute)
        except AttributeError:
            value = None
        return value

    def _set_properties(self):
        """set all the variables with the values"""
        cds = get_cds_by(id_cds=self.id)
        self.start = cds["start"]
        self.stop = cds["stop"]
        self.length = self.stop - self.start + 1
        self.mw = cds["mw"]
        self.complete = cds["complete"]
        self.seqADN = cds["seqADN"]