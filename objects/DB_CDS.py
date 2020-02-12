from database.functions_db import *


class DB_CDS:

    def __init__(self, id=None):
        self.id = id
        self.start = None
        self.stop = None
        self.length = None
        self.mw = None
        self.complete = None
        self.seqADN = None

        self.set_properties()

    def set_properties(self):
        cds = get_cds_by(id_cds=self.id)
        if cds["delete"] == 0:
            self.start = cds["start"]
            self.stop = cds["stop"]
            self.length = self.stop - self.start + 1
            self.mw = cds["mw"]
            self.complete = cds["complete"]
            self.seqADN = cds["seqADN"]