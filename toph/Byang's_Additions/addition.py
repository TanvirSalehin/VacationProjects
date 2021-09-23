def work(listb, lista):
	if len(listb) > len(lista):
		i = 0
		while len(listb) != len(lista):
			lista.insert(0, 0)
			i += 1
		listb = listb[i:]
		lista = lista[i:]
	elif len(listb) < len(lista):
		i = 0
		while len(listb) != len(lista):
			listb.insert(0, 0)
			i += 1
		listb = listb[i:]
		lista = lista[i:]
	else:
		pass

	return listb, lista

def res(listb, lista):
	for i in range(len(listb)):
		if int(listb[i]) + int(lista[i]) >= 10:
			return True
	return False

b, a = map(int, input().split())
result = "No"

listb = []
lista = []
for i in str(b):
	listb.append(i)
for i in str(a):
	lista.append(i)

listb, lista = work(listb, lista)

if res(listb, lista):
	result = "Yes"

print(result)