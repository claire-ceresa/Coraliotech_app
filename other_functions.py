import openpyxl as o
import re

def clean_collagen(title_file):
    file = o.load_workbook(title_file)
    worksheets = file.worksheets

    for worksheet in worksheets:
        max_row = worksheet.max_row

        for row in range(4, max_row+1) :
            cell_note = 'J' + str(row)
            note = worksheet[cell_note].value
            beginning_added = None
            end_added = None

            position_coverage = note.find('% coverage')
            if position_coverage > 0:
                percentage = note[position_coverage-3:position_coverage+1]
                cell_percentage = 'H' +  str(row)
                worksheet[cell_percentage].value = percentage

            for index_added in re.finditer('added', note):
                beginning_added = index_added.end()+1
            for index_bases in re.finditer("bases", note):
                end_added = index_bases.start()
            if beginning_added is not None and end_added is not None:
                number = note[int(beginning_added):int(end_added)]
                cell_added = 'I' + str(row)
                worksheet[cell_added].value = number

    file.save("new_collagen.xlsx")
    file.close()
