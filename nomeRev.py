def remove_name(list, name):
        if name in list:
            list.remove(name)
            print('name removed')
        else:
            print("nome nao encontrado na lista")