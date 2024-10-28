from openpyxl import load_workbook

wb = load_workbook('./A_1832154597_100008_1_11zon.xlsx')
ws = wb.active
# ws.page_setup.fitToWidth = 1
# ws.page_setup.fitToHeight = False
ws.page_setup.orientation = ws.ORIENTATION_LANDSCAPE
# ws.page_setup.fitToWidth = 1
# ws.page_setup.fitToHeight = False
ws.sheet_properties.pageSetUpPr.fitToPage = True
ws.page_setup.fitToHeight = False
ws.page_setup.fitToWidth = 1
wb.save('./test3.xlsx')