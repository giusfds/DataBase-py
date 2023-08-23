from dataBase import *

def addNome():
    def addNames(name_list, name_to_add):
        if name_to_add in name_list:
            print("O nome ja existe na lista", end="\n")
        else:
            name_list.append(name_to_add)
            print(name_list)
    return

def removNome():
    def remove_name(list, name):
        if name in list:
            list.remove(name)
            print('name removed')
        else:
            print("nome nao encontrado na lista")
    return

def verificar():

    return

while True:
    print("Menu\n")
    print("opcao 0 para sair do programa")
    print("opcao 1 para adicionar um novo nome a lista")
    print("opcao 2 para remover um nome da lista")
    print("opcao 3 para ver se existe o nome na lista")
    entrada = int(input("Digite um número (0 para sair): "))
    
    if entrada == 0:
        break
    if entrada == 1:
        addNome()
        break
    if entrada == 2:
        removNome() 
        break
    if entrada == 3:
        removNome() 
        break

    
    
    # Aqui você pode colocar o código que deseja executar enquanto a entrada não for 0

print("Saindo do loop")