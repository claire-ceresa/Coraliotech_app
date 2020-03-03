from Bio import Entrez

class NCBI_Search:

    def __init__(self, request):
        """
        object dealing with the NCBI research
        :param request: NCBI requet
        """
        self.request = request

    def get_list_ids(self):
        """
        Get the list of ids found with the NCBI request
        :return list
        """
        try:
            result = Entrez.esearch(db="nucleotide", term=self.request, idtype="acc", retmax=2500, usehistory='y')
            list = Entrez.read(result)
            if 'ErrorList' in list:
                ids = []
            else:
                ids = list["IdList"]
            return ids
        except Exception as e:
            self.errors.append(str(e))
