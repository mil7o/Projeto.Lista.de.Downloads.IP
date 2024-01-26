from Projeto_01 import *

def main():
    while True:
        opcao=opcao()
        if opcao==1:
            download()
        elif opcao==2:
            listardownload()
        elif opcao==3:
            pesquisadownload=input('Digite ID, nome ou data do arquivo: ')
            pesquisardownload(pesquisadownload)
        elif opcao==4:
            gerenciardownload()
        elif opcao==5:
            print('saindo...')
            break
        else:
            print('Comando inválido!')

            input('Digite qualquer tecla para continuar...')

main()













