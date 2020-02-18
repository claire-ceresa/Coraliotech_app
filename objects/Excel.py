import xlsxwriter as x

class Excel:

    def __init__(self, title):
        self.title = title
        self.workbook = x.Workbook(self.title)
        self.worksheets = []

    def add_worksheet(self):
        """add a worksheet to the workbook"""
        worksheet = self.workbook.add_worksheet()
        self.worksheets.append(worksheet)
        return worksheet

    def close(self):
        """close the workbook"""
        self.workbook.close()

    def add_QTableWidget(self, table, worksheet):
        """adding a QTableWidget to a worksheet"""
        headers = []

        for column in range(table.columnCount()):
            header = table.horizontalHeaderItem(column)
            if header is not None:
                headers.append(header.text())
            else:
                headers.append("Column " + str(column))
        worksheet.write_row(0, 0, headers)

        for row in range(table.rowCount()):
            rowdata = []
            for column in range(table.columnCount()):
                item = table.item(row, column)
                if item is not None:
                    rowdata.append(item.text())
                else:
                    rowdata.append('')
            worksheet.write_row(row+1, 0, rowdata)

    def add_data(self, worksheet, datas):
        for row, row_data in enumerate(datas):
            worksheet.write_row(row, 0, row_data)

    # def set_head(self, worksheet):
    #     """set all the format of the head of the worksheet"""
    #     format_head = self.workbook.add_format({'align':'center',
    #                                        'valign':'vcenter',
    #                                        'font_size':30,
    #                                         'bold':True})
    #     worksheet.merge_range('A1:F1', worksheet.name.upper(), format_head)
    #     worksheet.set_column(0, len(self.column_titles)-1, width=22)
    #     for title in enumerate(self.column_titles):
    #         format_title_column = self.workbook.add_format({'bold':True})
    #         worksheet.write(1, title[0], title[1].upper(), format_title_column)
    #
    # def add_data(self, worksheet, datas):
    #     """adding the data to each cells"""
    #     for line in enumerate(datas):
    #         for column in enumerate(line[1].values()):
    #             worksheet.write(line[0] + 2, column[0], column[1])
    #
