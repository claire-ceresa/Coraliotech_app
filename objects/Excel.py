import xlsxwriter as x

class Excel:

    def __init__(self, title):
        self.title = title
        self.workbook = x.Workbook(self.title)
        self.worksheets = []

    def add_worksheet(self, title):
        """add a worksheet to the workbook"""
        worksheet = self.workbook.add_worksheet(title)
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
        title = worksheet.get_name()
        columns_name = datas["column_names"]

        worksheet.merge_range(0, 0, 0, len(columns_name),title)
        format_columns_name = self.workbook.add_format({'bold':True, 'valign':'center'})
        worksheet.write_row(1, 0, columns_name)

        try:
            worksheet.set_row(0, None, format_columns_name)
        except Exception as e:
            print(e)

        for row, row_data in enumerate(datas["rows"]):
            worksheet.write_row(row+2, 0, row_data)