from Bio import Entrez

from object.Excel import Excel
from object.Organism import Organism


class Search:

    #def __init__(self, organism, request, type):
    def __init__(self, request):
        #self.organism = Organism(term=organism)
        self.request = request
        # self.type = type
        # self.errors = []
        # self.list_ids = None
        # self.file_created = False
        # self.nb_result = 0

        #self.go(request)


    def get_list_ids(self):
        """get the list of ids found with the request"""
        try:
            result = Entrez.esearch(db="nucleotide", term=self.request, idtype="acc", retmax=2500, usehistory='y')
            list = Entrez.read(result)
            if 'ErrorList' in list:
                ids = []
            else:
                ids = list["IdList"]
            return ids
        except Exception as e:
            self.errors.append(e)

    # def go(self, request):
    #     """actions to do the research"""
    #     self.list_ids = self.get_list_ids(request)
    #     self.nb_result = len(self.list_ids)
    #
    #     if self.nb_result > 0:
    #
    #         try:
    #             datas = self.get_all_data()
    #         except Exception as e:
    #             self.errors.append(e)
    #         else:
    #             try:
    #                 self.write_xls(datas)
    #             except Exception as e:
    #                 self.errors.append(e)
    #
    #
    # def get_all_data(self):
    #     """get all the data of the request, as a list of lists"""
    #     proteins = []
    #
    #     for id in enumerate(self.list_ids):
    #         protein = Protein(id[1])
    #
    #         if protein.molecular_weight is None:
    #             continue
    #
    #         if self.type == "mRNA complete cds":
    #             line = {'genus': protein.species.genus,
    #                     'species': protein.species.name,
    #                     'name': protein.name,
    #                     'l': protein.cds.length,
    #                     'mw': protein.molecular_weight,
    #                     'id': protein.id}
    #
    #         elif self.type == "mRNA complete cds hypothetical":
    #             line =  {'genus': protein.species.genus,
    #                     'species': protein.species.name,
    #                     'name': protein.name,
    #                     'id': protein.id}
    #
    #         elif self.type == "mRNA collagen":
    #
    #             if protein.is_predicted is True:
    #                 predicted = "*"
    #             else:
    #                 predicted = ""
    #
    #             line = {'genus': protein.species.genus,
    #                     'species': protein.species.name,
    #                     'name': protein.name,
    #                     'id': protein.id,
    #                     'l': protein.cds.length,
    #                     'mw':protein.molecular_weight,
    #                     'pred':predicted,
    #                     'note':protein.note}
    #
    #         print(id[0])
    #         print(line)
    #         proteins.append(line)
    #
    #     return sorted(proteins, key= lambda i: i['species'])
    #
    # def write_xls(self, datas):
    #     """write the results of the request in an Excel file"""
    #     try:
    #         type = self.type.replace(" ", "_")
    #         file = Excel(self.organism.order, type)
    #         file.create_worksheet(self.organism.family.upper(), datas)
    #         file.close()
    #     except Exception as e:
    #         self.errors.append(e)
    #         self.file_created = False
    #     else:
    #         self.file_created = True
    #
