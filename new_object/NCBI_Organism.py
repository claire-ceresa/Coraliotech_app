from Bio import Entrez


class NCBI_Organism:

    def __init__(self, id=None):
        self.id = id
        self.taxonomy = None
        self.lineage = None
        self.species = None
        self.family = None
        self.genus = None
        self.order = None
        self.subclass = None
        self.classe = None
        self.phylum = None

        self.set_taxonomy()
        self.set_lineage()
        if self.taxonomy is not None and len(self.taxonomy) > 0:
            self.set_properties()

    def set_taxonomy(self):
        """set the attribute taxonomy"""
        if self.id is not None:
            get_taxonomy = Entrez.efetch(db="Taxonomy", id=self.id, retmode="xml")
            self.taxonomy = Entrez.read(get_taxonomy)

    def set_lineage(self):
        if self.taxonomy is not None:
            self.lineage = self.taxonomy[0]["LineageEx"]

    def set_properties(self):
        self.species = self.taxonomy[0]["ScientificName"]
        genus = next((item for item in self.lineage if item["Rank"] == "genus"), None)
        self.genus = genus["ScientificName"] if genus is not None else None
        family = next((item for item in self.lineage if item["Rank"] == "family"), None)
        self.family = family["ScientificName"] if family is not None else None
        order = next((item for item in self.lineage if item["Rank"] == "order"), None)
        self.order = order["ScientificName"] if order is not None else None
        subclass = next((item for item in self.lineage if item["Rank"] == "subclass"), None)
        self.subclass = subclass["ScientificName"] if subclass is not None else None
        classe = next((item for item in self.lineage if item["Rank"] == "class"), None)
        self.classe = classe["ScientificName"] if classe is not None else None
        phylum = next((item for item in self.lineage if item["Rank"] == "phylum"), None)
        self.phylum = phylum["ScientificName"] if phylum is not None else None
