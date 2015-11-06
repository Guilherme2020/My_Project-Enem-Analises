'''Metodos do software 
	0-Ranking por nota
	1-Ranking
	2- nome de escolas
	3- municipios
	4- UF
	5 - Rede
	6- Indicador de permanencia na escolas
	7 - Media da escol
'''

#from importacoes import *
'''chaves = {
		1:7,
		2:8,
		3:9,
		4:10,
		5:11,
		6:12
	}

ca = 0  
'''
def read(filename = 'enem_2014.csv'):
	escolas = []

	file = open(filename)

	for f in file:
		'''item = re.sub(';[2]','',f.strip())
		item = item.split(";")'''
		it = f.strip().split(";")

		escolas.append(it)
		#print escolas

	file.close()
	return escolas


def ranking_por_nota(lista,n = 10):
	#ca = chave
	return lista[:n]


def por_nota(lista):
	
	return lista[7]

def ranking(escolas, n =10):
	lista = []
	escolas.sort()
	
	for i in range(0,10):
		lista.append(escolas[i])

	return escolas[:n]
	#rank = cmp_ranking()
	#print rank
	#for i in lista:

def rank_por_estado(escolas,estado,n=10):

	pass


def  por_nome(lista):
	pass



#print read()
#print ranking(read())

#print ranking(read())
	