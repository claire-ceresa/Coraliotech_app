import xlsxwriter as x

class Excel:

    def __init__(self, title):
        self.title = title
        self.workbook = x.Workbook(self.title)
        self.worksheets = []
        #self.column_titles = ["Genre", "Especes", "Nom du gène", "Taille CDS (pb)", "PM theorique (kD)", "GenBank"]

    def create_worksheet(self, name, datas):
        """create a worksheet in the workbook"""
        worksheet = self.workbook.add_worksheet(name)
        self.worksheets.append(worksheet)
        self.set_head(worksheet)
        self.add_data(worksheet, datas)

    def set_head(self, worksheet):
        """set all the format of the head of the worksheet"""
        format_head = self.workbook.add_format({'align':'center',
                                           'valign':'vcenter',
                                           'font_size':30,
                                            'bold':True})
        worksheet.merge_range('A1:F1', worksheet.name.upper(), format_head)
        worksheet.set_column(0, len(self.column_titles)-1, width=22)
        for title in enumerate(self.column_titles):
            format_title_column = self.workbook.add_format({'bold':True})
            worksheet.write(1, title[0], title[1].upper(), format_title_column)

    def add_data(self, worksheet, datas):
        """adding the data to each cells"""
        for line in enumerate(datas):
            for column in enumerate(line[1].values()):
                worksheet.write(line[0] + 2, column[0], column[1])

    def close(self):
        """close the workbook"""
        self.workbook.close()
