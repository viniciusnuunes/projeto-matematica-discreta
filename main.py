from item import Item
from itemEntrega import ItensEntrega
from local import Local
from locais import Locais
from caminhao import Caminhao
from caminhoes import Caminhoes

# from pythonds.basic import Queue
# from pythonds.basic import Stack

# pilha - fila - lista

# Criando os Itens
item1 = Item('1', 'celular')
item2 = Item('2', 'relogio')
item3 = Item('3', 'bolsa')
item4 = Item('4', 'garrafa')
item5 = Item('5', 'caixa de som')
item6 = Item('6', 'notebook')

# Criando e empilhando a estrutura de Itens
itensEntrega1 = ItensEntrega()
itensEntrega1.empilhar(item1)
itensEntrega1.empilhar(item2)

itensEntrega2 = ItensEntrega()
itensEntrega2.empilhar(item3)
itensEntrega2.empilhar(item4)

itensEntrega3 = ItensEntrega()
itensEntrega3.empilhar(item5)
itensEntrega3.empilhar(item6)

# Criando os Locais
local1 = Local('777', 'Gabriel de Piza', itensEntrega1)
local2 = Local('109', 'Elvira da Fonseca', itensEntrega2)
local3 = Local('50', 'Sacadura Cabral', itensEntrega3)

# Criando e enfileirando os Locais
locais1 = Locais()
locais1.enfileirar(local1)
locais1.enfileirar(local2)

locais2 = Locais()
locais2.enfileirar(local3)

# Criando e fazendo a lista de caminhoes
caminhao1 = Caminhao('kxj9683', locais1)
caminhao2 = Caminhao('lts3192', locais2)

caminhoes = Caminhoes()
caminhoes.inserir(caminhao1)
caminhoes.inserir(caminhao2)

# Empilhando Itens para serem entregues
caminhoes.empilharItens()

# imprimindo a rotina dos caminhoes
caminhoes.imprimirRotina()


# Exibir os itens da entrega e os locais de entrega da lista de caminhões
# caminhoes.listarItensEntrega()
# caminhoes.listarLocais()

# l = locais.listar()

# for a in l:
#     a = a.listar()
#     print(a)
#     for i in a[2]:
#         print(i)
#         i = i.listar()
    

# def associaItemAoLocal():
#     for i in listaDeItens:
#         print(i)

#     idItemEntrega = input('Selecione o ID do Item a ser associado: ')

#     for i in listaDeLocais:
#         print(i)

#     idLocal = input('Selecione o ID do Local para associar ao Item: ')

#     idxItem = None

#     for idx, l in enumerate(listaDeItens):
#         x = l.get()
#         if idItemEntrega == x[0]:
#             idxItem = idx
#             itemAssociar = l

#     for idx, l in enumerate(listaDeLocais):
#         x = l.get()
#         if idLocal == x[0]:
#             localAssociar = l

#     localAssociar.associar(itemAssociar)
#     listaDeItens.pop(idxItem)

#     print('Item associado com sucesso ao Local')


# def associaLocalAoCaminhao():
#     for i in listaDeLocais:
#         print(i)

#     idLocal = input(
#         'Selecione o ID do Local a ser associado ao Caminhão: ')

#     for i in listaDeCaminhoes:
#         print(i)

#     placaCaminhao = input('Selecione a Placa do Caminhão: ')

#     for l in listaDeLocais:
#         x = l.get()
#         if idLocal == x[0]:
#             localAssociar = l

#     for c in listaDeCaminhoes:
#         x = c.get()
#         if placaCaminhao == x[0]:
#             caminhaoAssociar = c

#     caminhaoAssociar.associarLocal(localAssociar)

#     print('Local associado ao Caminhão com sucesso')


# def realizarEntregas():
#     idLocaisAssociados = []

#     # buscando caminhões
#     for caminhao in listaDeCaminhoes:
#         c = caminhao.get()

#         # Local que já está associado a um caminhão
#         for local in reversed(c[1]):
#             l = local.get()

#             # verificando se o Local possui itens
#             # este if é responsável por salvar o ID do Local que
#             # está associado ao caminhão e possui Itens para
#             # uma verificação posterior (Local Cadastrado sem Caminhão associado)
#             if local.possuiItensEntrega():
#                 idLocaisAssociados.insert(0, l[0])

#             # verificando os Itens que estão associados ao Local
#             # que está associado à este caminhão e colocando-os
#             # na caçamba
#             for item in l[2]:
#                 caminhao.associarItemEntrega(item)

#     # ----- PARTE DE LOCAL CADASTRATO SEM CAMINHÃO ASSOCIADO (NÃO CONCLUÍDO) ----- #

#     totalPontosVisitados = 0
#     totalItensEntregues = 0

#     for caminhao in listaDeCaminhoes:
#         if caminhao.possuiLocais():
#             c = caminhao.get()
#             print(f'Percurso do caminhão {c[0].upper()}')

#             for local in c[1]:
#                 l = local.get()
#                 totalPontosVisitados += 1
#                 print(
#                     f'    Visitado o Ponto de Entrega {l[1].upper()}. Foram entregue os itens:')

#                 for item in reversed(l[2]):
#                     i = item.get()
#                     totalItensEntregues += 1
#                     print(f'        {i[1]} - {l[1]}'.upper())

#             print(f'Percurso do caminhão {c[0].upper()} finalizado')
#             print('-----------------------------------------')
#         else:
#             print(
#                 f'Caminhão {caminhao.placa.upper()} não está associado a nenhum Local')

#     print('-----------------------------------------')
#     print(f'Total de pontos de entrega: {str(totalPontosVisitados)}')
#     print(f'Total de Itens entregues: {str(totalItensEntregues)}')
#     print('ROTINA FINALIZADA')


# def itemEntregaTopo():
#     return listaDeItens[len(listaDeItens) - 1]


# def exibirDadosDoLocal(Local):
#     local = Local.get()
#     print(f'ID {local[0]} - {local[1]}')
#     for item in local[2]:
#         i = item.get()
#         print(f'Item {i[0]} - {i[1]}')

# sair = False          

# while not sair:
#     print('---------- Menu Principal ----------')
#     print('1 - Inserir Ponto de Entrega')
#     print('2 - Inserir Item de Entrega')
#     print('3 - Inserir Caminhão')
#     print('4 - Associar item a ponto de entrega')
#     print('5 - Associar ponto de entrega a caminhão')
#     print('6 - Realizar entregas')
#     print('0 - Sair')
#     print('--------------------')

#     opcao = input('Opção escolhida -> ')

#     if opcao == '0':
#         sair = True
#         print('Programa finalizado')
#     elif opcao == '1':
#         id = str(input('Informe um Identificador para o ponto de entrega: '))
#         nome = str(input('Informe o nome do ponto de entrega à ser inserido: '))

#         local = Local(id, nome)
#         listaDeLocais.append(local)
#     elif opcao == '2':
#         id = str(input('Informe um Identificador para o item: '))
#         nome = str(input('Informe o nome do item à ser inserido: '))

#         itemEntrega = ItensEntrega(id, nome)
#         listaDeItens.append(itemEntrega)
#     elif opcao == '3':
#         placa = str(input('Informe a placa do Caminhão: '))

#         caminhao = Caminhao(placa)
#         listaDeCaminhoes.append(caminhao)
#     elif opcao == '4':
#         associaItemAoLocal()
#     elif opcao == '5':
#         associaLocalAoCaminhao()
#     elif opcao == '6':
#         realizarEntregas()
#     elif opcao == '8':
#         exibirDadosDoLocal(listaDeLocais[0])
#     elif opcao == '9':
#         for i in listaDeItens:
#             print(i)

#         for i in listaDeLocais:
#             print(i)

#         for i in listaDeCaminhoes:
#             print(i)

#         print(listaDeItens)
#         print(listaDeLocais)
#         print(listaDeCaminhoes)
#     else:
#         print(f'Opção {opcao} não é válida')
