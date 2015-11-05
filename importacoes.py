''' 
1-Ranking
2- nome de escolas
3- municipios
4- UF
5 - Rede
6- Indicador de permanencia na escolas
7 - Media da escola





'''





def read(filename = 'enem_2014.csv'):
	lista = []

	file = open(filename)

	for f in file:
		'''item = re.sub(';[2]','',f.strip())
		item = item.split(";")'''
		it = f.strip().split(";")

		lista.append(item[2:15])

	file.close()

	return lista
print read()

