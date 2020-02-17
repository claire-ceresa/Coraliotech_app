from database.functions_db import *


class DB_Organism:
    """
    Organism object, issued of the local database
    """

    def __init__(self, species=None):
        self.species = species
        self.genus = None
        self.family = None
        self.order = None
        self.subclass = None
        self.classe = None
        self.phylum = None
        self.statut = None

        self._set_properties()

    def _set_properties(self):
        organism = get_organism_by_species(self.species)
        self.genus = organism["genus"]
        self.family = organism["family"]
        self.order = organism["order"]
        self.subclass = organism["subclass"]
        self.classe = organism["classe"]
        self.phylum = organism["phylum"]
        self.statut = organism["statut"]
