class NCBI_CDS:

    def __init__(self, start=None, stop=None, offset=None, seqADN=None):
        """
        CDS object, issued from the GenBank fiche
        :param start: beginning position of the cds
        :param stop: ending position of the cds
        :param offset: offset value precised on the fiche
        :param seqADN: complete ADN sequence
        """
        self.start = start
        self.stop = stop
        self.length = None
        self.offset = offset
        self.seqADN = seqADN

        self._set_length()

    def _set_length(self):
        """Set the attribute length"""
        if self.start is not None and self.stop is not None:
            self.length = self.stop - self.start + 1