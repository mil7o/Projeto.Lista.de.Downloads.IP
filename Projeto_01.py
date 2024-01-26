from datetime import datetime
listadownloads={}

def menu():
    print("1 - Cadastro de downloads")
    print("2 - Listagem de downloads")
    print("3 - Pesquisa de downloads")
    print("4 - Gerenciamento de downloads")
    print("5 - Sair")
    print('-' * 30)
    try:
        opcao=int(input("Opção: "))
        valorinteiro=True
    except ValueError:
        print('-' * 30)
        print('Opção inválida.')
        print('-' * 30)
        valorinteiro=False
    print('-' * 30)
    while valorinteiro==False:
        try:
            opcao = int(input("Opção: "))
            valorinteiro = True
        except ValueError:
            print('-' * 30)
            print('Opção inválida.')
            print('-' * 30)
            valorinteiro = False
    return opcao

def download():
    id = (input('ID: '))
    while id.isdigit()==False:
        print('-'*30)
        print('O ID deve conter apenas números!')
        id = input('Insira um ID válido: ')
    for arquivo in listadownloads.values():
        while id == arquivo.get('id'):
            print('ID já existente!')
            id=(input('Insira outro valor: '))
    nome=str(input('Nome: '))
    for arquivo in listadownloads.values():
        while arquivo.get('nome') == nome:
            print('Nome já existente!')
            nome = str(input('Renomeie o download: '))
    categoria=input('Categoria: ')
    categoria=categoria.capitalize()
    data=datetime.now()
    data_formatada=data.strftime('%d/%m/%Y')
    tamanho=input('Tamanho: ')
    tamanho=tamanho.upper()
    arquivo={'id':id, 'nome':nome, 'categoria':categoria, 'data':data_formatada, 'tamanho':tamanho}
    listadownloads[id,nome,]=arquivo
    print('-' * 30)
    print('Arquivo cadastrado com sucesso!')
    print('-' * 30)
   
def listar_download():
    print(f'{'Downloads':^30}')
    for arquivo in listadownloads.values():
        print('')
        print(f"ID: {arquivo.get('id')}")
        print(f"Nome: {arquivo.get('nome')}")
        print(f"Categoria: {arquivo.get('categoria')}")
        print(f"Data: {arquivo.get('data')}")
        print(f"Tamanho: {arquivo.get('tamanho')}")
        print('')
        print('-' * 30)


def pesquisar_download(nomeidpesq):
    if len(listadownloads)>0:
        found = False
        for arquivo in listadownloads.values():
            if arquivo.get('id')==nomeidpesq or arquivo.get('nome')==nomeidpesq:
                found = True
                print('-'*30)
                print('')
                print("ID: ", arquivo.get('id'))
                print("Nome: ", arquivo.get('nome'))
                print("Categoria: ", arquivo.get('categoria'))
                print("Data: ", arquivo.get('data'))
                print("Tamanho: ", arquivo.get('tamanho'))
                print('')
                print('-' * 30)
        if not found:
            print('DOWNLOAD NÃO ENCONTRADO!')

def gerenciar_download():
    if len(listadownloads)>0:
        print('1 - Excluir\n2 - Editar')
        print('-'*30)
        try:
            gerenciador = int(input('Opção: '))
        except ValueError:
            print('-' * 30)
            print('Opção inválida.')
            print('-' * 30)
            return

        if gerenciador == 1:
            id_excluir = input('Digite o nome ou ID do arquivo a ser excluído: ')
            for arquivo in listadownloads.values():
                if id_excluir in listadownloads:
                    del listadownloads[id_excluir]
                    print('Arquivo excluído com sucesso!')
                else:
                    print('ID não encontrado.')

        elif gerenciador == 2:
            id_editar = input('Digite o nome ou ID do arquivo a ser editado: ')
            print('-'*30)
            found=False
            for arquivo in listadownloads.values():
                if arquivo.get('id') == id_editar or arquivo.get('nome') == id_editar:
                    found=True

                    while True:
                        print('O que deseja editar?')
                        print(f"1 - ID: {arquivo.get('id')}")
                        print(f"2 - Nome: {arquivo.get('nome')}")
                        print(f"3 - Categoria: {arquivo.get('categoria')}")
                        print(f"4 - Tamanho: {arquivo.get('tamanho')}")
                        print('5 - Tudo')
                        print('6 - Voltar')
                        print('-'*30)
                        opcao_editar=int(input('Opção: '))
                        if opcao_editar==1:
                            novoid=input('Digite o novo ID do download: ')
                            for arquivo in listadownloads.values():
                                while arquivo.get('id') == novoid:
                                    print('ID já existente!')
                                    novoid = int(input('Insira outro valor: '))
                            arquivo.update({'id':novoid})
                        elif opcao_editar==2:
                            novonome=input('Digite o novo nome do download: ')
                            for arquivo in listadownloads.values():
                                while arquivo.get('nome') == novonome:
                                    print('Nome já existente!')
                                    novonome = str(input('Renomeie o download: '))
                            arquivo.update({'nome':novonome})
                        elif opcao_editar==3:
                            novocategoria=input('Digite a nova categoria do download: ')
                            arquivo.update({'categoria':novocategoria})
                        elif opcao_editar==4:
                            novotamanho=input('Digite o novo tamanho do download: ')
                            arquivo.update({'tamanho': novotamanho})
                        elif opcao_editar==5:
                            novoid=int(input('Digite o novo ID do download: '))
                            for arquivo in listadownloads.values():
                                while arquivo.get('id') == novoid:
                                    print('ID já existente!')
                                    novoid = int(input('Insira outro valor: '))
                            arquivo.update({'id':novoid})
                            novonome=input('Digite o novo nome do download: ')
                            for arquivo in listadownloads.values():
                                while arquivo.get('nome') == novonome:
                                    print('Nome já existente!')
                                    novonome = str(input('Renomeie o download: '))
                            arquivo.update({'nome':novonome})
                            novocategoria=input('Digite a nova categoria do download: ')
                            arquivo.update({'categoria': novocategoria})
                            novotamanho=input('Digite o novo tamanho do download: ')
                            arquivo.update({'tamanho': novotamanho})
                        elif opcao_editar==6:
                            return
                        else:
                            print('Opção inválida!')

                if not found:
                    print('Download não encontrado!')
    else:
        print('Nenhum download cadastrado!')
        input('Pressione qualquer tecla para continuar...\n')


def main():

    while True:
        opcao=menu()

        if opcao==1:
            download()
        elif opcao==2:
            listar_download()
        elif opcao==3:
            pesquisa=input('Digite ID ou Nome do arquivo: ')
            pesquisar_download(pesquisa)
        elif opcao==4:
            gerenciar_download()
        elif opcao==5:
            print('Saindo...')
            break
        else:
            print('Comando inválido!')

            input('Digite qualquer tecla para continuar...\n')

main()

#zeca pau gordinho
#piroka mole
#zzz




