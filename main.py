

#from importacoes import *
from metodos import *


print"########################## ENEM  ##############################"

''' 
0-Ranking por nota  #ok
1-Ranking Por estado
2- nome de escolas(por nome)
3- municipios
4- UF
5 - Rede
6- Indicador de permanencia na escolas
7 - Media da escola
''' 

ran_por_not = read()

def menu():
	print "\n############### ############################# ###################\n"
	texto  = '\n0-Ranking por nota\n1 - Ranking Por estado\n2 - Nome de Escolas\n3 - municipios\n4 - UF\n5 - Rede\n6 - Indicador de permanencia na escola\n7 - media da escola\n8 -para sair '
	print texto
	opcao = input("\nEscolha sua opcao: ")
	while (opcao != 8):
		if opcao == 0:
			menu = '1 - Objetivas\n2 - Linguagens\n3 - Matematica\n4 - Natureza \n5 - Humanas\n6 - Redacao\n7 - Sair'
			op = 0
			print menu
			op = input("\nEscolha As opcoes da prova : ")
			while(op!=7):
				if op == 1:
					valores = ranking_por_nota(ran_por_not)
					for i in valores:
						print "%s--%s"%(i[1],i[7])
				'''if op == 2:
					valores = ranking_por_nota(ran_por_not,op)
					for i in valores:
						print "%s--%s"%(i[1],i[8])
				if op == 3:
					valores = ranking_por_nota(ran_por_not,op)
					for i in valores:
						print "%s--%s"%(i[1],i[9])
				if op == 4:
					valores = ranking_por_nota(ran_por_not,op)
					for i in valores:
						print "%s--%s"%(i[1],i[10])

				if op == 5:
					valores = ranking_por_nota(ran_por_not,op)
					for i in valores:
						print "%s--%s"%(i[1],i[11])
				if op == 6:
					valores = ranking_por_nota(ran_por_not,op)
					for i in valores:
						print "%s--%s"%(i[1],i[12])			
				'''
				op = input("\nEscolha As opcoes da prova : ")

				# elif op ==2:
				# 	valores = ranking_por_nota(ran_por_not)
		elif opcao == 1:
			pass	

		elif opcao == 2:
			print ranking(read())

			pass
		else:
			pass
		print texto
		opcao = input("\nEscolha sua opcao: ")
menu()


