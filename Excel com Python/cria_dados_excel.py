import openpyxl

wb = openpyxl.Workbook()

planilha = wb.active

palavras = ['banana', 'maça', 'uva', 'pera']


for i in range(len(palavras)):
    c1 = planilha.cell(row=i+1, column=1)
    c1.value = palavras[i]

wb.save("palavras.xlsx")
