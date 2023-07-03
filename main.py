from ofclientes import *
from ofcontasapagar import*
from offornecedor import*
from ofnotasfiscais import*
from ofpecas import*
from ofservicos import*
from ofveiculos import*

def main():
    while True:
        try:
            print(8*"-=","Bem vindo a Mecânica do Ederson","-="*8)
            menu = input("Digite \n 1- Cadastro de Clientes \n 2- Cadastro de Peças \n 3- Cadastro de Notas Fiscais \n 4- Cadastro de Serviços \n 5- Cadastro de Contas a Pagar \n 6- Cadastro de Veículos \n 7- Cadastro de Fornecedor \n >>> ")  # menu
            if menu =="0":
                print(" Saindo...")
                print(8*"-=","Gracias, volte sempre !!!","-="*8)
                break
            switcher = {       
                "1":clientes,
                "2":peca,
                "3":notasf,
                "4":servic,
                "5":contasapagar,
                "6":veic,
                "7":fornece,
            }

            acao = switcher.get(menu)   # escolha da acao junto com armazenamento do def
            if acao:  # acao 
                acao()
            else:
                print("Opção não existente")
        except:
            print("Use apenas números !!!!")
            continue        
main()
