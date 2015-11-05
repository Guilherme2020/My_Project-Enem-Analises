'''Metodos do software '''

from importacoes import *


def ranking(lista, n =4):
	#lista = []
	return lista.sort(cmp_ranking)[:n]
	
	#rank = cmp_ranking()
	#print rank
	#for i in lista:
				
def cmp_ranking(x,y):
	return cmp(x[2],y[2])

	
print ranking(read())
#print ranking(read())
	