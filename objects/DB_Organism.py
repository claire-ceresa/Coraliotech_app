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

        if species is not None:
            self._set_properties()

    def get_all_attributes(self):
        """
        Get all the attributes of the class
        :return: list
        """
        dict = self.__dict__.keys()
        return list(dict)

    def get_value(self, attribute):
        """
        Get the value of an attribute
        :param attribute: string
        :return: the value of the attribute
        """
        try:
            value = getattr(self, attribute)
        except AttributeError:
            value = None
        return value

    def _set_properties(self):
        """Set all the variables with the values"""
        organism = get_organism_by_species(species=self.species)
        self.genus = organism["genus"]
        self.family = organism["family"]
        self.order = organism["order"]
        self.subclass = organism["subclass"]
        self.classe = organism["classe"]
        self.phylum = organism["phylum"]
        self.statut = organism["statut"]
