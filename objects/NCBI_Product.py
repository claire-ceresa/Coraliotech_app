from PyQt5.QtWidgets import QInputDialog
from Bio import Entrez
from Bio import SeqIO
from Bio.SeqUtils.ProtParam import ProteinAnalysis
from objects.NCBI_Organism import NCBI_Organism
from objects.NCBI_CDS import NCBI_CDS
from database.functions_db import *
from graphic.graphics_functions import create_messageBox


class NCBI_Product:
    """
    Product object issued from the GenBank fiche
    """

    def __init__(self, id):

        self.id = id
        self.fiche = None
        self.name = None
        self.feature_cds = None
        self.feature_gene = None
        self.feature_source = None
        self.is_predicted = False
        self.is_partial = False
        self.note = None
        self.molecular_weight = None
        self.species = None
        self.cds = None

        self._set_properties()
        self._check_exception()

    # SETTER METHODS #

    def _set_properties(self):
        self._set_fiche()
        self._set_features()
        self._set_name()
        self._set_is_predicted()
        self._set_is_partial()
        self._set_notes()
        self._set_molecular_weight()
        self._set_species()
        self._set_cds()

    def _set_fiche(self):
        """Set the attribute sequence with a SeqRecord old_object"""
        try:
            fiche = Entrez.efetch(db="nucleotide", id=self.id, rettype="gb", retmode="text")
        except:
            print(str(id) + " inconnu dans la base de donnees")
        else:
            self.fiche = SeqIO.read(fiche, "genbank")

    def _set_features(self):
        """Set the attributes concerning features"""
        if self.fiche is not None:
            self.feature_cds = self.get_feature_by_type("CDS")
            self.feature_gene = self.get_feature_by_type("gene")
            self.feature_source = self.get_feature_by_type("source")

    def _set_name(self):
        """Set the attribute name"""
        if self.feature_cds is not None and 'product' in self.feature_cds.qualifiers:
            self.name = self.feature_cds.qualifiers["product"][0]

    def _set_is_predicted(self):
        """Set the boolean is_predicted"""
        if self.fiche is not None:
            self.is_predicted = "PREDICTED" in self.fiche.description

    def _set_is_partial(self):
        """Set the boolean is_partial"""
        if self.fiche is not None:
            self.is_partial = "partial" in self.fiche.description

    def _set_notes(self):
        """Set the attribute note"""
        if self.feature_gene is not None and 'note' in self.feature_gene.qualifiers:
            self.note = " ".join(self.feature_gene.qualifiers["note"])

    def _set_molecular_weight(self):
        """Set the attribute molecular weight"""
        translation = self.get_translation()
        if translation is not None:
            analysed_seq = ProteinAnalysis(translation)
            try:
                self.molecular_weight = round(analysed_seq.molecular_weight() * 0.001)
            except Exception as e:
                return False

    def _set_species(self):
        """Set the attribute species"""
        id = self.get_id_taxon()
        if id is not None:
            self.species = NCBI_Organism(id)

    def _set_cds(self):
        """Set the attribute cds with a CDS Object"""
        if self.feature_cds is not None:
            start = self.feature_cds.location.start
            stop = self.feature_cds.location.end
            offset = int(self.feature_cds.qualifiers["codon_start"][0])
            seqTOT = self.fiche.seq
            seqCDS = str(seqTOT[start:stop])
            if start is not None and stop is not None :
                self.cds = NCBI_CDS(int(start+offset), int(stop), offset, seqCDS)

    # ACCESSIBLE METHODS #

    def save_genbank_file(self):
        """Save the GenBank fiche in a TXT file"""
        SeqIO.write(self.fiche, "fiche.txt", "genbank")

    def get_translation(self):
        """:return the translation of the protein"""
        if self.feature_cds is not None and len(self.feature_cds.qualifiers["translation"]) > 0:
            translation = self.feature_cds.qualifiers["translation"][0]
            return translation
        return None

    def get_id_taxon(self):
        """:return the NCBI_Window id of the taxon"""
        if self.feature_source is not None:
            id = self.feature_source.qualifiers["db_xref"][0].strip('taxon:')
            return int(id)
        return None

    def get_feature_by_type(self, type):
        """
        Get all the information of a feature
        :param type: type of the feature you need (CDS, source, etc)
        :return: the old_object SeqFeature corresponding to the type
        """
        for feature in self.fiche.features:
            if feature.type == type:
                return feature
        return None

    def _check_exception(self):
        """Check some precise exception and print a message if needed"""
        if self.cds.offset is not None and self.cds.offset > 1:
            print(str(self.id) + " : codon start > 1 --> verifier la taille du cds pour confirmation formule")

    # METHODS DEALING WITH THE LOCAL DATABASE#

    def save_on_database(self):
        """Save the informations on the local DB"""
        organism_saved = self.save_organism()
        cds_saved = self.save_cds()
        product_saved = self.save_product()
        return {"organism":organism_saved, "cds":cds_saved, "product":product_saved}

    def save_cds(self):
        """Save the cds in the table CDS of the local DB"""
        datas_cds = {}
        datas_cds["id"] = "\"cds_" + self.id + "\""
        datas_cds["debut"] = str(self.cds.start)
        datas_cds["fin"] = str(self.cds.stop)
        datas_cds["poids_moleculaire"] = str(self.molecular_weight)
        datas_cds["complete"] = "0" if self.is_partial else "1"
        datas_cds["seqADN"] = "\"" + self.cds.seqADN + "\""
        query = get_query_insert("CDS", datas_cds)
        commit = commit_query(query)
        return commit

    def save_organism(self):
        """Save the organism in the table Organisme of the local DB"""
        datas_org = {}
        datas_org["espece"] = "\"" + self.species.species + "\"" if self.species.species is not None else "NULL"
        datas_org["genre"] = "\"" + self.species.genus + "\"" if self.species.genus is not None else "NULL"
        datas_org["famille"] = "\"" + self.species.family + "\"" if self.species.family is not None else "NULL"
        datas_org["ordre"] = "\"" + self.species.order + "\"" if self.species.order is not None else "NULL"
        datas_org["sous_classe"] = "\"" + self.species.subclass + "\"" if self.species.subclass is not None else "NULL"
        datas_org["classe"] = "\"" + self.species.classe + "\"" if self.species.classe is not None else "NULL"
        datas_org["embranchement"] = "\"" + self.species.phylum + "\"" if self.species.phylum is not None else "NULL"
        query = get_query_insert("Organisme", datas_org)
        commit = commit_query(query)
        return commit

    def save_product(self):
        """Save the product in the table Produit of the local DB"""
        datas_prod = {}
        datas_prod["id"] = "\"" + self.id + "\""
        datas_prod["nom"] = "\"" + self.name + "\""
        datas_prod["source"] = "\"NCBI\""
        datas_prod["note"] = "\"" + self.note + "\"" if self.note is not None else "NULL"
        datas_prod["espece"] = "\"" + self.species.species + "\""
        datas_prod["id_cds"] = "\"cds_" + self.id + "\""
        datas_prod["predicted"] = "1" if self.is_predicted else "0"
        query = get_query_insert("Produit", datas_prod)
        commit = commit_query(query)
        return commit


