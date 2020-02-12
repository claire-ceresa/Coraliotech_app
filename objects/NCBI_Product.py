from Bio import Entrez
from Bio import SeqIO
from Bio.SeqUtils.ProtParam import ProteinAnalysis
from objects.NCBI_Organism import NCBI_Organism
from objects.NCBI_CDS import NCBI_CDS
from database.functions_db import *


class NCBI_Product:

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

        self.set_fiche()
        self.set_features()
        self.set_name()
        self.set_is_predicted()
        self.set_is_partial()
        self.set_notes()
        self.set_molecular_weight()
        self.set_species()
        self.set_cds()

        self._check_exception()

    def save_genbank_file(self):
        SeqIO.write(self.fiche, "fiche.txt", "genbank")

    def set_fiche(self):
        """set the attribute sequence with a SeqRecord old_object"""
        try:
            fiche = Entrez.efetch(db="nucleotide", id=self.id, rettype="gb", retmode="text")
        except:
            print(str(id) + " inconnu dans la base de donnees")
        else:
            self.fiche = SeqIO.read(fiche, "genbank")

    def set_is_predicted(self):
        """set the boolean is_predicted"""
        if self.fiche is not None:
            self.is_predicted = "PREDICTED" in self.fiche.description

    def set_is_partial(self):
        """set the boolean is_partial"""
        if self.fiche is not None:
            self.is_partial = "partial" in self.fiche.description

    def set_features(self):
        """set the attributes concerning features"""
        if self.fiche is not None:
            self.feature_cds = self.get_feature_by_type("CDS")
            self.feature_gene = self.get_feature_by_type("gene")
            self.feature_source = self.get_feature_by_type("source")

    def set_name(self):
        """set the attribute name"""
        if self.feature_cds is not None and 'product' in self.feature_cds.qualifiers:
            self.name = self.feature_cds.qualifiers["product"][0]

    def set_notes(self):
        """set the attribute note"""
        if self.feature_gene is not None and 'note' in self.feature_gene.qualifiers:
            self.note = " ".join(self.feature_gene.qualifiers["note"])

    def set_molecular_weight(self):
        """set the attribute molecular weight"""
        translation = self.get_translation()
        if translation is not None:
            analysed_seq = ProteinAnalysis(translation)
            try:
                self.molecular_weight = round(analysed_seq.molecular_weight() * 0.001)
            except Exception as e:
                return False

    def get_translation(self):
        """:return the translation of the protein"""
        if self.feature_cds is not None and len(self.feature_cds.qualifiers["translation"]) > 0:
            translation = self.feature_cds.qualifiers["translation"][0]
            return translation
        return None

    def set_species(self):
        """set the attribute species"""
        id = self.get_id_taxon()
        if id is not None:
            self.species = NCBI_Organism(id)

    def get_id_taxon(self):
        """:return the NCBI_Window id of the taxon"""
        if self.feature_source is not None:
            id = self.feature_source.qualifiers["db_xref"][0].strip('taxon:')
            return int(id)
        return None

    def set_cds(self):
        """set the attribute cds with a CDS Object"""
        if self.feature_cds is not None:
            start = self.feature_cds.location.start
            stop = self.feature_cds.location.end
            offset = int(self.feature_cds.qualifiers["codon_start"][0])
            if start is not None and stop is not None :
                self.cds = NCBI_CDS(int(start+offset), int(stop), offset)

    def get_feature_by_type(self, type):
        """:param type: type of the feature you need (CDS, source, etc)
        :return: the old_object SeqFeature corresponding to the type"""
        for feature in self.fiche.features:
            if feature.type == type:
                return feature
        return None

    def _check_exception(self):
        """check some precise exception and print a message if needed"""
        if self.cds.offset is not None and self.cds.offset > 1:
            print(str(self.id) + " : codon start > 1 --> verifier la taille du cds pour confirmation formule")

    def save_on_database(self):
        organism_saved = self.save_organism()
        cds_saved = self.save_cds()
        product_saved = self.save_product()
        return product_saved

    def save_cds(self):
        datas_cds = {}
        datas_cds["id"] = "\"cds_" + self.id + "\""
        datas_cds["debut"] = str(self.cds.start)
        datas_cds["fin"] = str(self.cds.stop)
        datas_cds["poids_moleculaire"] = str(self.molecular_weight)
        datas_cds["complete"] = "0" if self.is_partial else "1"
        query = get_query_insert("CDS", datas_cds)
        commit = commit_query(query)
        return commit

    def save_organism(self):
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


