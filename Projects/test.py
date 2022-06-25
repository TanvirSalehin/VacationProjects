from openpyxl import load_workbook

def gen(n):
	for i in range(n):
		yield i

temp = gen(3)

book = load_workbook("ROUTINE.xlsx")
sheet = book.active

rows = sheet.rows
days = [cell.value for cell in next(rows)]
periods = [cell.value for cell in next(rows)]
Teachers = []
for row in sheet["c3":"c5"]:
	for cell in row:
		Teachers.append(cell.value)

classes = {}

for teacher ,row in zip(Teachers, sheet["d3":"l5"]):
	classes_row = []
	for cell in row:
		classes_row.append(cell.value)
	classes[Teachers[next(temp)]] = classes_row

for index1 ,teacher in enumerate(classes):
	for index2, form in enumerate(classes[teacher]):
		if form == "8A":
			print(Teachers[index1], index2)

