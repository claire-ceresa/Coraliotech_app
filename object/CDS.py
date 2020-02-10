class CDS:

    def __init__(self, start=None, stop=None, offset=None):
        self.start = start
        self.stop = stop
        self.length = None
        self.offset = offset

        self.set_length()

    def set_length(self):
        """set the attribute length"""
        if self.start is not None and self.stop is not None:
            self.length = self.stop - self.start + 1